import re
import json




with open("C:\\Users\\jusef\\Downloads\\json-test.txt") as json_file:
     data = json.load(json_file)
     json_file.close
 
     srcterm = input('What genre should be searched for: ').capitalize()

     c = 0

     for x in data['mangas']:
         if srcterm in x['genres']:
            c = c + 1
            print(x['rating'],x['name'] ,x['genres'])

     if c == 0:
        print('No results found for "'+srcterm+'"')
     else:
        print('Found',c,'results for "'+srcterm+'"')
 