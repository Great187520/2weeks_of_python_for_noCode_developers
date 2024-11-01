#CRUD
""" CREATE READ UPDATE DELETE """
""" GET POST PUT DELETE """

import requests

#Make a GET request to the API
""" response = requests.get("https://jsonplaceholder.typicode.com/posts")


#Check if the request was successful 
if response.status_code == 200:
    posts = response.json() #Parse JSON response
    for post in posts[:5]: #Display the first 5 posts
        print(f"Title: {post['title']}\nBody: {post['body']}\n")


else:
    print("Failed to retrieve data:", response.status_code) """


#Fetching Data from External serives
#Using Query Parameters
""" user_id = 1
response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")

if response.status_code == 200:
    posts = response.json()
    for post in posts:
        print(f"Title: {post['title']}\n")
else:
    print("Failed to retrieve data:", response.status_code) """

#Sending Data with POST Requests
""" new_post = {
    "title": "My New Post",
    "body": "This is a post",
    "userId": 1
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)

if response.status_code == 201:
    print("Post created successfully:", response.json())
else:
    print("Failed to create post:", response.status_code) """

#Introduction to web scraping with beautiful soup
#Parsing HTML with beautifulsoup
""" from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else: 
    print("Failed to retrieve the web page:", response.status_code)

soup = BeautifulSoup(html_content, 'lxml') #parse the HTML content

#Print the title of the page
print(soup.title.string) """

#handling dynamic content with Selenium
from selenium import webdriver
from selenium.webdriver.common.by import  By

driver = webdriver.Chrome()

driver.get("https://example-blog.com")

#Wait for the page to load and find elements
titles = driver.find_elements(By.TAG_NAME, 'h2')


for title in titles:
    print(title.text)

driver.quit()
