# getDataByHashtags.py                                  By: Samer Al-khateeb
# script used to collect data based on searched hashtag (or list of hashtags)

# Make sure Mastodon.py installed correctly
# To install Mastodon.py follow these steps:
# Open terminal or cmd:
# Mac users type:
#    python3 -m pip install Mastodon.py -–user
# Windows users type:
#    py -m pip install Mastodon.py -–user


from mastodon import Mastodon
import json
import os
import csv
from datetime import datetime


def write_output_to_CSV(biglist):
    # column names
    columnNames = ["hashtagUsedToGetThisRow", "postID", "postLanguage", "postBookmarked", "postCreatedAt", "postEditedAt", "postFavourited", "postFavouritedCount", "postReblogsCount", "postRepliesCount", "postSensitive", "postVisibility", "postURL", "postURI", "accountEmail", "accountBot", "accountCreatedAt", "accountDiscoverable", "accountDisplayName", "accountFollowersCount", "accountFollowingCount", "accountGroup", "accountID", "accountLocked", "accountStatusesCount", "accountURL", "accountUsername", "attachedPostUrlAuthorName", "attachedPostUrlAuthorURL", "attachedPostUrlProviderName", "attachedPostUrlProviderUrl", "attachedPostUrlProviderTitle", "attachedPostUrlProviderType", "OtherHashtagsIncludedInPost"]
    
    # data rows of csv file
    rows = biglist

    # get the current date so we can 
	# append it to the CSV output file name
    now = datetime.now()
    dt_string = now.strftime("%m-%d-%Y")

    # name of csv file
    filename = "output{}.csv".format(dt_string)

    # opening the csv file in append mode
    with open(filename, 'a', encoding='utf-8') as csv_output_file:
        # define a variable to check if the file is empty (of size zero)
        fileIsEmpty = os.stat(filename).st_size == 0

        # creating a csv writer object
        csvwriter = csv.writer(csv_output_file)

        # if the file is empty (i.e., has size of 0) write the header or columnNames
        if fileIsEmpty:
            # writing the columnNames
            csvwriter.writerow(columnNames)

        # always write the data rows sent
        csvwriter.writerows(rows)


def search_mastodon(mastodonInstance, searchedHashTag):
	# timeline_hashtag method is used to "Fetch a timeline of 
	# toots with a given hashtag. The hashtag parameter should 
	# not contain the leading #" source: Mastodon.py
	jsonResponse = mastodonInstance.timeline_hashtag('{}'.format(searchedHashTag))
	
	# uncomment the line below if you want to see the response returned
	#print(json.dumps(jsonResponse, indent=4, sort_keys=True, default=str))

	# send the JSON Response to be processed and get it back as a list
	outputList = process_response(jsonResponse, searchedHashTag)

	# return the response as a list to the main() function
	return outputList


def process_response(jsonResponse, searchedHashTag):
	# need this so we know which hashtag is 
	# associated with the collected row
	hashtagUsedToGetThisRow = searchedHashTag

	# a list that will include all the info
	# extracted from the response
	CSVOutputList = []

	# variable to hold the length of the json response returned
	responseLength = len(jsonResponse)

	# for each item returned, let's extract it's info
	for responseItem in range(responseLength):
		# a local list used to collect other hashtags in the post
		localListForOtherPostHashtags = []

		postID = jsonResponse[responseItem]['id']
		postLanguage = jsonResponse[responseItem]['language']
		postBookmarked = jsonResponse[responseItem]['bookmarked']
		postCreatedAt = str(jsonResponse[responseItem]['created_at'])
		postEditedAt = str(jsonResponse[responseItem]['edited_at'])
		postFavourited = jsonResponse[responseItem]['favourited']
		postFavouritedCount = jsonResponse[responseItem]['favourites_count']
		postReblogsCount = jsonResponse[responseItem]['reblogs_count']
		postRepliesCount = jsonResponse[responseItem]['replies_count']
		postSensitive = jsonResponse[responseItem]['sensitive']
		postVisibility = jsonResponse[responseItem]['visibility']
		postURL = jsonResponse[responseItem]['url']
		postURI = jsonResponse[responseItem]['uri']
		accountEmail = jsonResponse[responseItem]['account']['acct']
		accountBot = jsonResponse[responseItem]['account']['bot']
		accountCreatedAt = str(jsonResponse[responseItem]['account']['created_at'])
		accountDiscoverable = jsonResponse[responseItem]['account']['discoverable']
		accountDisplayName = jsonResponse[responseItem]['account']['display_name']
		accountFollowersCount = jsonResponse[responseItem]['account']['followers_count']
		accountFollowingCount = jsonResponse[responseItem]['account']['following_count']
		accountGroup = jsonResponse[responseItem]['account']['group']
		accountID = jsonResponse[responseItem]['account']['id']
		accountLocked = jsonResponse[responseItem]['account']['locked']
		accountStatusesCount = jsonResponse[responseItem]['account']['statuses_count']
		accountURL = jsonResponse[responseItem]['account']['url']
		accountUsername = jsonResponse[responseItem]['account']['username']

		try:
			attachedPostUrlAuthorName = jsonResponse[responseItem]['card']['author_name']
		except TypeError as e:
			attachedPostUrlAuthorName = ''
		
		try:	
			attachedPostUrlAuthorURL = jsonResponse[responseItem]['card']['author_url']
		except TypeError as e:
			attachedPostUrlAuthorURL =''
		
		try:
			attachedPostUrlProviderName = jsonResponse[responseItem]['card']['provider_name']
		except TypeError as e:
			attachedPostUrlProviderName = ''
		
		try:
			attachedPostUrlProviderUrl = jsonResponse[responseItem]['card']['provider_url']
		except TypeError as e:
			attachedPostUrlProviderUrl = ''

		try:
			attachedPostUrlProviderTitle = jsonResponse[responseItem]['card']['title']
		except TypeError as e:
			attachedPostUrlProviderTitle = ''
		
		try:
			attachedPostUrlProviderType = jsonResponse[responseItem]['card']['type']
		except TypeError as e:
			attachedPostUrlProviderType = ''
		
		# creating a list of all the hashatgs mentioned in a post
		ListForOtherPostHashtags = jsonResponse[responseItem]['tags']
		for hashtag in range(len(ListForOtherPostHashtags)):
			hashtagName = ListForOtherPostHashtags[hashtag]['name']
			hashtagURL = ListForOtherPostHashtags[hashtag]['url']
			localListForOtherPostHashtags.append([hashtagName,hashtagURL])

		# creating a list of values (a row) 
		CSVOutputRow = [hashtagUsedToGetThisRow, postID, postLanguage, postBookmarked, postCreatedAt, postEditedAt, postFavourited, postFavouritedCount, postReblogsCount, postRepliesCount, postSensitive, postVisibility, postURL, postURI, accountEmail, accountBot, accountCreatedAt, accountDiscoverable, accountDisplayName, accountFollowersCount, accountFollowingCount, accountGroup, accountID, accountLocked, accountStatusesCount, accountURL, accountUsername, attachedPostUrlAuthorName, attachedPostUrlAuthorURL, attachedPostUrlProviderName, attachedPostUrlProviderUrl, attachedPostUrlProviderTitle, attachedPostUrlProviderType, localListForOtherPostHashtags]
		# adding the row to the output list
		CSVOutputList.append(CSVOutputRow)

	# return formatted list to the search_mastodon() function
	return CSVOutputList
	

def main():
	mastodonInstance = Mastodon(
	# create an app to get the access token code
    access_token = 'PasteYourAccessTokenKeyHere!',
    api_base_url = 'https://mastodon.social'
	)

	listOfKeywords = ['PasteYourHastagOneHereWithoutPoundSign', 'PasteYourHastagTwoHereWithoutPoundSign']
	
	# list to hold each reponse list we get from each hashtag
	listOfResponses = []

	for keyword in listOfKeywords:
		# call the search function to get the JSON resposne as formatted list
		responseAsList = search_mastodon(mastodonInstance, keyword)
		# return how many rows we obtained for each hashtag
		print(len(responseAsList))
		# write/append the list to the CSV file
		write_output_to_CSV(responseAsList)
		
if __name__ == "__main__":
    main()
