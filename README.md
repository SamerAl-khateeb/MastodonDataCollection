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

## Reference/Citation 

If you use any of the scripts provided or a modified version of them in your research, please cite the following article:

Al-khateeb, Samer. (2022). Dapping into the Fediverse: Analyzing What’s Trending on Mastodon Social. In: Thomson, R., Dancy, C., Pyke, A. (eds) Social, Cultural, and Behavioral Modeling. SBP-BRiMS 2022. Lecture Notes in Computer Science, vol 13558. Springer, Cham. https://doi.org/10.1007/978-3-031-17114-7_10
