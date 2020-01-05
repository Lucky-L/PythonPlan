import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/300/600')

cat_img = response.read()

with open('cat_300_600.jpg','wb') as f:
    f.write(cat_img)