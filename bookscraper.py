URL = "https://automationbookstore.dev/"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

options = Options()
# options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(URL)

book_list = {'title':[], 'author':[], 'price':[]}

def convert_books_to_csv():

  try:
      find_titles = driver.find_elements(By.TAG_NAME, 'h2')
      for title in find_titles:
          book_list['title'].append(title.text)
      find_authors = driver.find_elements(By.TAG_NAME, 'p')
      for index, element in enumerate(find_authors):
          if index % 2 == 0:
              book_list['author'].append(element.text)
          else:
              book_list['price'].append(element.text)
  except:
      driver.quit()
  
  df = pd.DataFrame(book_list)
  df.to_csv('book_list.csv', index=False)
