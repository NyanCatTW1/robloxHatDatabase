#!/usr/bin/python3
import requests
import json

extracted = {}
try:
  with open("hats.json", "r") as f:
    extracted = json.loads(f.read())
except Exception:
  pass

cursor = None

while True:
  url = "https://catalog.roblox.com/v1/search/items/details?Category=11&MaxPrice=50&Subcategory=9&SortType=4&Limit=30"
  if cursor is not None:
    url += "&cursor={}".format(cursor)
  response = requests.get(url).content
  data = json.loads(response)

  for hat in data["data"]:
    if str(hat["id"]) not in extracted:
      extracted[str(hat["id"])] = {"name": hat["name"], "price": hat["price"]}
      print(extracted[str(hat["id"])])
      keepGoing = True

  print(len(extracted))
  cursor = data["nextPageCursor"]
  if cursor is None:
    break

with open("hats.json", "w") as f:
  json.dump(extracted, f, sort_keys=True, indent=2)
  f.close()
