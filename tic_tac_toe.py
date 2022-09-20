#By Santiago Rodriguez Reyes.

classic_map = ['-','-','-','-','-','-','-','-','-']
guide = [ [1, 2, 3],[4, 5, 6],[7, 8, 9]]
turn = ["O","X"]
counter = 0

#functions to show code cleaner???

def showMap(): #shows user map and the guide to enter the numbers
    print('  CLASSIC TIC TAC TOE MAP')
    print('',classic_map[0:3], guide[0][:], '\n', classic_map[3:6], guide[1][:], '\n', classic_map[6:9], guide[2][:])
    
def joinData(): 
    data = int(input('\nFill with the number of your next play according to image > '))
    return data

def repeated(): #To not to overwrite in the same position

    if classic_map[number-1] == 'O' or classic_map[number-1] == 'X':
        return True

#win criteria
def vertical(mapa):
    if mapa[0] == 'X' and mapa[3] == 'X' and mapa[6] == 'X' or mapa[0] == 'O' and mapa[3] == 'O' and mapa[6] == 'O':
        return True
        
    elif mapa[1] == 'X' and mapa[4] == 'X' and mapa[7] == 'X' or mapa[1] == 'O' and mapa[4] == 'O' and mapa[7] == 'O':
        return True
        
    elif mapa[2] == 'X' and mapa[5] == 'X' and mapa[8] == 'X' or mapa[2] == 'O' and mapa[5] == 'O' and mapa[8] == 'O':
        return True

def horizontal(mapa):
    if mapa[0] == 'X' and mapa[1] == 'X' and mapa[2] == 'X' or mapa[0] == 'O' and mapa[1] == 'O' and mapa[2] == 'O':
        return True
    elif mapa[3] == 'X' and mapa[4] == 'X' and mapa[5] == 'X' or mapa[3] == 'O' and mapa[4] == 'O' and mapa[5] == 'O':
        return True
    elif mapa[6] == 'X' and mapa[7] == 'X' and mapa[8] == 'X' or mapa[6] == 'O' and mapa[7] == 'O' and mapa[8] == 'O':
        return True

def diagonals(mapa):
    if mapa[0] == 'X' and mapa[4] == 'X' and mapa[8] == 'X' or mapa[0] == 'O' and mapa[4] == 'O' and mapa[8] == 'O':
        return True
    elif mapa[6] == 'X' and mapa[4] == 'X' and mapa[2] == 'X' or mapa[6] == 'O' and mapa[4] == 'O' and mapa[2] == 'O':
        return True

def winner(mapa): 
    if horizontal(mapa) == True or vertical(mapa) == True or diagonals(mapa) == True:
        return True


def in_game(): #return false when it has ended and no one has won at that time
    if counter == 9:
        return False


while winner(classic_map) != True and in_game() != False:
    
    showMap()
    number = joinData()
    
    if repeated() == True:
        print('This field is already fullfilled, try again.')
        continue
    
    if number > 0 and number < 10: #Get the number in the range
        classic_map[number-1] = turn[counter%2]
        counter += 1
        
    if winner(classic_map):
        showMap()
        print('Game winner is >', turn[(counter-1)%2], '<')
        print('Game finished')
        
    if in_game() == False and winner(classic_map) == False:
        print('Game finished, tie')  