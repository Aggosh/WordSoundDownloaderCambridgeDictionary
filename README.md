This program can download sound from https://dictionary.cambridge.org/

### Setup

Install requirements:
    ```
    pip install -r requirements.txt
    ```

### Run 
```
python3 main.py <additional command>
```
### Additional commands
```
-h - help
```
```
-w or --word - search word (Cat)
```
If word not selected, words will come from file word_list.txt (in the folder where main.py is located). In word_list.txt write words separated by commas (cat, dog, man)
```
-l or --limit - Max count of sounds (2)
```
```
-lang or --lang - Language (english)
```

The files will be downloaded to the folder sounds/search_word/search_word_1.mp3
