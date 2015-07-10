#Amazon is rejecting the default User-Agent for urllib2 . One workaround is to use the Mechanize 
import mechanize, time
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0')]

#Create output file with column headers
output = open('Amazon_New_Book_Releases.csv', 'w')
column_header = 'Book_Name|Author|Release_Date|Rating|Number_of_Review\n'
output.write(column_header)

#Create variable condition for looping through web pages
more_page = True

#Create variable for url string. Variable will increment by 1 with each loop
i = 1

while more_page:
    url = 'http://www.amazon.com/s/ref=sr_pg_' + str(i) + '?fst=as%3Aoff&rh=n%3A283155%2Cp_n_publication_date%3A1250227011&page=' + str(i)

    #Open url and get data
    page = br.open(url)
    page_content = page.read()
    soup = BeautifulSoup(page_content)
    data = soup.find_all('div', {'class':'a-fixed-left-grid-col a-col-right'})
    
    #Check to see if last page. If not last page, get data and write to output file
    if len(data) != 0:
        
        for r in data:
            #Get name of book
            name = r.contents[0].find_all('a')[0].text.strip()
            output.write(name.encode('utf8') + '|')
            
            #Get author of book
            try:
                author = r.contents[0].find_all('div', {'class':'a-row a-spacing-none'})[0].text.strip('by ')
                output.write(author.encode('utf8') + '|')
            except:
                output.write('|')
             
            #Get date book was released
            try:
                releaseDT = r.contents[0].find_all('span')[2].text
                output.write(releaseDT + '|')
            except:
                output.write('|')
             
            #Get rating for book
            try:
                rating = r.contents[1].find_all('span', {'class':'a-icon-alt'})[0].text.split(' out of ')
                rating = rating[0]
                output.write(rating + '|')
            except:
                output.write('|')
             
            #Get number of reviews for book
            try:
                reviewNum = r.contents[1].find_all('div', {'class':'a-row a-spacing-mini'})[0].find_all('a')[1].text
                output.write(reviewNum)
            except:
                pass
            
            
            output.write('\n')
        
        #Increment variable i by 1
        i += 1
        
        #Sleep for 3 seconds
        time.sleep(3)
        
    #Check to see if last page. If last page, exit while loop
    else:
        more_page = False

#Closing output file
output.close()
print 'Script Completed!!!'
