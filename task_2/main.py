from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
data = []
# Самый простой вариант
count = 1
for title in soup.find_all('span', class_='titleline'):
    data.append({
        'id':count,
        'title':title.find('a').text,
        'comments':0 })
    count += 1

count1 = 1
for comments in soup.find_all('span', class_='subline'):
    for com in comments.find_all('a'):
        if 'comment' in com.text:
            str = com.text
            num = int(str.split()[0])
            for i in data:
                if i['id' == ]
            count += 1
    


#for comments in soup.find_all('td', class_='subtext'):
    #for znach in comments.find_all('span', class_='subline'):
        #for link in znach.find_all('a'):
            #if link.text:  #Проверяем что текст есть
                
                #if 'comment' in link.text.lower():
                    
                    #print(f"Найдены комментарии: {link.text}")
                    
            #print(comments.find('a').text)
#print(data)
