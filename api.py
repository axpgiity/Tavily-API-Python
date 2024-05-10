pip install tavily-python
title=input("Eneter your Query")

from tavily import TavilyClient 
user=TavilyClient(api="key")
response=user.search(str(title),include_images="true")
#optional: to view dictionary returned by the API 
print(response)
req=response

#to get images links
print(req['images'])

#to print the contents one by one
for i in range (len(re['results'])):
    print(req['results'][i]['content'])