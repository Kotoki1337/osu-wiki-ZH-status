import requests
import json
import github

from config import ACCESS_TOKEN, PROXIES

g = github.Github(ACCESS_TOKEN)
repo = g.get_repo("ppy/osu-wiki")

def searchFile(page="1"):
    r = requests.get(
    f"https://api.github.com/search/code?q=+repo:ppy/osu-wiki+filename:zh.md&per_page=100&page={page}",
    proxies=PROXIES)

    return r.json()


def getPath(json, fileList):
    i = 0
    for items in json['items']:

        i += 1
        print(i)

        fileDict = {}

        zhPath = items['path']
        if "zh-tw.md" in zhPath or "zh-hk.md" in zhPath:
            continue
        commits = repo.get_commits(path=zhPath)
        fileDict["zh"] = {
            "path" : zhPath,
            "date" : commits[0].commit.committer.date.strftime('%Y/%m/%d %H:%M:%S'),
            "sha" : commits[0].commit.sha
        }

        enPath = items['path'].replace("zh.md","en.md")
        commits = repo.get_commits(path=enPath)
        fileDict["en"] = {
            "path" : enPath,
            "date" : commits[0].commit.committer.date.strftime('%Y/%m/%d %H:%M:%S'),
            "sha" : commits[0].commit.sha
        }

        fileList.append(fileDict)

    print(fileList)
    return fileList


if __name__ == "__main__":
    fileList = []
    initReturn = searchFile()
    fileList = getPath(initReturn, fileList)
    total_count = initReturn['total_count']
    count = total_count//100
    if total_count%100 != 0:
        count += 1
    for i in range(count):
        if i == 0:
            continue
        initReturn = searchFile(str(i+1))
        fileList = getPath(initReturn, fileList)

    with open('src/data/data.json', 'w') as outfile:
        json.dump(fileList, outfile)
