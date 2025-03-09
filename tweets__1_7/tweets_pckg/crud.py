from datetime import datetime  # Для получения текущей даты и времени

# Глобальные переменные.
tweets = {}  # Словарь для хранения твитов.
next_tweet_id = 1  # Счетчик для уникальных ID твитов.

def create_tweet(text):
    """Функция создания нового твита
    проверяет текст на пустоту. генерит текущую дату/время
    создает словарь с данными: текст твита и дата создания
    присваивает uid и добавляет это в словарь tweets"""
    global next_tweet_id
    if not text.strip():
        print("tweet text cannot be empty!")

    timestamp = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    tweet = {"text": text, "timestamp": timestamp}
    tweets[next_tweet_id] = tweet
    print(f"tweet added successfully! tweet ID: {next_tweet_id}")
    next_tweet_id += 1


def update_tweet(tweet_id, new_text):
    """Функция, позволяющая изменить текст твита
    проверяет на существование-> потом что новый тест не пустой 
    и -> изменяет текст на вновь введенный"""
    if tweet_id not in tweets:
        print("tweet not found!")
    if not new_text.strip():
        print("tweet text cannot be empty!")

    tweets[tweet_id]["text"] = new_text
    print("tweet edited successfully!")


def delete_tweet(tweet_id):
    """Функция удаления твита
    проверяет на существование и удаляет если есть
    """
    
    if tweet_id not in tweets:
        print("tweet not found!")

    deleted_tweet = tweets.pop(tweet_id)
    print(f"tweet deleted: {deleted_tweet['text']}")


def show_tweets():
    """Показывает все твиты.
    проверяет есть ли твиты в словаре tweets, если нет то выводит сообщение о том, 
    что лента пуста, а иначе выводит твиты"""
    
    if not tweets:
        print("Your Tweets feed is empty!")
    else:
        print("\nTweets Feed:")
        for tweet_id, tweet in tweets.items():
            print(f"tweet ID: {tweet_id}")
            print(f"Text: {tweet['text']}")
            print(f"tweeted on: {tweet['timestamp']}")
            print("=" * 80)
        print()
        