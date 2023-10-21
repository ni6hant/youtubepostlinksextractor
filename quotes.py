import time
from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm

#Set this accordingly
scroll_duration = 5

# Define the URL of the YouTube channel's post page.
# channels = [
#     'https://www.youtube.com/@makingtechfriendlyindia/community'
# ]

# Note: You can add more channels like this but since different channels might have different number of posts,
# it might be better to do it one by one. However, if you have a lot of time, you can set the scroll_duration
# to a long time and let the code run as it is
channels = [
    'https://www.youtube.com/@ni6hant/community',
    'https://www.youtube.com/@ni6hantgaming/community',
    'https://www.youtube.com/@ni6hantgamingindia/community',
    'https://www.youtube.com/@makingtechfriendly/community',
    'https://www.youtube.com/@makingtechfriendlyindia/community'
]

# Create a list to store post information
post_info = []


#Iterate through the YouTube Channel lists to go over them one by one:
for channel in channels:
    # Initialize Selenium WebDriver without specifying executable_path
    driver = webdriver.Chrome()
    
    # Open the channel URL
    driver.get(channel)

    # Parse the HTML content with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')



    # Execute JavaScript to scroll to the bottom of the page
    driver.execute_script('''
        var scroll = setInterval(function(){
            window.scrollBy(0, 1000);a
        }, 1000);
    ''')

    # Initialize the progress bar
    with tqdm(total=scroll_duration, unit="s", desc="Scrolling") as pbar:
        # Wait for the calculated duration to allow content to load
        for _ in range(int(scroll_duration)):
            time.sleep(1)
            pbar.update(1)  # Update the progress bar

    # Get the updated page source
    updated_page_source = driver.page_source

    # Close the web driver
    driver.quit()

    # Parse the updated HTML content with BeautifulSoup
    soup = BeautifulSoup(updated_page_source, 'html.parser')
    
    # Find all the post containers
    post_containers = soup.find_all('ytd-backstage-post-thread-renderer')

    # Iterate through the post elements and extract information
    for post in post_containers:
        post_element = post.find('yt-formatted-string', {'id': 'content-text'})
        post_text = post_element.get_text(strip=True)[:100].replace('\n', ' ').replace('\r', ' ')
        a_tag = post.find('a', class_='yt-simple-endpoint style-scope yt-formatted-string').get('href')
        post_url = "https://www.youtube.com/" + a_tag
        post_info.append(f"{post_text}\t{post_url}")

# Write the post information to a text file
with open('post_info.txt', 'w', encoding='utf-8') as output_file:
    for entry in post_info:
        output_file.write(entry + '\n')

print("Post information has been saved to post_info.txt")
print(f"Total posts found: {len(post_info)}")
