# TODO: 1) sort the list so that you go from longest played games to the games
# you have spend less time on.
# 2) Somehow get access to prices someone has paid for these games.
# https://store.steampowered.com/app/{appID} works well.
# <div class="game_purchase_price price" data-price-final="719">£7.19</div>

import json # appid and playtime comes from json file from steam
import requests # used for web scrapping the data from steam's api website


# Important!
# Input your own key and steamID.
print("input your API key: ")
key = input()
print("input your steamID: ")
steamID = input()

# What is this magic link?
# It connects to steam api to get all owned games by the user with the specified
# steamID, along with their titles. Since we use steam's API, we needs a steam
# developer API key to connect to said services. I can't share mine in fear of
# some misusage, since I would be the one to blame.
# The other arguments specify: the format of the data (json for easy data read),
# To include app info(logo, icon and name) and the last one is for including
# free to play games.

websiteURL =  "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+key+"&steamid="+steamID+"&format=json&include_appinfo=1&include_played_free_games=1"

# This actually downloads the website so that python can process it.
response = requests.get(websiteURL)

# This simply parses/loads the json file into text so that python can see it as
# dictionaries and lists.
testing = json.loads(response.text)

# First we want to get what's inside the "response" part of the dictionary
x = testing.get("response")

# Get the amount of games with all the dlcs.
y = x.get("game_count")

# 'games' is a list, while x is a dictionary
games = x.get('games')

# convert the number of games into string.
print("You have "+ str(y)+ " games/applications.")

games_played = 0
total_time_played = 0

# sort the list by playtime, from highest to lowest.
newlist = sorted(games, key=lambda k: k["playtime_forever"], reverse=True)

# As long as there is something to get from the list of dictionaries.
for i in range(len(newlist)):
    # Only data in every iteration is appid and playtime forever
    # if you actually played the game at all
    if newlist[i].get('playtime_forever') > 0:
        games_played += 1
        print("You've spent " + str(round(float(newlist[i].get("playtime_forever") / 60), 3)) + "h playing "+ newlist[i].get("name") +".")
        total_time_played += newlist[i].get('playtime_forever')

print("You've played a total of "+ str(games_played) + " games, meaning you played only through about " + str(round((games_played / y) * 100)) + "% of your games.")
print("You have played a total of " + str(round((total_time_played / 60), 3) ) + " hours across all your games.")
