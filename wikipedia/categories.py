import requests

def get_subcategories(category, depth=1):
  url = "https://en.wikipedia.org/w/api.php"
  subcategories = []
  params = {
    "action": "query",
    "list": "categorymembers",
    "cmtitle": f"Category:{category}",
    "cmtype": "subcat",
    "cmlimit": "max",
    "format": "json"
  }

  response = requests.get(url, params=params)
  data = response.json()

  for member in data['query']['categorymembers']:
    subcategories.append(member['title'])
    if depth > 1:
      subcategories.extend(get_subcategories(member['title'], depth - 1))

  return subcategories


top_level_categories = ["Geography", "Places", "Administrative divisions", "Regions", "Geographical features"]
all_subcategories = []

for category in top_level_categories:
  all_subcategories.extend(get_subcategories(category, depth=2))

print(all_subcategories)