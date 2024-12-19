import argparse
import config
import threading


def takeArgs():
    parser = argparse.ArgumentParser(description='bot token')
    parser.add_argument('token', type=str, help="type here bot token")
    token = parser.parse_args()
    config.bot = token.token


def startBots():
    import tele_bot
    import checker
    threadChecker = threading.Thread(target=checker.main)
    threadTeleBot = threading.Thread(target=tele_bot.main)
    threadChecker.start()
    threadTeleBot.start()
    print('хуй')


def main():
    startBots()


if __name__ == '__main__':
    main()
