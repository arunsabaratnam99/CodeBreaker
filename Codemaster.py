import copy
import random
from itertools import permutations
from typing import OrderedDict


def computerguess(guess, colours, codemaster, blackandwhite, guesses):
  black = 0
  white = 0
  
  guesses.append(list(OrderedDict.fromkeys(guess)))
  
  #changing the computers guess from numbers to colours then removing it from the colours list 
  colourguess = []
  
  for j in range(0, len(guess)):
    index = guess[j]
    colourguess.append(colours[index])
    
  #printing the computers guess
  print('\nThe computer guessed: ', end = "")

  for j in range(0, 4):
    if j == 3:
      print(colourguess[j])
    else:
      print(colourguess[j], end = ", ")
    
  #receiving the computers guess and checking the blacks and whites for that guess
  
  newcolourguess = list(OrderedDict.fromkeys(colourguess))
  
  if len(newcolourguess) == 4:
    notFirst = True 
  else:
    notFirst = False 

  
  for i in range(len(newcolourguess)):
    if notFirst == False and i == 1:
      if newcolourguess[1] in codemaster[1:4]   :
        black = black + 1 
      elif newcolourguess[1] == codemaster[0]:
        white = white + 1
    else:
      if newcolourguess[i] == codemaster[i]:
        black = black + 1
        
      elif newcolourguess[i] in codemaster:
        white = white + 1
        
  #adding the blacks and white from that guess into the blackandwhite array
  templist = []
  templist.append(black)
  templist.append(white)
  blackandwhite.append(templist)
  
  #based on the black and whites, it will show a response
  if black == 4:
    print('\nThe computer got 4 blacks')
    raise SystemExit
    return True, blackandwhite
  else:
    print('\nThe computer got ' + str(black) + ' blacks, and ' + str(white) + ' whites for this guess.')
    return False, blackandwhite

def blackandwhitecheck(blackandwhite,guesses,possiblecolours,notpossiblecolours, continue_going):
  counter = 0
  for i in blackandwhite:
    guessatblackandwhite = guesses[counter]
  
    if i == [2,0] or i == [1,1] or i == [0,2]:  
      continue_going = False 
      for l in range(2):
        possiblecolours.append(guessatblackandwhite[l])
      
    elif i == [0,0]:
      for l in range(2):
       notpossiblecolours.append(guessatblackandwhite[l]) 
       
       if guessatblackandwhite[l] in possiblecolours:
         possiblecolours.remove(guessatblackandwhite[l])
      
      for j in range(0, counter): 
        if blackandwhite[j] == [1,0] or blackandwhite[j] == [0,1]:
          for k in guesses[j]:
            if k not in notpossiblecolours:
             possiblecolours.append(k)
            
    counter = counter + 1 
      
      
  return continue_going, possiblecolours, notpossiblecolours
  

#Picking colours
colours = ['Red', 'Yellow', 'Blue', 'Green', 'Orange', 'Pink', 'Purple', 'Cyan', 'Silver', 'Teal']

name = input('Please enter your name\n')

print('\n\nHello ' + name + ' you are the codemaster the colours that you have to choose from are below:\n')

print(*colours, sep = ', ')

codemaster = []
blackandwhite = []
possiblecolours = []
notpossiblecolours = []
guesses = []

for i in range(1, 5):
  x = input('\nPlease enter your colour #' + str(i) + '\n')

  while x.lower() not in (colour.lower() for colour in colours) or x.lower() in (codemas.lower() for codemas in codemaster):
    print('\nSorry that is not a valid colour please enter again')
    x = input('\nPlease enter your colour #' + str(i) + '\n')

  codemaster.append(x)
  
codemaster = [codemas.capitalize() for codemas in codemaster]

print('\nYour chosen colours are: ', end = '')
print(*codemaster, sep = ', ')

print('--------------------------------------------------')

#Guessing (0,1,1,1), (1,2,2,2), (2,3,3,3), (3,0,0,0) and regustering the blacks and whites within another array
firstguesses = ([0,1,1,1], [1,2,2,2], [2,3,3,3], [3,0,0,0])

for i in range(len(firstguesses)):
  computerguess(firstguesses[i], colours, codemaster, blackandwhite, guesses)
  
#checking the list of the blacks and white in order to see if there are any 2,0 1,1 or 0,2 else keep going 
continue_going = True  
counter = 0 

for i in blackandwhite:
  guessatblackandwhite = guesses[counter]
  if i == [2,0] or i == [1,1] or i == [0,2]:  
    continue_going = False 
    for l in range(2):
      possiblecolours.append(guessatblackandwhite[l])
      
  elif i == [0,0]:
    for l in range(2):
      notpossiblecolours.append(guessatblackandwhite[l])
    
    for j in range(0, counter):
      if blackandwhite[j] == [1,0] or blackandwhite[j] == [0,1]:
        for k in guesses[j]:
          if k not in notpossiblecolours:
            possiblecolours.append(k)

  counter = counter + 1
  
while continue_going == True:
    nextguesses = ([3,1,1,1],[2,0,0,0])
    
    for i in range(len(nextguesses)):
      computerguess(nextguesses[i], colours, codemaster, blackandwhite, guesses,)
      if blackandwhite[-1] == [2,0] or blackandwhite[-1] == [1,1] or blackandwhite[-1] == [0,2] or blackandwhite[-1] == [0,0]:
        break
      
    receive = blackandwhitecheck(blackandwhite,guesses,possiblecolours,notpossiblecolours,continue_going) 
    continue_going = receive[0]
    possiblecolours = receive[1]
    notpossiblecolours = receive[2] 
    continue_going = False 

if blackandwhite.count([0,0]) == 5:
  continue_going = True
  nextguesses = ([4,5,5,5],[5,6,6,6], [6,7,7,7], [7,4,4,4])
  
  for i in range(len(nextguesses)):
    computerguess(nextguesses[i], colours, codemaster, blackandwhite, guesses)
    
  receive = blackandwhitecheck(blackandwhite,guesses,possiblecolours,notpossiblecolours,continue_going) 
  continue_going = receive[0]
  possiblecolours = receive[1]
  notpossiblecolours = receive[2] 
  
  if continue_going == True:
    nextguesses = ([7,5,5,5],[6,4,4,4])
    
    for i in range(len(nextguesses)):
      computerguess(nextguesses[i], colours, codemaster, blackandwhite, guesses)
      if blackandwhite[-1] == [2,0] or blackandwhite[-1] == [1,1] or blackandwhite[-1] == [0,2] or blackandwhite[-1] == [0,0]:
        break
      
    receive = blackandwhitecheck(blackandwhite,guesses,possiblecolours,notpossiblecolours,continue_going) 
    possiblecolours = receive[1]
    notpossiblecolours = receive[2] 
    
coloursused = []
for i in range(len(guesses)):
  coloursused = coloursused + guesses[i]
    
coloursused = list(set(coloursused))   
  
possiblecolours = list(OrderedDict.fromkeys(possiblecolours))
notpossiblecolours = list(OrderedDict.fromkeys(notpossiblecolours))

#Using the blacks and whites from that guess in order to make an educated guess
educatedguess = ['temp', 'temp', 'temp','temp']

for i in range(0, len(guesses)):
  guessatpoint = guesses[i]
  
  if blackandwhite[i] == [1,0]:
    for j in range(0,len(possiblecolours)):
      if possiblecolours[j] in guessatpoint:
        if guessatpoint[0] == possiblecolours[j]:
          educatedguess[0] = possiblecolours[j]
        else:
          for k in range(1,len(educatedguess)):
            if possiblecolours[j] not in educatedguess:
              if educatedguess[k] == 'temp':
                educatedguess[k] = possiblecolours[j]
                break
    for l in guessatpoint:
      if l not in possiblecolours:
        notpossiblecolours.append(l)
  
  elif blackandwhite[i] == [0,1]:
    for j in range(0,len(possiblecolours)):
      if possiblecolours[j] in guessatpoint:
        if guessatpoint[0] == possiblecolours[j]: 
          for k in range(1,len(educatedguess)):
            if possiblecolours[j] not in educatedguess:
              if educatedguess[k] == 'temp':
                educatedguess[k] = possiblecolours[j]
                break
        else:
           educatedguess[0] = possiblecolours[j]  
            
    for l in guessatpoint:
      if l not in possiblecolours:
        notpossiblecolours.append(l) 
                    
  elif blackandwhite[i] == [1,1]:
    for i in guessatpoint:
      if i not in educatedguess:
        for k in range(1,len(educatedguess)):
            if educatedguess[k] == 'temp':
              educatedguess[k] = i
              break
  
  elif blackandwhite[i] == [0,2]:
    educatedguess[0] = guessatpoint[1]
     
    if educatedguess[1] != 'temp' and guessatpoint[0] not in educatedguess:
      for k in range(1,len(educatedguess)):
            if educatedguess[k] == 'temp':
              educatedguess[k] = educatedguess[1]
              educatedguess[1] = guessatpoint[0]
              break 
            
  elif blackandwhite[i] == [2,0]:
    educatedguess[0] = guessatpoint[0]

    if educatedguess[1] != 'temp' and educatedguess[1] != guessatpoint[1]:
      for k in range(1,len(educatedguess)):
            if educatedguess[k] == 'temp':
              educatedguess[k] = educatedguess[1]
              educatedguess[1] = guessatpoint[1]
              break 
            

possiblecolours = list(OrderedDict.fromkeys(possiblecolours))
notpossiblecolours = list(OrderedDict.fromkeys(notpossiblecolours))

#Use the information of the educated guess to continue guessing and getting the 4 main colours 
copyofeducatedguess = copy.deepcopy(educatedguess)
colournumbers = [0,1,2,3,4,5,6,7,8,9]
colournumbers = list(set(colournumbers) - set(coloursused))
between = []
holdv2 = []
go = True 

while go == True or len(colournumbers) == 0:
  if len(possiblecolours) == 3 or len(possiblecolours) == 2:
    try:
      choices = random.sample(colournumbers, 1)
    except:
      go = False 
      break 
  elif len(possiblecolours) == 1:
    try:
      choices = random.sample(colournumbers, 1)
    except:
      go = False 
      break
    
  elif len(possiblecolours) == 4:
    go = False 
    break 
    
  copyofchoices = copy.deepcopy(choices)

  for i in choices:
    while i in colournumbers:
      colournumbers.remove(i)   

  choicescounter = 0
  hold = []
  for i in range(len(educatedguess)):
    if educatedguess[i] == 'temp' or educatedguess[i] in notpossiblecolours:
      if len(choices) > 0 :
        educatedguess[i] = choices[0]
        hold.append(choices[0])
        hold.append(i)
        choices.remove(choices[0])
      else:
        educatedguess[i] = notpossiblecolours[random.randint(0, len(notpossiblecolours) - 1)]


  result = computerguess(educatedguess, colours, codemaster, blackandwhite,guesses)

  expected = len(possiblecolours)
  blackandwhiteatindex = blackandwhite[-1]
  prevblackandwhite = blackandwhite[-2]
  addtotal = blackandwhiteatindex[0] + blackandwhiteatindex[1]
  
  if prevblackandwhite[0] < blackandwhiteatindex[0]:
    if len(blackandwhite) != 5:
      holdv2.append(hold)
    
  if expected == addtotal:
    for i in copyofchoices:
      notpossiblecolours.append(i)
         
  elif expected == (addtotal - 1):
    if len(possiblecolours) == 1:
      for i in copyofchoices:
        between.append(i)
      
      educatedguess.clear()
      educatedguess.extend(copyofeducatedguess)

    else:
      for i in copyofchoices:
        possiblecolours.append(i) 
       
  elif expected == (addtotal - 2):
    for i in copyofchoices:
      possiblecolours.append(i) 
      
recent = blackandwhite[-1]
recentadd = recent[0] + recent[1]
copyofcopy =  copy.deepcopy(copyofeducatedguess)

if recentadd != 4:
  copyofcopy =  copy.deepcopy(copyofeducatedguess)
  count = 0 
  for i in range(len(copyofeducatedguess)):
    if copyofeducatedguess[i] == 'temp':
      copyofeducatedguess[i] = between[count]
      count = count + 1
      
  guess = copy.deepcopy(copyofeducatedguess)
  
  possiblecolours.extend(between)
  
  computerguess(guess,colours,codemaster,blackandwhite,guesses)

if len(holdv2) > 0:
  supposedtobe = holdv2[-1]
  
  copyofcopy[supposedtobe[1]] = supposedtobe[0]
  
  for i in range(len(possiblecolours)):
    if possiblecolours[i] not in copyofcopy:
      for j in range(len(copyofcopy)):
        if copyofcopy[j] == 'temp':
          copyofcopy[j] = possiblecolours[i]
          break
        
  if guesses[-1] != copyofcopy:
    computerguess(copyofcopy,colours, codemaster,blackandwhite,guesses)
  
  temp = copyofcopy[2]
  copyofcopy[2] = copyofcopy[3]
  copyofcopy[3] = temp 
  
  if prevblackandwhite[0] < blackandwhiteatindex[0]:
    if len(blackandwhite) != 5:
      holdv2.append(hold)
      
  computerguess(copyofcopy,colours, codemaster,blackandwhite,guesses)



unknowns = []

for i in range(len(guesses)):
  if blackandwhite[i] == [1,3] or blackandwhite[i] == [3,1] or blackandwhite[i] == [2,2]:
    recentguess = guesses[i]
    

unknowns = recentguess[1:4]
known = recentguess[0]
combinations = list(permutations(unknowns,3))
countz = 1
guess = []

while blackandwhite[-1] != [4,0]:
  guess.clear()
  
  guess.append(known)
  
  combinationatpoint = list(combinations[countz])
  
  guess.extend(combinationatpoint)
  
  computerguess(guess,colours,codemaster,blackandwhite,guesses)
  
  countz = countz + 1
  
  



