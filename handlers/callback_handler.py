from utils.csv_utils import read_csv_data

def get_reviews_for_app(data, app_name, n=5):
    reviews = data[data['App'] == app_name]
    return reviews.head(n)

def format_reviews(reviews):
    if reviews.empty:
        return "No reviews found."
    output = []
    for i, row in reviews.iterrows():
        output.append(f"Review {i+1}:\n{row['Translated_Review']}\nSentiment: {row['Sentiment']}\n")
    return "\n".join(output)

async def button_handler(update, context):
    query = update.callback_query
    await query.answer()
    app_name = query.data.split(":")[1]

    reviews_data = read_csv_data(r"C:\Users\ASUS\OneDrive\دسکتاپ\googleplaystore_user_reviews.csv")
    reviews = get_reviews_for_app(reviews_data, app_name)
    await query.message.reply_text(format_reviews(reviews))