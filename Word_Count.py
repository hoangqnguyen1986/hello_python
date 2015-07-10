#Function receives string as parameter
#Function creates dictionary to store words and their counts from the string

def wordCount(s1):
    
    #Convert string to lower case
    #Create a list using the split method; the parameter is the white blank space
    s1 = str(s1).lower()
    s1 = s1.replace(',' , '').replace('.' , '').replace('?' , ''). replace(';' , '').replace('!' , '').replace(':' , '')
    s1 = s1.replace('\xe2\x80\x99' , '\'') #Replace special character apostrophe
    s1 = s1.replace('\n', ' ')
    s1 = s1.split(' ')
    
    
    #Create empty dictionary to store each word and its count
    dict1 = {}

    #Loop through each word in string1
    for z in s1:
        if z == '':
            pass #Ignore and not store the white blank space
        elif z not in dict1:
            dict1[z] = 1 #If word does not exist in dictionary, add word as a key and set value equal 1
        else:
            dict1[z] += 1 #If word exist in dictionary, increase count by 1
    
    #Print a sorted dictionary to show each word and its occurence in the strings to calling method
    for z in sorted(dict1.keys()):
        print z + ': ' + str(dict1[z])
     
    print '\n'

    
    
#Read from string and do word count    
x = 'The Blue Bottle Coffee empire now extends to the heart of San Francisco’s Financial District, as James Freeman and co. opened their latest cafe on the corner of Sansome and Bush last week.'
wordCount(x)


#Read from a file and do word count
file = open('word_count_text_sample.txt','r')
z = file.read()
wordCount(z) 
file.close()
