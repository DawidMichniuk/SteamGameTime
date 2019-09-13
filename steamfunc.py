import json
import requests
import sys

def locate_the_api_key():
    global key
    print("Have you already put the API key in the key.txt file? Y/N")
    answer = input()
    key_from_file = ""
    if answer == 'Y':
        # the '+' creates the file if it doesnt exists.
        keyFile = open("key.txt", "r+")
        key_from_file = keyFile.read()
        if key_from_file == "":
            print("The fact that there's nothing in the file says otherwise")
        else:
            key = key_from_file
            print("Key found.")
    if answer == 'N':
        key = input("input your API key: ")

        keyFile = open("key.txt", "w+")
        key_from_file = keyFile.write(key)
    keyFile.close()

def get_steam_id():
    global steamID
    print("Now you have to give the program the steam id of the account.")
    steamID = input("input the steamID: ")
    # Don't create the file for this steam id just yet


def get_data_from_steam():
    global mainJsonFile, fileWithData
    if key == "":
        print("Did you set up the API key?")
    if steamID == "":
        print("I need the steam ID of the account you want to find.")
    try:
        # Create the file to save the data to.
        fileWithData = open((str(steamID) + ".txt"), "w+" )
        websiteURL =  "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+key+"&steamid="+steamID+"&format=json&include_appinfo=1&include_played_free_games=1"
        # This actually downloads the website so that python can process it.
        response = requests.get(websiteURL)

        # This simply parses/loads the json file into text so that python can see it as
        # dictionaries and lists.
        mainJsonFile = json.loads(response.text)

        print("Data scrapped from Steam's API successfully!")
    except json.decoder.JSONDecodeError:
        print("There was a problem with what you entered.")
        print("Either check for a typo in API Key/Steam ID")
        print("or double check that the profile exists!")

def parse_data():
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
    except TypeError:
        print("Profile is either private or has no games")

    fileWithData.close()
