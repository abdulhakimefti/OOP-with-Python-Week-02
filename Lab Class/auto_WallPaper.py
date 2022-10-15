import requests
import json
import PyWallpaper


api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
response = requests.get(api_url)
# print(list(response))

content = response.content.decode('UTF-8')
# print((content))

dict_content = json.loads(content)
print(dict_content)
image_url = dict_content['url']
# print(image_url)

res = requests.get(image_url)
# print(list(res))
with open ('apod.png','wb') as image :
    image.write(res.content)

PyWallpaper.change_wallpaper('/home/efti/Desktop/New Folder/C/OPP with Python/Week 02/Lab Class/apod.png')