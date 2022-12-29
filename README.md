<h1 align="center">Welcome to my server database project!</h1>


# About the project
The project was created on the principle of a database server.
It contains information about their login and password, the player's equipment and the data on the items appearing  the game.
In the future monsters and their kills will be added, which will change the structure of a given player.
This will expand the project with data related to the drop of items from a given monster, and enlarge the player's panel with its stats and levels.

The project was created to improve python skills.


# Function description

* 1 -> Display eq of players on the server
* 2 -> Display all items on the server
* 3 -> Display the number of players on the server'
* 4 -> Display Player Names on the server
* 5 -> Add items to the server
* 6 -> Edit player inventory from base
* 7 -> Add a new player account
* 8 -> Edit player password
* soon...

# Function description

* 1 ~
Allows you to display the inventory of players who are in the inventory dictionary. In addition, it allows you to display the players' inventory data from a json file.

* 2 ~
Allows you to display the items on the server with their quantity from the inventory dictionary.
And display items and their quantity from the json file.

* 3 ~

Allows you to display the number of all registered players who are in the players dictionary and the same functions from the text file responsible for storing player data.

* 4 ~
Allows you to display players in the numbering along with the name of their login from the players dictionary and from a text file that contains information storing account data.

* 5 ~
Allows you to add a new item to the server to the database that stores information about items in the perks file. The item must contain a name and an ID - 4 digits are required, otherwise the addition will fail. After successfully adding an item, a list of all items with their ID will be displayed.

* 6 ~
Allows you to edit the amount of items owned by the player. The inventory is in a json file. First, we enter the player's login, then we get a list of his current items with quantities, which causes exact editing.

* 7 ~
Allows you to add a new player account. Checks if the login is already in the database. If it does not this allow us to provide a password. The account is saved in the dictionary and in the text file that stores the account data.

* 8 ~
Allows you to change the password to the account of the player selected by us, which is in the file responsible for storing player data

<h1> Thank for your visit and have fun! </h1>