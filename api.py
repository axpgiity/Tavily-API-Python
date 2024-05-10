#!pip install tavily-python
title=input("Eneter your Query")

from tavily import TavilyClient  # type: ignore
user=TavilyClient(api="key")
response=user.search(str(title),include_images="true")
#optional: to view dictionary returned by the API 
print(response)
req=response

#to get images links
print(req['images'])

#to print the contents one by one
for i in range (len(req['results'])):
    cont=req['results'][i]['content']
    print(cont)


#!pip install openai

from openai import OpenAi # type: ignore
user=OpenAi(api_key="key")
#The function to Summarize data using GPT
responseGPT=user.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role":"system",
            "content":"Summarize it."
        },
        {
            "role":"user",
            "content":str(cont)
        }],
    temperature=0.7,
    max_tokens=150,
    top_p=1
    )
print(responseGPT)
#responseGPT is not a dictionary, thus we need object indexing to access data
ans=responseGPT.choices[0].message.content
print("THE SUMMARY:\n",ans)