import requests

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
header = {"Accept":"application/vnd.github.v3+json"}
r = requests.get(url,headers=header)
print(f"Status code: {r.status_code}")

# 变量接收API响应
response_dict = r.json()
# print(response_dict.keys())

# 查看GitHub共包含多少和Python仓库
print(f"Total repositories: {response_dict['total_count']}")

# ‘items’的值是一个列表，其中包含很多个字典，每个字典都包含一个python仓库的信息
repo_dicts = response_dict['items']
print(f"Reponsitories returned: {len(repo_dicts)}")

# 查看第一个仓库
repo_dict = repo_dicts[0]
print(f"\nKeys:{len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)