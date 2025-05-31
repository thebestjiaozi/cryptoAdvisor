def format_news_for_prompt(news_list, top_n=5):
    sorted_news = sorted(news_list, key=lambda x: x['published_at'], reverse=True)
    selected = sorted_news[:top_n]
    
    context = ""
    for i, item in enumerate(selected, 1):
        title = item.get("title", "")
        desc = item.get("description", "")
        date = item.get("published_at", "")
        context += f"{i}. {title} ({date})\n{desc}\n\n"
    
    return context.strip()
