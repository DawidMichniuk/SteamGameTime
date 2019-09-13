# TODO: 1) Somehow get access to prices someone has paid for these games.
# https://store.steampowered.com/app/{appID} works well.
# <div class="game_purchase_price price" data-price-final="719">£7.19</div>
# 2) Put everything into different classes, create a main function and some sort of menu
# so that you can check out multiple accounts instead of restarting the program every time

import json # appid and playtime comes from json file from steam
import requests # used for web scrapping the data from steam's api website


print("SteamGameTime counts how many hours have you spent on games in total across your steam library")
print("In future versions it will also count the money per hour value of each game.")

key_was_received = False

try:
    # Setting up (opening) a file to read the API key from.
    keyFile = open("key.txt", "r")
    keyFromFile = keyFile.read()
    if keyFromFile == "":
        print("input your API key: ")
        key = input()
    else:
        key = keyFromFile
    key_was_received = True
# If there is no key.txt file then just ask for the API key.
except FileNotFoundError:
    print("For future use, you can simply create a file called 'key.txt' with your key inside it.")
    key = input("input your API key: ")


continueTheLoop = ""
while continueTheLoop == "":
    try:
        steamID = input("input your steamID: ")
        fileWithData = open((str(steamID) + ".txt"), "w+" )
        websiteURL =  "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+key+"&steamid="+steamID+"&format=json&include_appinfo=1&include_played_free_games=1"
        # This actually downloads the website so that python can process it.
        response = requests.get(websiteURL)

        # This simply parses/loads the json file into text so that python can see it as
        # dictionaries and lists.
        mainJsonFile = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        print("You didn't enter anything for the steam id or api key OR there was a problem with what you entered.")
        # break the loop, close the files and then finish the program (instead of simply exiting the program).
        break

    # Get the total amount of games.
    games_owned = (mainJsonFile.get("response")).get("game_count")

    gamesList = (mainJsonFile.get("response")).get('games')

    # convert the number of games into string.
    print("You have "+ str(games_owned)+ " games/applications.")
    fileWithData.write("You have "+ str(games_owned)+ " games/applications.\n")
    games_played = 0
    total_time_played = 0
    try:
        # sort the list by playtime, from highest to lowest.
        newlist = sorted(gamesList, key=lambda k: k["playtime_forever"], reverse=True)

        # The list of games you haven't played.
        list = []
        for i in range(len(newlist)):
            # if you actually played the game at all
            if newlist[i].get('playtime_forever') > 0:
                games_played += 1
                fileWithData.write("You've spent " + str(round(float(newlist[i].get("playtime_forever") / 60), 3)) + "h playing "+ newlist[i].get("name") +".\n")
                total_time_played += newlist[i].get('playtime_forever')
            else:
                list.append(newlist[i].get("name"))


        print("Done! Check out the results in " + str(steamID) + ".txt")
        fileWithData.write("Games you own that you haven't played at all:\n")
        # Loop through everything but the last one so that i can format it nicely.
        for i in range(len(list) - 1):
            fileWithData.write(list[i] + ", ")
        fileWithData.write(list[len(list) - 1] + ".\n")
        fileWithData.write("You've played a total of "+ str(games_played) + " games, meaning you played only through about " + str(round((games_played / games_owned) * 100)) + "% of your games.\n")
        fileWithData.write("You have played a total of " + str(round((total_time_played / 60), 3) ) + " hours across all your games.\n")

        print("If you want to check out another profile, simply press enter")
        print("If not, write anything else, this will close the program")
        continueTheLoop = input()

    except TypeError:
        print("Profile is either private or has no games")
fileWithData.close()
if key_was_received:
    keyFile.close()
