# hashtagsCoOccuranceNetworkGenerator.py     By: Samer Al-khateeb
# A script to extract Hashtag X Hashtag network   
#################################################################

"""
hashtagUsedToGetThisRow 
postID  
postContent 
postLanguage  
postBookmarked  
postCreatedAt 
postEditedAt  
postFavourited  
postFavouritedCount 
postReblogsCount  
postRepliesCount  
postSensitive 
postVisibility  
postURL 
postURI 
accountEmail  
accountBot  
accountCreatedAt  
accountDiscoverable 
accountDisplayName  
accountFollowersCount 
accountFollowingCount 
accountGroup  
accountID 
accountLocked 
accountStatusesCount  
accountURL  
accountUsername 
attachedPostUrlAuthorName 
attachedPostUrlAuthorURL  
attachedPostUrlProviderName 
attachedPostUrlProviderUrl  
attachedPostUrlProviderTitle  
attachedPostUrlProviderType 
OtherHashtagsIncludedInPost
"""

import csv
import ast

def main():
  #counter to keep track of the rows processed
  count = 0
  
  #creating a list to hold the output values so we can write it to CSV file
  CSV_output_list =[]

  #variable that hold the file name
  input_filename = 'TrendingHashtagsOutput-DateOfTheDay.csv'


  #open the input file and read it
  with open(input_filename, encoding='utf-8') as csv_input_file:
    CSV_file_as_list = csv.reader(csv_input_file)
    #Skipping the first row in the CSV file
    next(CSV_file_as_list)
    #process each row in the input file
    for row in CSV_file_as_list:
      count = count +1
      print()
      print("Processing row#", count)
      print()

      hashtagUsedToGetThisRow = row[0]
      # to treat the value in the csv cell as a list not as a string
      OtherHashtagsIncludedInPost = ast.literal_eval(row[34])

      for i in range(len(OtherHashtagsIncludedInPost)):
        otherhashtag = OtherHashtagsIncludedInPost[i][0]
        #create a row
        CSV_output_row = [hashtagUsedToGetThisRow, otherhashtag]
        #adding the row to the list of output
        CSV_output_list.append(CSV_output_row) 

  #creating a file to save the output
  with open('Hashtags-CoOccurance-Network.csv', 'w', encoding='utf-8') as csv_output_file:
    #creating a csv writer object 
    csvwriter = csv.writer(csv_output_file, delimiter=',')
    #write the columns headers
    csvwriter.writerow(["Source", "Target"])
    #writing/inserting the list to the output file 
    csvwriter.writerows(CSV_output_list)
    
main()


