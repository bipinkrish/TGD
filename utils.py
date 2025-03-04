from sys import stdout, exit
from pyrogram.types import Message
from pyrogram import enums
from time import time
from os import system, name as osname


def wait():
    try:
        input("Press enter to exit...")
    except KeyboardInterrupt:
        pass
    finally:
        exit(0)


SPEED_DATA = {}


def progress(current, total, uuid):
    current_time = time()
    length = 50

    if uuid in SPEED_DATA:
        elapsed_time = current_time - SPEED_DATA[uuid]["last_time"]
        speed = (current - SPEED_DATA[uuid]["progress"]) / elapsed_time
    else:
        speed = 0

    SPEED_DATA[uuid] = {"last_time": current_time, "progress": current}
    progress_percent = current * 100 / total
    completed = int(length * current / total)

    bar = f"[{'#' * completed}{' ' * (length - completed)}] {progress_percent:.1f} % - {convert_bytes(speed)}/s - {convert_bytes(current)}"
    stdout.write(f"\r{bar}")
    stdout.flush()


available_media = ("audio", "document", "photo", "sticker",
                   "animation", "video", "voice", "video_note")


def get_media_type(message: Message) -> enums.MessageMediaType:
    if isinstance(message, Message):
        for kind in available_media:
            media = getattr(message, kind, None)
            if media is not None:
                return media
        else:
            return None


def convert_bytes(size, precision=2):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    suffix_index = 0

    while size >= 1024 and suffix_index < len(suffixes) - 1:
        suffix_index += 1
        size /= 1024.0

    return f"{size:.{precision}f} {suffixes[suffix_index]}"


def get_file_name(media: enums.MessageMediaType) -> str:
    try:
        return media.file_name
    except:
        return media.file_unique_id


def print_dowload_msg(media: enums.MessageMediaType, msgid: int, fromID: int, total: int):
    print(
        f"{get_file_name(media)} -",
        f"{media.__class__.__name__} -",
        f"{convert_bytes(media.file_size)}",
        f"({(msgid - fromID + 1)}/{total})",
    )


def print_examples():
    print("""
Examples:

    https://t.me/xxxx/1423
    https://t.me/c/xxxx/10
    https://t.me/xxxx/1001-1010
    https://t.me/c/xxxx/101 - 120"""
          )


configfile = "tgd.txt"
TGD = """
  ▄██████▄    ▄██████▄    ████████▄
 ██▀▀███▀▀██  ███    ███  ███   ▀███
     ███      ███    █▀   ███    ███
     ███     ▄███         ███    ███
     ███    ▀▀███ ████▄   ███    ███
     ███      ███    ███  ███    ███
     ███      ███    ███  ███   ▄███
    ▄████    ████████▀   ████████▀
"""
VERSION = "1.3"

system("cls" if osname == "nt" else "clear")
print(TGD)
print("	TeleGram Downloader")
print(f"	    Version {VERSION}\n")
