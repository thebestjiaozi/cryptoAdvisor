from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL
from formatter import format_news_for_prompt

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_price_data(coin_data):
    latest = coin_data[-1]
    text = f"Latest price of Bitcoin is ${latest['price']:.2f} at {latest['timestamp']}. What is your investment advice?"
    return text

def build_prompt(coin_data, news_context):
    return f"""
You are a professional crypto day trader and analyst.

Below is the latest market data and news headlines collected **today** ({coin_data[-1]['timestamp']}):

===== PRICE DATA =====
{generate_price_data(coin_data)}

===== LATEST NEWS =====
{news_context}

Your task:
Analyze today's news and real-time price movements to provide **clear, concise, and actionable trading advice** for short-term (intraday) decisions.

Please respond with:
1. What is the **overall market sentiment** (bullish / bearish / mixed)? Why?
2. Identify **any major news events** today that are likely to trigger immediate price movements. Rate their **impact level** (Low/Medium/High).
3. For **each major coin mentioned** (e.g., BTC, ETH), give a trading decision:
   - Should I BUY, SELL, or HOLD **today**?
   - At what conditions (price level or confirmation signal) should I execute the trade?
4. Highlight any **urgent alerts or trade signals** (e.g., panic sell, breakout, whale activity) that require immediate action.

Your output should be written clearly and professionally. Avoid vague terms. Be specific. Think like a day trader who must act on the market within hours.
"""


def analyze_market(news_list):
    news_context = format_news_for_prompt(news_list)
    prompt = build_prompt(news_context)
    result = ask_gemini(prompt)
    return result


def ask_gemini(prompt):
    response = client.models.generate_content(
        model=GEMINI_MODEL,contents=prompt
    )
    return response.text
