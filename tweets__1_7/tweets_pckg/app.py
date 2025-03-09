from tweets_pckg.crud import create_tweet, update_tweet, delete_tweet, show_tweets


def show_menu():
    """Показывает меню и возвращает выбранный пункт."""
    menu = """
    ====================================================================================================
    |                                       TWEETS APP PROJECT                                         |
    ====================================================================================================
    |                                       1 - Add a new tweet                                        |
    |                                       2 - Update a tweet                                         |
    |                                       3 - Delete a tweet                                         |
    |                                       4 - Show all tweets                                        |
    |                                       -1 - Exit                                                  |
    ====================================================================================================
    """
    return int(input(menu))


def get_tweet_text():
    """Запрашивает текст твита у пользователя."""
    return input("Enter tweet text: ")


def get_tweet_id():
    """Запрашивает ID твита у пользователя"""
    return int(input("Enter the tweet ID: "))

def main():
    """Меню программы"""
    oper = show_menu()

    while oper != -1:
        try:
        

            if oper == 1:
                text = get_tweet_text()
                create_tweet(text)
            elif oper == 2:
                tweet_id = get_tweet_id()
                new_text = get_tweet_text()
                update_tweet(tweet_id, new_text)
            elif oper == 3:
                tweet_id = get_tweet_id()
                delete_tweet(tweet_id)
            elif oper == 4:
                show_tweets()
            else:
                print("Invalid option! Please try again.")
        except ValueError:
            print(f"Error: tweet text can't be empty!")
        except KeyError:
            print(f"Error: tweet not found")
        oper = show_menu()

    print("=================================================Exit=================================================")
