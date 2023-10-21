# youtubepostslinksextractor
This extracts post links and posts names from multiple youtube channel's post page.

# How To:
Install Python.
Copy/Download Code and open the code in Visual Studio Code root directory.
Windows: Copy paste in VSCode Terminal. If prompted to change environment, select yes.
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
clear

```

Change the url in the quotes.py file here: Make sure it points to the videos page and not the channel's homepage
```
# Define the URL of the YouTube channel's videos page in the code itself under channels. Make sure they point to the videos page.

```
For this project, I have added a timer for the time being. You can set it to what you like as I am unable to extract the number of posts of a channel and decide before hand how long the code should run
```
scroll_duration = 5
```

You can keep your terminal open on the side to see how much time is remaining for the scroll as the scroll time is dependent on the number of videos on that youtube channel.


A new file will be created when the links are extracted. You can copy paste it directly in database or excel and it will retain it's structure since it has a tab character in between then.
