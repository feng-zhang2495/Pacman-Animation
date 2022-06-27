###########################################
# Programmer: Feng Zhang
# Date: 2021-10-14
# Purpose: To create a fun pacman animation
###########################################

#Initialize Tkinter and other libraries
from tkinter import*
import time
import random 
myInterface = Tk()
myInterface.title("Pacman Animation")
screen = Canvas( myInterface, width=800, height=600, background="#87CEEB")
screen.pack()


#Background of the canvas 
screen.create_rectangle(0,600,800,400, fill='#9b7653', outline='')

screen.create_rectangle(0,410,800,400, fill='#348C31', outline='')


#Coordinates of the apple
applex1 = 150
appley1 = 300


#Creates first apple on screen
apple1 = screen.create_polygon(22 + applex1,17 + appley1, 30+ applex1,14+ appley1, 36+ applex1,13+ appley1, 41+ applex1,17+ appley1, 43+ applex1,23+ appley1, 41+ applex1,32+ appley1, 32+ applex1,46+ appley1, 23+ applex1,46+ appley1, 16+ applex1,48+ appley1, 11+ applex1,43+ appley1, 3+ applex1,32+ appley1, 2+ applex1,20+ appley1, 10+ applex1,14+ appley1, smooth=True, fill='red') 

stem1 = screen.create_line(28+ applex1,2+ appley1, 24+ applex1,8+ appley1, 23+ applex1,17+ appley1, smooth=1, fill='brown', width=3)

applex1 = 400


#Creates Second Apple on screen
apple2 = screen.create_polygon(22 + applex1,17 + appley1, 30+ applex1,14+ appley1, 36+ applex1,13+ appley1, 41+ applex1,17+ appley1, 43+ applex1,23+ appley1, 41+ applex1,32+ appley1, 32+ applex1,46+ appley1, 23+ applex1,46+ appley1, 16+ applex1,48+ appley1, 11+ applex1,43+ appley1, 3+ applex1,32+ appley1, 2+ applex1,20+ appley1, 10+ applex1,14+ appley1, smooth=True, fill='red') 

stem2 = screen.create_line(28+ applex1,2+ appley1, 24+ applex1,8+ appley1, 23+ applex1,17+ appley1, smooth=1, fill='brown', width=3)

#Used later on as switches to prevent inefficient code
ran1 = False
ran2 = False

#Coordinates of Pacman
pacX = -150
pacY = 250

#Angles of Pacman's mouth
startAngle = 30
startExtent = 300
jawSpeed = -1

#SCENE 1: PACMAN EATS APPLES
while True:

  #Moves pacman to the right
  pacX += 2
  
  #Moves pacmans mouth
  startAngle += jawSpeed
  startExtent -= jawSpeed*2  

  #Draws pacman if his mouth isnt closed 
  if startAngle > 0:
    pacman = screen.create_arc(pacX, pacY, pacX+150, pacY+150, fill='yellow', start=startAngle, extent= startExtent, width=3)
  
  #If pacman's mouth is fully closed
  else: 
    pacman = screen.create_oval(pacX, pacY, pacX+150, pacY+150, fill='yellow', width=3)
  
  #If the angle of pacman's mouth exceeds 60, close his mouth
  if startAngle >= 30:
    jawSpeed = -1
  
  #Open pacman's mouth if its closed
  elif startAngle <= 0:
    jawSpeed = 1
  
  #Deltes apples from canvas if pacman ate them
  if pacX + 75 > 150:
    screen.delete(apple1, stem1)

  if pacX + 75 > applex1:
    screen.delete(apple2, stem2)

  #Introduction to scene 2
  if pacX + 75 >= 550:

    #Creates the first text on screen
    text = screen.create_text(400, 100, text='How Dare You...', font='Bakersville 40')


    #Exclamation mark
    markCircle = screen.create_oval(400, 300, 425, 325, fill='red', outline ='')

    markTop = screen.create_polygon(400, 290, 425, 290, 440, 200, 385, 200, fill='red', outline='')

    #Waits for user to read text
    screen.update()
    time.sleep(3) 
    screen.delete(markCircle, text, markTop, pacman)

    #Exits the first Scene 
    break

  #Updates canvas and deletes any animated objects
  screen.update()
  time.sleep(0.01)
  screen.delete(pacman)

#END OF SCENE 1

#Coordinates of where the apple boss starts
appleBossx1 = 725
appleBossy1 = 70

#Angles for pacman's mouth
jawSpeed = 1
startAng = 210
extentAng = 300


#Run text for scene 2
runtext = screen.create_text(400, 100, text='RUN PACMAN, RUN!', font='Bakersville 40', fill='red')

#SCENE 2: APPLE BOSS CHASES PACMAN
while True:
  #DRAWING APPLE BOSS

  #Apple boss body
  appleBoss = screen.create_polygon(117+appleBossx1,69+appleBossy1, 144+appleBossx1,60+appleBossy1, 170+appleBossx1,54+appleBossy1, 195+appleBossx1,58+appleBossy1,212+appleBossx1,70+appleBossy1,220+appleBossx1,85+appleBossy1,228+appleBossx1,111+appleBossy1,231+appleBossx1,142+appleBossy1,228+appleBossx1,178+appleBossy1,212+appleBossx1,219+appleBossy1,183+appleBossx1,239+appleBossy1,147+appleBossx1,251+appleBossy1,107+appleBossx1,257+appleBossy1,60+appleBossx1,232+appleBossy1,39+appleBossx1,186+appleBossy1,29+appleBossx1,132+appleBossy1,34+appleBossx1,105+appleBossy1,51+appleBossx1,81+appleBossy1,84+appleBossx1,70+appleBossy1, fill='red', smooth=1)

  #Apple boss Legs
  appleBossLeg1 = screen.create_line(124+appleBossx1, 255+appleBossy1, 124+appleBossx1, 336+appleBossy1, fill='brown', width=3)

  appleBossLeg2 = screen.create_line(170+appleBossx1, 244+appleBossy1, 170+appleBossx1, 336+appleBossy1, fill='brown', width=3)

  #Apple boss Eyes
  eye1 = screen.create_oval(appleBossx1 + 70, appleBossy1 + 110, appleBossx1 + 90, appleBossy1+130, fill='white', outline ='')

  eye2 =screen.create_oval(appleBossx1 + 120, appleBossy1 + 110, appleBossx1 + 140, appleBossy1+130, fill='white', outline ='')

  #Apple boss Eyebrows
  Eyebrow1 = screen.create_line(appleBossx1 + 70, appleBossy1 + 95, appleBossx1 + 100, appleBossy1 + 100, fill='brown', width=3)

  Eyebrow2 = screen.create_line(appleBossx1 + 140, appleBossy1 + 95, appleBossx1 + 115, appleBossy1 + 105, fill='brown', width=3)

  #Apple boss Pupils
  pupil1 = screen.create_oval(appleBossx1 + 70, appleBossy1 + 115, appleBossx1 + 80, appleBossy1+125, fill='black', outline ='')

  pupil2 = screen.create_oval(appleBossx1 + 120, appleBossy1 + 115, appleBossx1 + 130, appleBossy1+125, fill='black', outline ='')

  #Apple boss Mouth
  mouth = screen.create_oval(appleBossx1 + 90, appleBossy1 + 170, appleBossx1 + 130, appleBossy1+230, fill='black', outline ='')

  #Apple boss Tooth
  teeth1 =  screen.create_arc(appleBossx1 +90, appleBossy1+170, appleBossx1+130, appleBossy1 +230, fill='white', outline ='', start=60, extent=60)

  #Apple boss Tongue (red in mouth)
  tongue1 = screen.create_oval(appleBossx1 + 100, appleBossy1 + 190, appleBossx1 + 120, appleBossy1+220, fill='red', outline ='') 

  #Stem of apple boss   
  stem1 = screen.create_line(122+appleBossx1,68+appleBossy1,112+appleBossx1,5+appleBossy1, fill='#5b4a35', width=5) 

  #Leaf beside the stem of apple 
  leaf = screen.create_polygon(127+appleBossx1,64+appleBossy1,124+appleBossx1,49+appleBossy1,128+appleBossx1,30+appleBossy1,146+appleBossx1,14+appleBossy1,171+appleBossx1,5+appleBossy1,183+appleBossx1,8+appleBossy1,178+appleBossx1,22+appleBossy1,173+appleBossx1,35+appleBossy1,166+appleBossx1,53+appleBossy1,147+appleBossx1,59+appleBossy1, fill='green', outline='', smooth=1)

  #END OF APPLE BOSS DRAWING 


  #PACMAN RUNNING BACKWARDS DRAWING

  #Changing pacman's mouth opening 
  startAng -= jawSpeed
  extentAng += jawSpeed*2

  #If his mouth isnt closed 
  if startAng > 180:
    pacman = screen.create_arc(pacX, pacY, pacX+150, pacY+150, start=startAng, extent=extentAng, fill='yellow', width=3)

  #If his mouth is closed draw a circle
  else:
    pacman = screen.create_oval(pacX, pacY, pacX+150, pacY+150, fill='yellow', width=3)

  #If his mouth is fully open, close it
  if startAng >= 210:
    jawSpeed = 1
  
  #If his mouth is fully closed open it 
  elif startAng <= 180:
    jawSpeed = -1

  #END OF PACMAN DRAWING

  
  #Moves the apple and pacman
  pacX -= 2.5
  appleBossx1 -= 3


  #Updates drawings to canvas
  screen.update()
  time.sleep(0.01)
  screen.delete(pacman, appleBoss, tongue1, teeth1, appleBossLeg1, appleBossLeg2, pupil1, pupil2, eye1, eye2, Eyebrow1, Eyebrow2, mouth, stem1, leaf)
  
  #If everyone has ran off the screen
  if appleBossx1 + 231 < 0:
    screen.delete(runtext)
    break 

#END OF APPLE CHASING PACMAN SCENE


#PACMAN falling off cliff animation

#Background for the scene
#Sky
screen.create_rectangle(0,500,600,400, fill = '#87CEEB', outline='')

#Cliff
screen.create_rectangle(600,500,800,150, fill='#9b7653', outline='')

#Grass on cliff
screen.create_rectangle(600,150,800,160, fill='#348c31', outline='')

#Coordinates of apple and pacman
appleBossx1 = 1000
appleBossy1 = -180

pacX = 800
pacY = 0

#Variable used to simulate parabolic motion in scene
multiplier = 1

#... Text on screen
dotText = screen.create_text(400, 100, text='...', font='Bakersville 40', fill='red')

while True:

  #DRAWS THE APPLE BOSS AGAIN
  #Apple boss body
  appleBoss = screen.create_polygon(117+appleBossx1,69+appleBossy1, 144+appleBossx1,60+appleBossy1, 170+appleBossx1,54+appleBossy1, 195+appleBossx1,58+appleBossy1,212+appleBossx1,70+appleBossy1,220+appleBossx1,85+appleBossy1,228+appleBossx1,111+appleBossy1,231+appleBossx1,142+appleBossy1,228+appleBossx1,178+appleBossy1,212+appleBossx1,219+appleBossy1,183+appleBossx1,239+appleBossy1,147+appleBossx1,251+appleBossy1,107+appleBossx1,257+appleBossy1,60+appleBossx1,232+appleBossy1,39+appleBossx1,186+appleBossy1,29+appleBossx1,132+appleBossy1,34+appleBossx1,105+appleBossy1,51+appleBossx1,81+appleBossy1,84+appleBossx1,70+appleBossy1, fill='red', smooth=1)

  #Legs
  appleBossLeg1 = screen.create_line(124+appleBossx1, 255+appleBossy1, 124+appleBossx1, 336+appleBossy1, fill='brown', width=3)

  appleBossLeg2 = screen.create_line(170+appleBossx1, 244+appleBossy1, 170+appleBossx1, 336+appleBossy1, fill='brown', width=3)

  #Eyes
  eye1 = screen.create_oval(appleBossx1 + 70, appleBossy1 + 110, appleBossx1 + 90, appleBossy1+130, fill='white', outline ='')

  eye2 =screen.create_oval(appleBossx1 + 120, appleBossy1 + 110, appleBossx1 + 140, appleBossy1+130, fill='white', outline ='')

  #Eyebrows
  Eyebrow1 = screen.create_line(appleBossx1 + 70, appleBossy1 + 95, appleBossx1 + 100, appleBossy1 + 100, fill='brown', width=3)

  Eyebrow2 = screen.create_line(appleBossx1 + 140, appleBossy1 + 95, appleBossx1 + 115, appleBossy1 + 105, fill='brown', width=3)

  #Pupils
  pupil1 = screen.create_oval(appleBossx1 + 70, appleBossy1 + 115, appleBossx1 + 80, appleBossy1+125, fill='black', outline ='')

  pupil2 = screen.create_oval(appleBossx1 + 120, appleBossy1 + 115, appleBossx1 + 130, appleBossy1+125, fill='black', outline ='')

  #Mouth
  mouth = screen.create_oval(appleBossx1 + 90, appleBossy1 + 170, appleBossx1 + 130, appleBossy1+230, fill='black', outline ='')

  #Tooth
  teeth1 =  screen.create_arc(appleBossx1 +90, appleBossy1+170, appleBossx1+130, appleBossy1 +230, fill='white', outline ='', start=60, extent=60)

  #Tongue
  tongue1 = screen.create_oval(appleBossx1 + 100, appleBossy1 + 190, appleBossx1 + 120, appleBossy1+220, fill='red', outline ='') 

  #Stem of apple boss   
  stem1 = screen.create_line(122+appleBossx1,68+appleBossy1,112+appleBossx1,5+appleBossy1, fill='#5b4a35', width=5) 

  #Leaf beside the stem of apple 
  leaf = screen.create_polygon(127+appleBossx1,64+appleBossy1,124+appleBossx1,49+appleBossy1,128+appleBossx1,30+appleBossy1,146+appleBossx1,14+appleBossy1,171+appleBossx1,5+appleBossy1,183+appleBossx1,8+appleBossy1,178+appleBossx1,22+appleBossy1,173+appleBossx1,35+appleBossy1,166+appleBossx1,53+appleBossy1,147+appleBossx1,59+appleBossy1, fill='green', outline='', smooth=1)

  #END OF APPLE BOSS DRAWING 


  #PACMAN DRAWING
  
  #Mouth angles
  startAng -= jawSpeed
  extentAng += jawSpeed*2

  #If his mouth isnt closed
  if startAng > 180:
    pacman = screen.create_arc(pacX, pacY, pacX+150, pacY+150, start=startAng, extent=extentAng, fill='yellow', width=3)
  
  #If his mouth is closed, draw a circle
  else:
    pacman = screen.create_oval(pacX, pacY, pacX+150, pacY+150, fill='yellow', width=3)

  #If his mouth is fully open, close it
  if startAng >= 210:
    jawSpeed = 1
  
  #If his mouth is fully closed, open it 
  elif startAng <= 180:
    jawSpeed = -1

  #If pacman has reached the cliff edge
  if pacX + 75 < 600:

    #Pacman slowly falls down the cliff 
    pacY += 0.025*multiplier 
    multiplier += 1
  
  #Moves pacman and the apple
  pacX -= 2

  #Apple boss stops at cliff edge 
  if appleBossx1+51 > 600:
    appleBossx1 -= 3


  #When pacman hits the ground 
  if pacY+150 >= 505:

    #Exits the loop 
    time.sleep(2)
    screen.delete(pacman, dotText)
    break


  #Updates the canvas
  screen.update()
  time.sleep(0.01)
  screen.delete(pacman, appleBoss, tongue1, teeth1, appleBossLeg1, appleBossLeg2, pupil1, pupil2, eye1, eye2, Eyebrow1, Eyebrow2, mouth, stem1, leaf)
  

#FINAL SCENE
for pacmen in range(5):
  #Generates random sizes and locations
  xRange = random.randint(50, 550)
  size = random.randint(20, 70)

  #Creates smaller pacmen 
  screen.create_arc(xRange, 500, xRange+size, 500-size, fill='yellow', start=30, extent=300, width=2)

#Generates happily ever after text on canvas
happyText = screen.create_text(400, 100, text='Poof!\nAnd they lived happily ever after.', font='Bakersville 20', fill='black')

#Updates the canvas
screen.update()


#END OF PROGRAM