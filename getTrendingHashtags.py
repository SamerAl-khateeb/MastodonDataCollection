# getTrendingHashtags.py            By: Samer Al-khateeb
# script used to collect the top 20 daily hashtags on Mastodon

# Make sure Mastodon.py installed correctly
# To install Mastodon.py follow these steps:
# Open terminal or cmd:
# Mac users type:
#    python3 -m pip install Mastodon.py -–user
# Windows users type:
#    py -m pip install Mastodon.py -–user


from mastodon import Mastodon
import json
import csv
from datetime import datetime


def get_trending_hashtags(mastodon_instance):
	# trends method: Fetch the top 20 (the max you can get) 
    # trending-hashtag information, it returns a list of `hashtag dicts`, 
    # sorted by the instances trending algorithm, in descending order
	json_response = mastodon_instance.trends(limit = 20)
	# uncomment the line of code below if you want to see the reponse on screen
	#print(json.dumps(response, indent=4, sort_keys=True, default=str))
	return json_response


def write_output_to_CSV(biglist):
	# get the current date so we can 
	# append it to the CSV output file name
    now = datetime.now()
    dt_string = now.strftime("%m-%d-%Y")
	# name of csv file
    filename = "TrendingHashtagsOutput{}.csv".format(dt_string)

    # creating a file to save the output
    with open(filename, 'w', newline='', encoding='utf-8') as csv_output_file:
        #creating a csv writer object 
        csvwriter = csv.writer(csv_output_file, delimiter=',', lineterminator='\n')
        #write the columns headers
        csvwriter.writerow(["Hashtag", "HashtagURL", "maxNumOfAccounts", "maxNumOfUses", "DateOfMaxTrending"])
        csvwriter.writerows(biglist)
    # close the output file
    csv_output_file.close()


def process_response(response):

	# list that will include info about the hashtags
	# treding extracted from the response
	CSVOutputListHashtags = []
	
	# for each item in the response, lets extract info from it
	for result in range(len(response)):
		history = response[result]['history']
		name = response[result]['name']
		url = response[result]['url']

		maxNumOfAccounts = history[0]['accounts']
		day = history[0]['day']
		maxNumOfUses = history[0]['uses']

		print("'"+name+"'", end=',')
		# creating a list of values (a row) 
		CSVOutputRow = [name, url, maxNumOfAccounts, maxNumOfUses, day]

		# adding the row to the output list
		CSVOutputListHashtags.append(CSVOutputRow)
	
	# write the CSVOutputList to the CSV file
	write_output_to_CSV(CSVOutputListHashtags)


def main():
	mastodonInstance = Mastodon(
	# create an app to get the access token code
    access_token = 'PasteYourAccessTokenKeyHere!',
    api_base_url = 'https://mastodon.social'
	)

	# call the trending hashtag function
	response = get_trending_hashtags(mastodonInstance)

	# extract the data from the resposne returned
	process_response(response)

	
if __name__ == "__main__":
    main()