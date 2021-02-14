import requests
from termcolor import colored, cprint
from bs4 import BeautifulSoup
import pandas as pd


header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }
URL= "https://old.reddit.com/user/Gingaboo"
page = requests.get(URL, headers = header)
print(page.status_code)
soup = BeautifulSoup(page.content,'html.parser')
userCatalouge = soup.find(id="siteTable")

userTitle = [uT.get_text() for uT in userCatalouge.find_all('a',{'class':'title'})]
userDate = [uD['title'] for uD in userCatalouge.select('.tagline time[title]')]
userSub =[uS['data-subreddit-prefixed'] for uS in userCatalouge.find_all('div', {'class':'thing'})]
userPoints =[uP['title'] for uP in userCatalouge.find_all(class_="score unvoted")]

print(userTitle)
print(userDate)
print(userSub)
print(userPoints)

a ={

"User Title": userTitle,
"User Date": userDate,
"User Subreddit": userSub,
"User Points": userPoints
}

RedditorInfo = pd.DataFrame.from_dict(a, orient ='index')
RedditorInfo = RedditorInfo.transpose()
RedditorInfo.to_csv(r'C:\Users\elayb\Desktop\Coding Projects\Python\RedditorInfo.csv', index=True, header = True)

print(RedditorInfo.describe())
print("-----------------------------")
print(RedditorInfo.shape)
print("-----------------------------")
print(RedditorInfo.dtypes)


userComment = [uCom.get_text() for uCom in userCatalouge.select('.md p')]

b ={

"LIST OF WORDS IN SENTENCE STRUCTURE": userComment + userTitle,
}
WordBubble = pd.DataFrame.from_dict(b, orient = 'index')
WordBubble = WordBubble.transpose()
WordBubble.to_csv(r'C:\Users\elayb\Desktop\Coding Projects\Python\RedditWordBubble.csv', index=True, header = True)

print(WordBubble.shape)
