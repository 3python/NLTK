# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:54:18 2018

@author: kate
"""
#This code analyses the text 'The Wasteland' by T.S. Elliot.
#I have not attached a license to this code because it contains someone else's work who has not attached 
#a license to thier work and I do not feel comftable licensing that.

#Before starting download the nltk software.
#nltk.download() 		

#Imports the language analysis software.
import nltk
#Allows requests from web servers.
import requests
#Allows time to be put between running lines of code.
import time


#Read in the file.
raw = open('wasteland.txt', 'rU').read()


#Read in text from a website.
#url = "http://www.gutenberg.org/files/1321/1321-0.txt"
#raw = requests.get(url).text

#Reduce the contents of the text to just the wasteland poem.
#Find the line before the start of the peom.
start = "Produced by An Anonymous Project Gutenberg Volunteer"
start_pos = raw.find(start) + len(start)
#Find the line at the end of the poem. 
end_pos = raw.rfind("Line 416 aetherial] aethereal")

#Extract everything after the start and before the end of the poem.
raw = raw[start_pos:end_pos]
#Check that this has worked.
print(raw)


#Tokenise the raw text.
tokens = nltk.word_tokenize(raw)
#Convert to nltk text object.
text = nltk.Text(tokens)

#Find the 20 most common words.
fdist1 = nltk.FreqDist(text)
print("Most common words:")
print(fdist1.most_common(20))

#Print the 20 most common word lengths.
fdist2 =  nltk.FreqDist(len(w) for w in text)
print("The most common word lengths.")
print(fdist2.most_common(20))

#Print all the words that have more than 10 letters.
long_words = [w for w in text if len(w) > 10]
print(long_words)

#Speech tagging.
tagged = nltk.pos_tag(text)
#Check that this has worked.
print(tagged)


#Make a list of the proper nouns.
#modified (by one word) from https://stackoverflow.com/questions/17669952/finding-proper-nouns-using-nltk-wordnet
proper_nouns = [word for word,pos in tagged if pos == 'NNP']
print(proper_nouns)

#Proper nouns should begin with a capital, make a list of all the proper nouns that start with a capital.
#Only include words that are just composed of letters.
#Set up a blank list.

#List to store filtered proper_nouns list.
tidy = []
#Run through all the words in proper_nouns list.
for i in proper_nouns:
    #Get the first letter from each word.
    test = i[0]
    #Check that the first letter is a capital and does not contain punctuation.
    if test.isupper() == True and i.isalpha() == True:
        #If it is, add it to the list called 'tidy'.
        tidy.append(i)
    
#Check that the new list containing only proper nouns that begin with a capital has worked.
print("tidy test")     
print(tidy)


#Finding the loations of text on the map.

#Modified from https://gist.github.com/pnavarrc/5379521 github.
# Using Python requests and the Google Maps Geocoding API.
#
# References:
#
# * http://docs.python-requests.org/en/latest/
# * https://developers.google.com/maps/

#Set the website that addresses will be extracted from.
GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

print("geodata test")
print (tidy[260:270])

#Get addresses for a subsection of the list.
for i in tidy[260:270]:  
    time.sleep(.2)
    params = {
            'address': i
            }
        
    # Request the addresses in a json format.
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()
    
    #Do this if a valid address is found.
    if res['results']:
        # Only use the first address result that google provides.
        result = res['results'][0]
        
        #Obtain the coordinates and name of the address.
        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']
        
        #Print the address name and coordinates.
        print("For word", i, "the location is:")
        print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
    
    #Inform the user if the address can not be found.   
    else:
        print("For word", i, "an address has not been found.")


#End of the code that has been modified from #Modified from https://gist.github.com/pnavarrc/5379521 github.





