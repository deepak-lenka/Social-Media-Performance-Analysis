import os
from dotenv import load_dotenv
from astrapy.db import AstraDB
import pandas as pd

class SocialMediaAnalytics:
    def __init__(self):
        load_dotenv()
        self.setup_connection()

    def setup_connection(self):
        ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
        
        # Initialize the client
        self.db = AstraDB(
            token=ASTRA_DB_APPLICATION_TOKEN,
            api_endpoint="https://a989e7a0-77e1-455f-a09f-e317ee50519f-us-east1.apps.astra.datastax.com"
        )
        
        # Get collection reference
        self.collection = self.db.collection('posts')

    def get_engagement_metrics(self, post_type=None):
        if post_type and post_type != "All Types":
            results = self.collection.find({"post_type": post_type}).get('data', {}).get('documents', [])
        else:
            results = self.collection.find({}).get('data', {}).get('documents', [])
        
        # Process results into metrics
        metrics = []
        for ptype in ['carousel', 'reel', 'static']:
            type_posts = [p for p in results if p.get('post_type') == ptype]
            if type_posts:
                metrics.append({
                    'post_type': ptype,
                    'avg_likes': sum(p['likes'] for p in type_posts) / len(type_posts),
                    'avg_shares': sum(p['shares'] for p in type_posts) / len(type_posts),
                    'avg_comments': sum(p['comments'] for p in type_posts) / len(type_posts)
                })
        
        return metrics

    def generate_insights(self, metrics):
        if not metrics:
            return ["No data available to generate insights."]
            
        insights = []
        df = pd.DataFrame(metrics)
        
        for idx, row in df.iterrows():
            other_posts = df[df.post_type != row.post_type]
            if len(other_posts) > 0:
                avg_other_likes = other_posts['avg_likes'].mean()
                likes_diff_pct = ((row['avg_likes'] - avg_other_likes) / avg_other_likes) * 100
                
                insights.append(f"{row.post_type.capitalize()} posts have "
                              f"{'higher' if likes_diff_pct > 0 else 'lower'} engagement "
                              f"with {abs(likes_diff_pct):.1f}% "
                              f"{'more' if likes_diff_pct > 0 else 'fewer'} likes "
                              f"compared to other formats")
        
        return insights 