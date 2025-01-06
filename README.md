# Social Media Performance Analysis

A Python application that analyzes social media engagement metrics using DataStax Astra DB and OpenAI's GPT model.

## Features

- Mock social media data generation
- Real-time engagement metrics visualization
- AI-powered insights using GPT-3.5
- Interactive dashboard using Streamlit
- Custom analytics workflows with Langflow

## Prerequisites

- Python 3.10+
- DataStax Astra DB account
- OpenAI API key

## Setup

1. Clone the repository:
```bash
git clone https://github.com/deepak-lenka/Social-Media-Performance-Analysis.git
cd Social-Media-Performance-Analysis
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file with your credentials:
```
ASTRA_DB_APPLICATION_TOKEN=your_token_here
ASTRA_DB_ID=your_db_id_here
OPENAI_API_KEY=your_openai_api_key_here
```

4. Create a `.streamlit/secrets.toml` file:
```toml
openai_api_key = "your_openai_api_key_here"
astra_db_token = "your_astra_db_token_here"
```

## Usage

1. Generate mock data:
```bash
python data_generator.py
```

2. Start the Streamlit application:
```bash
streamlit run app.py
```

3. Access the dashboard at http://localhost:8501

## Project Structure

- `app.py`: Main Streamlit application
- `data_generator.py`: Mock data generation script
- `db_operations.py`: Database operations and analytics
- `langflow_template.json`: Langflow workflow template
- `requirements.txt`: Project dependencies

## Analytics Features

- Post type performance comparison
- Engagement metrics visualization
- AI-generated insights and recommendations
- Custom analytics workflows

## License

MIT License 