import requests
from urllib import parse
from bs4 import BeautifulSoup



base_url = "https://en.wikipedia.org/wiki/History_of_Mexico"
page = requests.get(base_url)


def get_citations_needed_count():
  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find_all(title = "Wikipedia:Citation needed")
  citations_count = 0
  
  for result in results:
    citations_count += 1

  print(f"This page: {base_url} needs {citations_count} citations")



def get_citations_needed_report():
  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find_all(title = "Wikipedia:Citation needed")
  citations_needed = []

  for result in results:
    citations_needed.append(result.parent.parent.parent.text)

  for paragraph in citations_needed:
    print(paragraph)


get_citations_needed_count()
get_citations_needed_report()
