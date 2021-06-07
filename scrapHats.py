#!/usr/bin/python3
import requests
import json

cursor = None

extracted = {}

while True:
  url = "https://catalog.roblox.com/v1/search/items/details?Category=11&MaxPrice=50&Subcategory=9&SortType=4&Limit=30"
  if cursor is not None:
    url += "&cursor={}".format(cursor)
  response = requests.get(url).content
  data = json.loads(response)

  for hat in data["data"]:
    extracted[hat["id"]] = {"name": hat["name"], "price": hat["price"]}
    print(extracted[hat["id"]])

  cursor = data["nextPageCursor"]
  if cursor is None:
    break

with open("hats.json", "w") as f:
  json.dump(extracted, f, sort_keys=True, indent=2)
  f.close()
