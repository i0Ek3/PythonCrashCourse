## 
## hackernews_submissions.py
## @ianpasm(kno30826@gmail.com)
## 2018-04-05 11:54:52
## 
 
#!/usr/bin/env python3
# coding=utf-8

import requests

from operator import itemgetter

#excute API calling and store response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

#settle all article info
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    #excute API calling for every article
    url = ('https://hacker-news.firebaseio.com/v0/item' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
            'title': response_dict['title'],
            'link': 'http://news.ycominator.com/item?id=' + str(submission_id), 
            'comments': response_dict.get('descendants', 0)
            }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=Ture)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

