# SteamGameTime

This program allows you to see the amount of time someone has spend on
their steam games. It will fail if the profile is private.

## To make this usable you need to have a Steam Developer API Key and a steam ID of a user you want to check out

You can get a steam API key from: https://steamcommunity.com/dev/apikey
Since this program is used locally you can enter 127.0.0.1 as domain.

You can get steamID from the profile on steam's website.
Example: https://steamcommunity.com/profiles/XXXXXXXXXXXXXXXX/home/.
If instead of some random numbers there's a normal nickname you'll have to use
some sort of converter, for example: https://steamidfinder.com/.

## Example of how the program looks

UI:

![UI](https://i.imgur.com/BGvzGM5.png "UI")

Output:

![Output](https://i.imgur.com/QuLyTsE.png "Output")

**Requires requests module for python:**
>pip install requests

**How to use:**
Proceed in the natural order of 1 to 4 in the main menu loop.
You only have to set up the API key once for every startup of the program,
so when scraping multiple profiles you ONLY need to provide the steam ID for every profile.
*Be sure to include the key.txt in the folder you want to run the file in*

The program will check if key.txt exists in the folder you call the program in.
This means that if you include key.txt in project's folder it's best to call the program from that folder if you're using the command line.
