import requests
import urllib.request
import re
import os
import getopt
import sys

from bs4 import BeautifulSoup


def download_sound(
    searched_word, lang="english", limit=3, url="dictionary.cambridge.org"
):
    """Downloads sound files from the site
    Args:
        searched_word (str): The word you need to pronounce.
        lang (str): Language of this word.
        limit (int): Max count of sound files.
        url (str): url.
    Returns:
        None
    """

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.360"

    headers = {
        "User-Agent": USER_AGENT,
    }
    r = requests.get(
        f"https://{url}/dictionary/{lang}/{searched_word}", headers=headers
    )
    soup = BeautifulSoup(r.content, "html.parser")

    for index, word in enumerate(soup.findAll("source", type="audio/mpeg")):
        path = word.get("src")
        sound_url = f"https://{url}{path}"
        sound_path = f"sounds/{searched_word}/{searched_word}_{index+1}.mp3"

        opener = urllib.request.build_opener()
        opener.addheaders = [("User-agent", USER_AGENT)]
        urllib.request.install_opener(opener)

        create_file(sound_path)  # Create folder and file for sound
        urllib.request.urlretrieve(sound_url, sound_path)
        print(f"Downloading {searched_word}_{index+1}.mp3 was complited!")

        if index + 1 >= limit:
            break


def create_file(path):
    """Create folder and file
    Args:
        path (str): Path to file.
    Returns:
        None
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write("Pass")


def param_parser(argv):
    """Parse additional params
    Args:
        argv (list): Row additional params.
    Returns:
        str: word
        int: limit
        str: lang
    """
    word = ""
    limit = 2
    lang = "english"

    try:
        opts, args = getopt.getopt(argv[1:], "hw:l:lang", ["word=", "limit=", "lang="])
    except getopt.GetoptError:
        print(f"{argv[0]} -w <word> -l <limit> -lang <language>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(f"{argv[0]} -w <word> -l <limit> -lang <language>")
            sys.exit()
        elif opt in ("-w", "--word"):
            word = arg
        elif opt in ("-l", "--limit"):
            limit = int(arg)
        elif opt in ("-lang", "--lang"):
            lang = arg

    if word == "":
        print("Words will be received from word_list.txt")
    else:
        print("Word:", word)

    print("Limit:", limit)
    print("Language:", lang)

    return (word, limit, lang)


def main():
    word, limit, lang = param_parser(sys.argv)

    if word == "":
        word_list = []
        with open("word_list.txt") as f:
            word_list = f.read().replace(" ", "").split(",")

        for word in word_list:
            download_sound(word, limit=limit, lang=lang)
    else:
        download_sound(word, limit=limit, lang=lang)


if __name__ == "__main__":
    main()
