# Correlation between Sentiment Analysis and Stock Movement

## Project Overview
This project aims to explore the correlation between public sentiment, as derived from news articles, and stock market movements. Our team has developed a comprehensive approach to collect, analyze, and interpret data to understand how sentiment reflects and possibly predicts stock prices.

### Objectives
- **Sentiment Analysis**: Analyze the sentiment of news articles related to major companies.
- **Stock Analysis**: Study stock price movements for the same companies.
- **Correlation Analysis**: Determine the relationship between news sentiment and stock performance.
- **Accuracy Assessment**: Validate the predictive power of sentiment analysis on stock prices.
- **AWS Integration**: Deploy our analysis via a Lambda function and create a conversational interface using Amazon Lex.

## Project Components

### Sentiment Analysis
- **Libraries Used**: NLTK, NewsAPI, Pandas, NumPy, and others for data handling and analysis.
- **Data Collection**: Articles fetched for multiple companies over a specified period using NewsAPI.
- **Analysis**: Sentiment scores calculated using NLTK's VADER tool, focusing on compound, positive, negative, and neutral scores.

### Stock Analysis
- **yfinance Library**: Used to fetch historical stock data, aligning dates with sentiment data for accurate comparison.
- **Data Points**: Primarily focused on stock prices but considering additional financial metrics for a comprehensive analysis.

### Correlation Analysis
- **Statistical Methods**: Employ various methods to identify and understand correlations between sentiment scores and stock movements.
- **Kendall Method**: Employed Kendall method for calculating correlation as it provides more accurate results for non-parametric data (in this situation the sentiment analysis data).

### Visualization
- **StandardScaler**: Used StandardScaler to create more visually accurate graphs by scaling the sentiment data to stock price movement.

### Accuracy and Validation
- **Testing**: Tested the accuracy of the recommendation with the actual price movement within the specified time.

### AWS Lambda and Amazon Lex Integration
- **Lambda Function**: Deploy our analysis code to AWS Lambda, ensuring it handles data fetching, processing, and error management effectively.
- **Amazon Lex**: Develop a conversational interface to allow users to query sentiment and stock analysis results.

## Development Workflow

1. **Data Collection**: Set up scripts to fetch and preprocess news articles and stock data.
2. **Sentiment Analysis**: Implement and test the sentiment analysis model.
3. **Stock Data Analysis**: Analyze stock data and align with sentiment data.
4. **Correlation Analysis**: Perform statistical analysis to discover correlations.
5. **Accuracy Assessment**: Test and validate our models and findings.
6. **AWS Integration**: Develop and test the AWS Lambda function and Lex bot.
7. **Review and Refinement**: Continuously test the entire workflow and refine based on findings and team feedback.

## Challenges and Considerations

- **API Limitations**: Managing and mitigating issues related to API rate limits and data availability.
- **User Interface**: Due to limitation of newsapi, had to hardcode the lambda function.

## Conclusion

It is a collaborative effort to understand and quantify the impact of public sentiment on stock markets. Through rigorous analysis and innovative technology integration. We aim to make the results more accurate by integrating more short term and long term analytical features and by better understanding the sentiment scores.

