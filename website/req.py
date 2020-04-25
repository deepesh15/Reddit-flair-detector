import requests
url ='https://flair-classifier.herokuapp.com/automated_testing'

files = {'upload_file': open('file.txt','r')}
r = requests.post(url, files=files)
print(r.content)
