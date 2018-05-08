from requests import get
from bs4 import BeautifulSoup
import csv
names = []
authors = []
prices = []
ratings = []
avg_ratings = []
urls = []
final = []
ans = []
for i in range(1,6,1):
     url = 'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_i?_encoding=UTF8&pg='+str(i)
     response = get(url)
     best = BeautifulSoup(response.text,'html.parser')
     bestsellers = best.find_all('div',class_ = 'zg_itemImmersion')

     for book in bestsellers:
          name1 = book.find('div', class_ = 'p13n-sc-truncate p13n-sc-line-clamp-1')
          if name1 is not None:
          	names = name1.text.strip()
          else:
     	    	names = "Not Available" 
          name2 = book.find('a',class_ = 'a-size-small a-link-child')
          if name2 is not None:
     	    	authors = name2.text
          else:
     	    	authors = "Not Available"     
          name3 = book.find('span',class_ = 'p13n-sc-price')
          if name3 is not None:
     	    	prices = name3.text
          else:             
     	    	prices = "Not Available"
          name4 = book.i
          if name4 is not None:
     	  	  ratings = name4.text.strip()
          else: 
     	    	ratings = "Not Available"
          name5 = book.find('a',class_ = 'a-size-small a-link-normal')
          if name5 is not None:             
     	    	avg_ratings = name5.text  
          else:
     	    	avg_ratings = "Not Available"
          name6 = book.find('a',class_ = 'a-link-normal')['href']
          if name6 is not None:
     	    	urls = name6
          else: 
     	    	urls = "Not Available"
          ans = [names,urls,authors,prices,ratings,avg_ratings]
          final.append(ans)

ofile = open('com_book.csv','w')
writer = csv.writer(ofile,delimiter = ';')
writer.writerow(["Names","URL","Author","Price","Number of Ratings","Average Rating"])
for row in final:
    writer.writerow((row))          



