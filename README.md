# MastodonDataCollection

## getTrendingHashtags.py           
This script can be used to collect the top 20 daily trending hashtags on Mastodon.

Make sure Mastodon.py is correctly installed 

You need to create an account with Mastodon and obtain an **access_token** key. 

Need to Paste the key to the code so it can work

Need to run this code everyday if you want to get trending hashtags everyday.

### Input and Output
No input, the output will be a CSV file called **TrendingHashtagsOutput-DateOfTheDay.csv** containing the top 20 daily trending hashtags on Mastodon.


## getDataByHashtags.py
This script is used to collect data based on searched hashtag (or list of hashtags)

### Input and Output
Input: a hashtag or a list of hashtags

Output: the output will be a CSV file called **TrendingHashtagsOutput-DateOfTheDay.csv** containing info collected about each hashtag
