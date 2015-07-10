#Scrape San Francisco restaurant data from OpenTable website

import urllib2, time
from bs4 import BeautifulSoup

#Create output file with column headers
output = open('OpenTable_Restaurant_Data.csv', 'w')
column_header = 'Restaurant_Name|Rating|Number_of_Review|Restaurant_Type|SF_Neighborhood\n'
output.write(column_header)

#Create variable condition for looping through web pages
more_page = True

#Create variable for url string. Variable will increment by 100 with each loop
i = 0

#Looping through web page while more_page is True
while more_page:
    url = 'http://www.opentable.com/san-francisco-bay-area-restaurant-listings?metroid=4&regionids=5&sort=Name&size=100&excludefields=description&from=' + str(i)
    
    #Open url and get data
    page = urllib2.urlopen(url)
    page_text = page.read()
    soup = BeautifulSoup(page_text)
    data = soup.find_all('div', {'class':'rest-row-info'})
    
    #If there is data on open page, extract data
    if len(data) != 0:
        
        for r in data:
            #Get name of restaurant
            try:
                name = r.contents[1].text
                
                #Comment: Encode is needed because of special character in name
                output.write(name.encode('utf8') + '|')
            except:
                #print 'No Restaurant Name'
                output.write('ERROR|')
        
            #Get rating for restaurant
            try:
                rating = r.contents[3].find_all('div', {'class':'star-cont'})[0].find_all('div')[1]
                rating = str(rating).strip('<div class=').strip('></div').replace('stars cnt-', '').replace('-', '.').encode('string-escape').replace('"', '')
                output.write(rating + '|')
            except:
                output.write('|')
    
            #Get number of reviews for restaurant
            try:
                reviewNum = r.contents[3].find('span').string.replace('(', '').strip(')')
                output.write(reviewNum + '|')
            except:
                output.write('|')
        
            #Get restaurant type and neighborhood restaurant is located in 
            try:
                c = r.contents[7].text.strip().split('|')
        
                r_type = c[0].strip()
                output.write(r_type + '|')
        
                neighborhood = c[1].split(',')
                neighborhood = neighborhood[0].strip()
                output.write(neighborhood)
            except:
                output.write('|')
    
            #Move to next line in print
            output.write('\n')
        
        #Increase variable i by 100
        i += 100
        
    
    #If there is no data on open page, set more_page to False
    else:
        more_page = False
    
    #Sleep for 5 seconds
    time.sleep(5)
    
#Closing output file
output.close()
print "Script Completed!!!"
