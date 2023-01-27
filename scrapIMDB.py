from bs4 import BeautifulSoup
import requests,openpyxl

excel=openpyxl.workbook()
print(excel.sheetnames)

sheet=excel.active
sheet.title='Top Rated Movies'
print(excel.sheetnames)

sheet.append(['Movie Rank','Movie Name','Year of Release','IMDB Rating'])

try:
    source=requests.get('https://www.imdb.com/chart/top')
    source.raise_for_status()

    soup=BeautifulSoup(source.text,'html.parser')

    movies=soup.find('tbody', class_="lister-list").find_all('tr')
    print(len(movies))

    for movie in movies:

        name=movie.find('td', class_="titleColumn").a.text

        rank=movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]


        year=movie.find('td', class_="titleColumn").span.text.strip('()')

        rating=movie.find('td', class_="ratingColumn imdbRating").strong.text

        print(rating)
        
        print(year, rank, name,movie)
        
        print(rank)
         
        print(name)
        
        print(movie)
        break 
     
    print(movies)

    print(soup)

    sheet.append([rank,name,year,rating])

except Exception as e:
    print(e)
  
excel.save('IMDB Movie Ratings.xlsx')
