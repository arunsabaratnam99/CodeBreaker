import random


def checker(guesses, colours):
  error = 0 
  reason = 0
  for k in range(len(guesses)):
    if guesses[k].lower() not in (colour.lower() for colour in colours):
      error = error + 1
      reason = reason + 1
      break

  for h in range(len(guesses)):
    if guesses.count(guesses[h]) > 1:
      error = error + 1
      reason = reason + 2
      break
  
  if len(guesses) != 4:
    error = error + 1 
    reason = reason + 3
    
  #No problems
  if error == 0:
    return True, 1 
  #There is a problem
  elif error == 1:
    #Colour isnt a valid colour
    if reason == 1:
      return False, 1 
    #Colour is repeated
    elif reason == 2:
      return False, 2
    #More than 4 colours inputted 
    else:
      return False, 3 
  elif error == 2: 
    #error 1 and 2
    if reason == 3:
      return False, 4 
    #error 1 and 3
    elif reason == 4:
      return False, 5
    #error 3 and 2 
    else:
      return False, 6
  else:
    #All errors
    return False, 7

def round(round):
  colourGuess = []
  print('\nEnter guess ' + str(round) + ':')

  for j in range(1, 5):
    colour = input('\nEnter your colour #' + str(j) + "\n")
    colourGuess.append(colour)
  
  return colourGuess

def penalty(name, penaltycount, type):
  if type[1] == 1: 
    print('\nSorry ' + name + ', cannot recognize the colours you entered. One penalty is considered')

  elif type[1] == 2:
    print('\nSorry ' + name + ', repeated colours are not allowed in this game. One penalty is considered')

  elif type[1] == 3:
    print('\nSorry, ' + name + ', you have to have 4 colours inputted. One penalty is considered.')
  
  elif type[1] == 4:
    print('\nSorry ' + name + ', repeated colours are not allowed in this game. Also, cannot recognize the colours you entered. One penality is considered')
  
  elif type[1] == 5:
    print('\nSorry ' + name + ', cannot recognize the colours you entered. Also, you have to have 4 colours inputted. One penalty is considered.')
    
  elif type[1] == 6: 
    print('Sorry, ' + name + ', repeated colours are not allowed in this game. Also, you have to have 4 colours inputted. One penalty is considered.')
    
  else: 
    print('Sorry, ' + name + ', cannot recognize the colours you entered. Also, repeated colours are not allowed in this game. Also, you have to have 4 colours inputted. One penalty is considered' )
  penaltycount+= 1
  return penaltycount

def good(playername,colourguess, codeMaster):
  white = 0 
  black = 0 

  for i in range (len(colourguess)):
    if colourguess[i].lower()  in (master.lower() for master in codeMaster):
      if colourguess[i].lower() == codeMaster[i].lower():
        black += 1
      else:
        white += 1
    
  if black == 4:
    print('\nYou got 4 blacks', playername)
    return True
  else:
    print('\nYou got ' + str(black) + ' blacks, and ' + str(white) + ' whites for this guess.')
    return False 
    

colours = ['Red', 'Yellow', 'Blue', 'Green', 'Orange', 'Pink', 'Purple', 'Cyan', 'Silver', 'Teal']

#selecting the code
codemaster = []
while len(codemaster) < 4 :
  randomint = random.randint(0,len(colours) - 1)
  
  if colours[randomint] not in codemaster:
    codemaster.append(colours[randomint])

#Getting the players name 
name = input('What is your name?\n')
print('\nWelcome to Master Mind', name + '!\n' )

#Printing all the colours
print(*colours, sep = ", ")
  
print('\nYou have 15 guesses, total of 5 penalties are allowed but avoid penalties.')
print('\nThe code maker selected 4 colours.\n\nYou can start guessing', name)

#Starting the game

penaltycount = 0 
gameWin = False 

for n in range(1, 16):
  colourGuess = input('\nPlease input your guess: ').split()

  check = checker(colourGuess, colours) 

  if check[0] == False :
    penaltycount = penalty(name, penaltycount, check)
    if penaltycount == 5:
      print('\nTotal penalties = ' + str(penaltycount))
      print('\n' + name + ', you lost the game by reaching the maxiumum number of allowed penalities.')
      gameWin = True
      break
    else: 
      print('\nTotal penalties = ' + str(penaltycount))
  elif check[0] == True:
    endgame = good(name, colourGuess, codemaster)
    if endgame == True:
      gameWin == True
      print('\nYou won the game with ' + str(n) + ' guesses ' + ' and ' + str(penaltycount) + ' penalties, Congratulations')
      break 
  else:
      print('Error')


if gameWin == False :
  print('Sorry ', name + ', you ran out of guesses and you lost the game with ' + str(penaltycount) + ' penalties')







