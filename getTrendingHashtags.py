# getTrendingHashtags.py                           By: Samer Al-khateeb
# script used to collect the top 20 daily trending hashtags on Mastodon
# Make sure Mastodon.py is correctly installed 


from mastodon import Mastodon
import json
import csv


def get_trending_hashtags(mastodon_instance):
	# trends method: Fetch the top 20 (the max you can get) 
    # trending-hashtag information, it returns a list of `hashtag dicts`, 
    # sorted by the instances trending algorithm, in descending order
	json_response = mastodon_instance.trends(limit = 20)
	return json_response


def write_output_to_CSV(biglist):
    # creating a file to save the output
    with open('TrendingHashtagsOutput.csv', 'w', newline='', encoding='utf-8') as csv_output_file:
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

		print(name, url, maxNumOfAccounts, maxNumOfUses, day)
		
		# creating a list of values (a row) 
		CSVOutputRow = [name, url, maxNumOfAccounts, maxNumOfUses, day]

		# adding the row to the output list
		CSVOutputListHashtags.append(CSVOutputRow)
	
	# write the CSVOutputList to the CSV file
	write_output_to_CSV(CSVOutputListHashtags)


def main():
	mastodonInstance = Mastodon(
	# create an app to get the access token code
    access_token = 'PlaceYourAccessTokenKeyHere!',
    api_base_url = 'https://mastodon.social'
	)

	# call the trending hashtag function
	response = get_trending_hashtags(mastodonInstance)

	# extract the data from the resposne returned
	process_response(response)

if __name__ == "__main__":
    main()