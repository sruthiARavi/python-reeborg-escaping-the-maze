# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
class solution :
  def turn_around():
      turn_left()
      turn_left()
      
  def turn_right():
      turn_around()
      turn_left()
      
  #maze challenge 
  
  #edge-case : 
  #No hurdles on any side for single step moves
  while front_is_clear():
      move()
      
  turn_left()
  #solution 
  while not at_goal(): 
      if right_is_clear(): 
          turn_right()
          move()
      elif front_is_clear():
          move()    
      else:                    
          turn_left()  
    
