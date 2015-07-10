#An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase
#Function receives 2 strings as parameter
#Function creates 2 dictionary variables to store letters and their counts from each string
#If the dictionaries has the same keys and values, then the strings are anagram

def anagram(s1, s2):
    
    #Convert string to lower case and create a list from the string
    s1 = list( str(s1).lower() )
    s2 = list( str(s2).lower() )

    #Create empty dictionary to store each character and its count
    dict1 = {}
    dict2 = {}

    #Loop through each character in string1
    for z in s1:
        if z == ' ':
            pass #Ignore and not store the white blank space
        elif z not in dict1:
            dict1[z] = 1 #If character does not exist in dictionary, add character as a key and set value equal 1
        else:
            dict1[z] += 1 #If character exist in dictionary, increase the count by 1

    #Loop through each character in string2
    for z in s2:
        if z == ' ':
            pass #Ignore and not store the white blank space
        elif z not in dict2:
            dict2[z] = 1 #If character does not exist in dictionary, add character as a key and set value equal 1
        else:
            dict2[z] += 1 #If character exist in dictionary, increase the count by 1
            
    #Print dictionary to show each letter and its occurence in the strings
    print dict1
    print dict2
            

    #Use cmp function to compare the 2 dictionaries
    #cmp function return value 0 if dictionaries match, meaning it is an anagram
    if cmp(dict1, dict2) == 0:
        return 'Is an anagram'
    else:
        return 'Not an anagram'
    
     
x = 'hello  world'
y = 'oHeLL  dwlor'

a = 'rat'
b = 'brat'

#Calling the function and passing x and y as parameter
print anagram(x, y) #Will return confirmation that x and y are anagram

#Calling the function and passing a and b as parameter
print anagram(a, b) #Will return confirmation that a and b are not anagram
