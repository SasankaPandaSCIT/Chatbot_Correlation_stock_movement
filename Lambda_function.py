from datetime import datetime

# Running the code

amazon_compound_avg = 0.12380952380952381
google_compound_avg = 0.16447724374618106
tesla_compound_avg = -0.07602339181286549
microsoft_compound_avg = -0.35947712418300654
apple_compound_avg = -0.12280701754385964
meta_compound_avg = -0.0588235294117647
walmart_compound_avg = 0.2928895930645031
samsung_compound_avg = 0.1118445257474031
verizon_compound_avg = -0.09180377212587396

def analyze_news_compound_scores(compound_scores):
    positive_companies = []
    negative_companies = []

    # Categorise each company based on compound score
    for company, score in compound_scores.items():
        if score > 0:
            positive_companies.append(company)
        elif score < 0:
            negative_companies.append(company)

    # Format the response
    response = ""
    if positive_companies:
        positive_list = ", ".join(positive_companies)
        response += f"The news was positive for {positive_list}. "
    if negative_companies:
        negative_list = ", ".join(negative_companies)
        response += f"The news was negative for {negative_list}."
    
    # Handle case where there's no news or all neutral
    if not response:
        response = "There was no significant news for the companies."

    return response

# Dataset
compound_scores = {
    "Amazon": amazon_compound_avg,
    "Google": google_compound_avg,
    "Tesla": tesla_compound_avg,
    "Microsoft": microsoft_compound_avg,
    "Apple": apple_compound_avg,
    "META": meta_compound_avg,
    "Walmart": walmart_compound_avg,
    "Samsung": samsung_compound_avg,
    "Verizon": verizon_compound_avg
}

response = analyze_news_compound_scores(compound_scores)
response



def analyze_stock_investment_opportunity(compound_scores, stock_correlation_dict):
    investment_advice = {}

    for company, compound_score in compound_scores.items():
        sentiment = "positive" if compound_score > 0 else "negative"
        correlation = stock_correlation_dict.get(company, 0)

        if sentiment == "positive":
            if correlation > 0:
                advice = "There is a positive correlation between the stock and the news, so it might be a good option for investing."
            else:
                advice = "There is a negative correlation, so I don't recommend investing in this."
        else:  # Negative sentiment
            if correlation < 0:
                advice = "The news was bad but it is negatively correlated, so it might be a good option to invest."
            else:
                advice = "The news was bad and there is a positive correlation, so it might not be a good option to invest."

        investment_advice[company] = advice

    return investment_advice

# dataset
compound_scores = {
    "Amazon": amazon_compound_avg,
    "Google": google_compound_avg,
    "Tesla": tesla_compound_avg,
    "Microsoft": microsoft_compound_avg,
    "Apple": apple_compound_avg,
    "META": meta_compound_avg,
    "Walmart": walmart_compound_avg,
    "Samsung": samsung_compound_avg,
    "Verizon": verizon_compound_avg
}

stock_correlation_dict= {
    'Amazon': 0.12380952380952381,
    'Google': 0.16447724374618106,
    'Tesla': -0.07602339181286549,
    'Microsoft': -0.35947712418300654,
    'Apple': -0.12280701754385964,
    'META': -0.0588235294117647,
    'Walmart': 0.2928895930645031,
    'Samsung': 0.1118445257474031,
    'Verizon': -0.09180377212587396,
}

advice = analyze_stock_investment_opportunity(compound_scores, stock_correlation_dict)

for company, advice_string in advice.items():
    print(f"{company}: {advice_string}")


def lambda_handler(event, context):
    intent_name = event['currentIntent']['name']

    if intent_name == "sentiment_score":
        response = analyze_news_compound_scores(compound_scores)
    elif intent_name == "correlation_analysis":
        response = analyze_stock_investment_opportunity(compound_scores, stock_correlation_dict)
    else:
        response = "Sorry, I did not understand that."

    # Format the response for Lex
    lex_response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": response
            }
        }
    }

    return lex_response


import json