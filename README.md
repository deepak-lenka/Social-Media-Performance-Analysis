# Social Media Performance Analysis

A sophisticated Python application that leverages DataStax Astra DB and OpenAI's GPT model to analyze social media engagement metrics and provide actionable insights.

## 🚀 Features

- **Real-time Analytics**
  - Track likes, comments, and shares across different post types
  - Compare performance metrics between carousel, reels, and static posts
  - Generate engagement rate analysis and trends

- **AI-Powered Insights**
  - Automated content performance analysis using GPT-3.5
  - Personalized recommendations for content strategy
  - Comparative analysis between different post formats

- **Interactive Dashboard**
  - Clean and intuitive Streamlit interface
  - Dynamic visualization of engagement metrics
  - Filter and analyze data by post type

- **Custom Analytics Workflows**
  - Flexible Langflow integration
  - Customizable analysis parameters
  - Extensible workflow templates

## 🛠️ Technologies Used

- **DataStax Astra DB**: Cloud-native Cassandra database
- **Langflow**: Workflow creation and GPT integration
- **Streamlit**: Interactive web interface
- **OpenAI GPT**: AI-powered insights generation
- **Python**: Core application logic

## 📋 Prerequisites

- Python 3.10+
- DataStax Astra DB account
- OpenAI API key
- Langflow installation

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/deepak-lenka/Social-Media-Performance-Analysis.git
cd Social-Media-Performance-Analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file based on `.env.template`
   - Add your DataStax Astra DB credentials
   - Include your OpenAI API key

5. Configure Streamlit secrets:
   - Create `.streamlit/secrets.toml`
   - Add required API keys and tokens

## 🚀 Usage

1. Generate mock data:
```bash
python data_generator.py
```

2. Start the Streamlit application:
```bash
streamlit run app.py
```

3. Access the dashboard at `http://localhost:8501`

## 📁 Project Structure

```
├── app.py                    # Main Streamlit application
├── data_generator.py         # Mock data generation script
├── db_operations.py          # Database operations
├── langflow_template.json    # Langflow workflow configuration
├── requirements.txt          # Project dependencies
├── .env.template            # Environment variables template
└── README.md                # Project documentation
```

## 🔍 Analytics Features

### Post Performance Analysis
- Engagement rate calculation
- Post type comparison
- Trend analysis
- Performance benchmarking

### AI-Generated Insights
- Content strategy recommendations
- Performance improvement suggestions
- Engagement optimization tips
- Audience behavior analysis

### Custom Metrics
- Average engagement per post type
- Comment sentiment analysis
- Share-to-like ratio
- Growth rate tracking

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- DataStax for providing the Astra DB platform
- OpenAI for the GPT API
- Langflow community for workflow tools
- Streamlit team for the amazing dashboard framework

## 📧 Contact

Deepak Lenka - iamdeepak034@gmail.com

Project Link: [https://github.com/deepak-lenka/Social-Media-Performance-Analysis](https://github.com/deepak-lenka/Social-Media-Performance-Analysis) 