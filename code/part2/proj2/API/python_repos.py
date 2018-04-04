## 
## python_repos.py
## @ianpasm(kno30826@gmail.com)
## 2018-04-04 14:45:35
## 
 
#!/usr/bin/env python3
# coding=utf-8

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
r = requests.get(url)
print("Status code:", r.status_code) ##200 shows successed

response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

#search something about repo
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

#study first repo
repo_dict = repo_dicts[0]

print("\nSelected information about first repostitory:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])
#print("\nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)




