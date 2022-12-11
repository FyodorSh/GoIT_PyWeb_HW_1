from commands import bot
from parse_utils import parse_input


def main():
    try:
        while True:
            command_input = input("Enter command: ")
            result = parse_input(command_input)
            print(result)
            if result == 'good bye':
                break
    finally:
        bot.save_data()


if __name__ == "__main__":
    main()
