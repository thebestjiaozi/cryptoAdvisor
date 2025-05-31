from coingecko import fetch_coin_data
from gemini_analyst import ask_gemini, build_prompt
from config import TARGET_COIN, CURRENCY, HISTORY_DAYS
from fetch_news import fetch_news
from formatter import format_news_for_prompt
from telegram_utils import send_telegram_message


def run_analysis(return_output=False, send_to_telegram=False):
    try:
        print("=== Fetching market data ===")
        coin_data = fetch_coin_data(TARGET_COIN, CURRENCY, HISTORY_DAYS)

        print("=== Fetching news data ===")
        news_list = fetch_news()
        news_context = format_news_for_prompt(news_list)

        print("=== Building Gemini prompt ===")
        prompt = build_prompt(coin_data, news_context)

        print("=== Sending to Gemini ===")
        result = ask_gemini(prompt)

        print("=== Investment Suggestion ===")
        print(result)

        if send_to_telegram:
            if len(result) <= 4000:
                send_telegram_message(result)
            else:
                for i in range(0, len(result), 4000):
                    send_telegram_message(result[i:i+4000])

        if return_output:
            return result

    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        return "An error occurred during analysis."
