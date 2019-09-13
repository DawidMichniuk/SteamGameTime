# TODO: 1) Somehow get access to prices someone has paid for these games.
# https://store.steampowered.com/app/{appID} works well.
# <div class="game_purchase_price price" data-price-final="719">£7.19</div>

import json
import requests
import sys
import steamfunc
# Global variables
# key,steamID = ""

print("Hello!")
def menu():
    """
    This menu serves as the main hub of the program.
    Users will use it to enter/locate their API keys and give steam IDs
    of the accounts they want to scrape data from.
    Use stars to make it look 'pretty'.
    """
    while True:
        print("**********************")
        print("1. Locate the API key")
        print("2. Give Steam ID.")
        print("3. Get the data.")
        print("4. Parse the data.")
        print("5. Exit the Program")
        print("**********************")
        users_choice = int(input())

        # Work in progress.
        if users_choice == 1:
            steamfunc.locate_the_api_key()
        elif users_choice == 2:
            steamfunc.get_steam_id()
        elif users_choice == 3:
            steamfunc.get_data_from_steam()
        elif users_choice == 4:
            steamfunc.parse_data()
        elif users_choice == 5:
            sys.exit()
        else:
            print("The number given does not match with the numbers from the list.")
# Makes it so the menu runs at startup!
if __name__ == "__main__":
    menu()