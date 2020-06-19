import logging
import argparse
import os
from datetime import datetime
import signal
import pyfiglet

parser = argparse.ArgumentParser()
parser.add_argument('-output', '-o', action='store', help='Path for Diary entries')
parser.add_argument('-file', '-f', action='store', help='File Name')
parser.add_argument('-name', '-n', action='store', help='Name Entry')
parser.add_argument('-people', '-p', action='store', help='People Entry')
parser.add_argument('-info', '-a', action='store', help='Additional Information entry')
args = parser.parse_args()

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)

VERSION = "v0.1"


def startup_logger(path):
    diary_exist, full_path = diary_check(path)

    if diary_exist:
        save_to_file(path, "-"*20 + "\n")  # Add divider
        respawn_diary(full_path)
    else:
        generate_diary_banner(path)
        diary_exist, full_path = diary_check(path)
        respawn_diary(full_path)

    while True:
        entry = input("\n")
        generate_txt(path, entry)
        full_file_path = grab_full_path(path)
        respawn_diary(full_file_path)


def diary_check(path):  # Check if a diary has already been created for this date and load that
    full_path = grab_full_path(path)
    file_exist_boolean = file_exist_check(full_path)

    if file_exist_boolean:
        return True, full_path
    else:
        return False, None


def file_exist_check(full_path):
    if os.path.isfile(full_path):
        return True
    else:
        return False


def respawn_diary(path_file):
    os.system('cls' if os.name == 'nt' else 'clear')  # Works on win and linux
    diary = read_file(path_file)

    print(diary)


def read_file(path_file):
    with open(path_file, 'r') as file:
        diary = file.read()
    return diary


def close_app(signum, frame):  # Is called when Control + C is called
    logging.info("[!] Closing Diary")
    exit()


def generate_diary_banner(path):
    title = pyfiglet.figlet_format("Dear Diary " + VERSION, font="slant")

    now = datetime.now()

    date = datetime.date(now)
    name = str(args.name)
    people = str(args.people)
    info = str(args.info)

    banner = "%s\nDate: %s\nName: %s\nPeople: %s\nInfo: %s\n\n" % (title, date, name, people, info)
    save_to_file(path, banner)


def generate_txt(file_path, text_str):
    now = datetime.now()
    time_now = datetime.time(now).replace(microsecond=0)  # Remove microseconds from time output

    full_file_path = grab_full_path(file_path)  # e.g path/to/folder/date
    text = "[%s] %s \n" % (time_now, text_str)

    save_to_file(file_path, text)

    return full_file_path


def grab_full_path(file_path):
    now = datetime.now()
    date_now = datetime.date(now)
    full_file_path = file_path + str(date_now) + str("_" + args.file)  # e.g path/to/folder/date

    return full_file_path


def save_to_file(path, text):
    now = datetime.now()
    date_now = datetime.date(now)

    full_file_path = path + str(date_now) + str("_" + args.file)  # e.g path/to/folder/date

    with open(full_file_path, 'a') as f:
        f.write(text)


def check_path(path):
    if not os.path.exists(path):
        return False
    else:
        return True


if __name__ == "__main__":
    signal.signal(signal.SIGINT, close_app)  # SIGINT for the Control+C when it is used to close the program
    path = args.output

    if check_path(path):
        startup_logger(path)
    else:
        logging.info("[!] The path selected %s does not exist" % path)
