import json # appid and playtime comes from json file from steam
import requests # used for web scrapping the data from steam's api website

key = 
steamID =

# What is this magic link?
# It connects to steam api to get all the owned games, along with their titles
# and names of a user with specified steamID and needs a steam developer as key.
# In the public version I will delete mine since it's best if I don't share it.
# The other arguments specify: the format of the data (json for easy data read)
# To include app info(logo, icon and name) and free to play games respectively.

websiteURL =  "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+key+"&steamid="+steamID+"&format=json&include_appinfo=1&include_played_free_games=1"

response = requests.get(websiteURL)

# Change that later on so users can add their API key and account id
# The original link: response = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=C1E13D40571114336AAF4E64A1473BB9&steamid=76561198064555348&format=json")
testing = json.loads(response.text)

# First we want to get what's inside the "response" part of the dictionary
x = testing.get("response")

# Get the amount of games with all the dlcs.
y = x.get("game_count")

# For now we don't care about the amount of games, only games
# (I believe it includes the dlcs since it found over 20 more games than I actually have)
# 'games' is a list, while x is a dictionary
games = x.get('games')
type(games)
print("You have about: "+ str(y)+ " games (that should include all the dlcs)")

# This will serve to count how many games you have actually played.
count = 0
# As long as there is an appid to get do the loop
for i in range(len(games)):
    # Only data in every iteration is appid and playtime forever
    # if you actually played the game at all
    if games[i].get('playtime_forever') > 0:
        count = count + 1
        print("You've spent " + str(round(float(games[i].get("playtime_forever") / 60), 3)) + "h playing: "+ str(games[i].get("name")))


print("You've played a total of: "+ str(count) + " games, meaning you played only through about: " + str(round((count / y) * 100)) + " % of your games.")
