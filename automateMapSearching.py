#! python3
# automateMapSearching.py - Takes an address either from the command line or clipboard and opens it in the browser

import webbrowser, sys, pyperclip
# check if there is command line arguments
if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://maps.google.com/maps/place/' + address)