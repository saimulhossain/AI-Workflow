# AI Business Solution
A machine learning-based business solution for sales prediction, deployed with a Flask API and containerized using Docker.

## Overview
This project provides a scalable AI workflow for predicting sales by country, with features including:
- Flask API for predictions
- Random Forest model with baseline comparison
- Automated data ingestion
- Logging and performance monitoring
- Comprehensive unit tests
- EDA with visualizations
- Docker containerization

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-business-solution.git
   cd ai-business-solution
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python -m app
   ```

4. **Run Unit Tests**:
   ```bash
   python tests/run_tests.py
   ```

5. **Build and Run Docker Container**:
   ```bash
   docker build -t ai-business-solution .
   docker run -p 5000:5000 ai-business-solution
   ```

## API Endpoints
- **GET /predict?country=<country_name>**: Predict sales for a specific country.
- **GET /predict**: Predict sales for all countries combined.

Example:
```bash
curl "http://localhost:5000/predict?country=USA"
```

## License
MIT License