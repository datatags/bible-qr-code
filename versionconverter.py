import json

# Use this script to update the contents of the versions dict
# in the get_version_code function in bibleqrcode.py
#
# This can't be done programmatically because it's protected
# by CloudFlare.

print("Paste content of: https://www.bible.com/json/bible/versions/eng")
j = json.loads(input())

print("\n\n    versions = {")
for item in j["items"]:
    print('        "{0}": {1},'.format(item["local_abbreviation"], item["id"]))

print("    }")
