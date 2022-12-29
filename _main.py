import sys, json
##########################DATA Server###########################################

inventory = {
    'player1': {'arrow': 10, 'dagger': 1, 'rope': 1, 'torch': 1, 'gold': 500},
    'player2': {'arrow': 12, 'dagger': 0, 'rope': 3, 'torch': 1, 'gold': 10},
    'player3': {'arrow': 5, 'dagger': 5, 'rope': 0, 'torch': 2, 'gold': 5400},
}

perks = {
    'arrow': 1000,
    'dagger': 1001,
    'rope': 1002,
    'torch': 1003,
    'gold': 1004,
}

players = {
    'player1': 'password1',
    'player2': 'password2',
    'player3': 'password3',
}

##########################MAIN CODE######################################

print('\nSelect mode\n')
print('1 -> Players')
print('2 -> Mobs')
print('3 -> Killings')

question = input('\nSelect options: ')
if question == '1':
    question = 'Players'
elif question == '2':
    question = 'Mobs'
elif question == '3':
    question = 'Killings'

print(f"\nYou have selected sections {question}..")
quest = input(f'\nYou are sure of your choice {question}?.. Re-enter Selected option number: ')

if quest == '1':
    print('\n################################################################################')
    print('\nWhat you want to do? \n')
    print('1 -> Display eq of players on the server')
    print('2 -> Display all items on the server')
    print('3 -> Display the number of players on the server')
    print('4 -> Display Player Names on the server')
    print('5 -> Add items to the server')
    print('6 -> Edit player inventory from base')
    print('7 -> Add a new player account')
    print('8 -> Edit player password')


    question1 = input('\nSelect options: ')
    print(f'\nYou have selected item number: {question1}, re-enter selected option number')
    question2 = input('\nConfirm: ')
    print() 

    if question1 == question2:
        if question1 == '1':
            for n, i in inventory.items():
                print('For %s -> %s' %(n, i))
            print('\n################################################################################\n')
            print('You can also display the EQ of all players from database: 1 - Display / 2 - To exit')
            inventorybase = input('\nSelect options: ')
            print(f'\nYou have selected item number: {inventorybase}, re-enter selected option number')
            inventorybase2 = input('\nConfirm: ')
            print()
            if inventorybase == inventorybase2:
                if inventorybase == '1':
                    with open('inventory.json', 'r') as f:
                        inventory = json.load(f)
                        for player, data in inventory.items():
                            print(f'Player: {player}')
                            print('Items:')
                            for item, quantity in data['items'].items():
                                print(f'{item}: {quantity}')
                            print()
                        

        elif question1 == '2':
            def displayinventory(players, item):
                total = 0
                for p,i in players.items():
                    total += i.get(item, 0)
                return total
            print('The number of items in the list on the whole server \n')
            print(' -   Arrow       ->      ' + str(displayinventory(inventory, 'arrow')))
            print(' -   Dagger      ->      ' + str(displayinventory(inventory, 'dagger')))
            print(' -   Rope        ->      ' + str(displayinventory(inventory, 'rope')))
            print(' -   Torch       ->      ' + str(displayinventory(inventory, 'torch')))
            print(' -   Gold        ->      ' + str(displayinventory(inventory, 'gold')))
            print('\n################################################################\n')
            print('You can also display item from database: 1 - Display / 2 - To exit')
            eqbase = input('\nSelect options: ')
            print(f'\nYou have selected item number: {eqbase}, re-enter selected option number')
            eqbase2 = input('\nConfirm: ')
            print()
            if eqbase == eqbase2:
                if eqbase == '1':
                    with open('inventory.json', 'r') as f:
                        data = json.load(f)
                    counts = {}
                    for p, i in data.items():
                        for item, count in i['items'].items():
                            if item in counts:
                                counts[item] += count
                            else:
                                counts[item] = count
                    print(counts)
                     
        elif question1 == '3':
            print('There are currently: ', players.__len__(), 'players on the server')
            print('\nYou can also display number of players on the server from database: 1 - Display / 2 - To exit \n')
            playerbase = input('\nSelect options: ')
            print(f'\nYou have selected item number: {playerbase}, re-enter selected option number')
            playerbase2 = input('\nConfirm: ')
            print()
            if playerbase == playerbase2:
                if playerbase == '1':
                    with open('players.txt', 'r') as f:
                        key = 0
                        for line in f:
                           key += 1
                        print(f'There are currently: {key} players on the server') 
                else:
                    print("You have not confirmed your selection.. Please start again")
                    sys.exit()

        elif question1 == '4':
            numbers = 0
            for i in players.keys():
                numbers += 1
                print(f'Name player {numbers} : ', i)
            print('\nYou can also display name of players on the server from database: 1 - Display / 2 - To exit \n')
            namebase = input('\nSelect options: ')
            print(f'\nYou have selected item number: {namebase}, re-enter selected option number')
            namebase2 = input('\nConfirm: ')
            print()
            if namebase == namebase2:
                if namebase == '1':
                    with open('players.txt', 'r') as f:
                        for i, line in enumerate(f):
                            key = line.split(':')[0]
                            print(f'Name player {i+1}: {key}')

        elif question1 == '5':
            while True:
                newtype = input('Enter the name of the new item: ')
                if newtype in perks:
                    print('Sorry, this item is already in the dictionary. Please choose a different one.')
                else:
                    index = input('Enter the item ID: ')
                    def count_digit(index):
                        return index
                    index = count_digit(index)
                    if len(index) == 4:
                        with open('perks.txt', 'r') as f:
                            lines = f.readlines()
                        found = False
                        for line in lines:
                            if index in line:
                                found = True
                                break
                        if found:
                            print('This index is already in use, please choose a different one.')
                            continue
                        perks[newtype] = index
                        print(f'Item "{newtype}" added to the dictionary with ID {index}.')
                        with open('perks.txt', 'a') as f:
                            f.write(f'{newtype}: {index}\n')
                        print(f'New item {newtype} added, with id {index}')
                        print('Current item list: ')
                        print(perks)
                        break
                    else:
                        print('Wrong index length, 4 digits required')

        elif question1 == '6':
            def main():
                with open("inventory.json", "r") as f:
                    data = json.load(f)
                player_name = input("Enter the player's name: ")
                print(f'\n{data[player_name]["items"]}\n')
                if player_name not in data:
                    data[player_name] = {"items": {}}
                item_name = input("Enter the name of the item: ")
                if item_name in data[player_name]["items"]:
                    item_count = int(input("Item exists, enter new value: "))
                else:
                    item_count = int(input("Item no exists, enter value of item: "))
                data[player_name]["items"][item_name] = item_count
                with open("inventory.json", "w") as f:
                    json.dump(data, f)
            if __name__ == "__main__":
                main()
        
        elif question1 == "7":
            print('Add a new player account')
            while True:
                key = input('Enter login: ')
                if key in players:
                    print('Sorry, this login is already in use. Please choose a different one.')
                    break
                else:
                    value = input('Enter password: ')
                    players[key] = value
                    print(f'Player account "{key}" added successfully!')
                print('\nYou can also add players on the server from database: 1 - Display / 2 - To exit \n')
                addplayer = input('\nSelect options: ')
                print(f'\nYou have selected item number: {addplayer}, re-enter selected option number')
                addplayer2 = input('\nConfirm: ')
                print()
                if addplayer == addplayer2:
                    if addplayer == '1':
                        while True:
                            def read_player_file():
                                players = {}
                                with open('players.txt', 'r') as f:
                                    for line in f:
                                        login, password = line.strip().split(':')
                                        players[login] = password
                                    return players
                            def write_player_file(players):
                                with open('players.txt', 'w') as f:
                                    for login, password in players.items():
                                        f.write(f'{login}:{password}\n')
                            players = read_player_file()
                            login = input('Enter login: ')
                            if login in players:
                                print('Soory, this login is already in use. Please choose a diffrent one')
                            else:
                                password = input('Enter password: ')
                                players[login] = password
                                write_player_file(players)
                                print(f'Player account: {login} added succefully!')
                                sys.exit()
        elif question1 == "8":
            print('Enter the login of the account in which you want to change the password')
            while True:
                def update_password(filename, key):
                    with open('players.txt', 'r') as f:
                        lines = f.readlines()
                    for line in lines:
                        if line.startswith(f'{key}:'):
                            new_value = input(f'Enter a new password: ')
                            lines = [line.replace(line, f"{key}:{new_value}\n") if line.startswith(f'{key}:') else line for line in lines ]
                            print('Password successfully changed')
                            with open(filename, 'w') as f:
                                f.writelines(lines)
                            return
                    print('Sorry, there is no such login')
                key = input('Enter login: ')
                update_password('players.txt', key)
                sys.exit()
    else:
        print("You have not confirmed your selection.. Please start again")
        sys.exit()