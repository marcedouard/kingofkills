#4TripleM
#King of Kills
#Mouayad, Matthew, Mark, Julius
#Obtain CA$H through killing the enemy, picking up random money drops

from gamelib import*  #import game library

#objects and initial settings
game = Game (800,600,"King of Kills")
bk = Image("background.jpg",game)
play = Image('Play.png',game)
bk.resizeTo(800,600)
 

#Level 1 - game loop


while not game.over:
    game.processInput()
    bk.draw()
    
    (play.draw)
    
    game.update()



game.over = False
#Level 2 - game loop
while not game.over:
    game.processInput()
    play.draw()

    game.update(30)

game.quit()
