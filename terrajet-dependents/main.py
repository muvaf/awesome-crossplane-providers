import requests
from bs4 import BeautifulSoup

repo = "crossplane/terrajet"
url = 'https://github.com/{}/network/dependents'.format(repo)
nextExists = True
result = []
print("Getting the dependents of {}".format(repo))
while nextExists:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    result = result + [
        "{}/{}".format(
            t.find('a', {"data-repository-hovercards-enabled":""}).text,
            t.find('a', {"data-hovercard-type":"repository"}).text
        )
        for t in soup.findAll("div", {"class": "Box-row"})
    ]
    nextExists = False
    for u in soup.find("div", {"class":"paginate-container"}).findAll('a'):
        if u.text == "Next":
            nextExists = True
            url = u["href"]
path = "../providers.txt"
f = open(path, "w+")
for r in result:
    print(r)
    f.write(r + "\n")
f.close()
print("{} lines have been written to {}".format(len(result), path))

