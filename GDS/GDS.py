# German Discount Supermarkets: the RPG
# by Ian Garforth 2024

import os
import csv


# Clear console method - used throughout the game
def clear_console():
    if (os.name == 'posix'): # works for MacOS and Linux
        cmd = 'clear'
    else: # works for Windows
        cmd = 'cls'
    os.system(cmd)


# Import scene data from CSV file - MEMORY PROBLEMS, IF CSV FILE GETS TOO BIG?
with open("GDS_the_RPG_scene_data.csv") as scene_data:
  scene_data_reader = csv.reader(scene_data)
  scene_rows = list(scene_data_reader)
  

# start-up message
start_up_message = "###########################################\n\nWelcome to Supermarket: the RPG \n \n Choose a player class\n1: Mum with kids\n2: Sharp-elbowed Granny\n3) Sunday League Football Dad on way back from having lost game."


#init of variables where necessary
player_choice_of_class = 0
#next_segment = 0


# Setup of player class, influenced by which type of shopper they initially choose
startup_stats = [["Mum with kids", 30, 120, 120, 70, 70, 100], ["Sharp-elbowed Granny", 45, 70, 70, 100, 100, 80], ["Sunday League Football Dad on way back from having lost game", 25, 100, 100, 120, 120, 100]]

class Player:
  def __init__(self, player_class, time_remaining, stamina, max_stamina, patience, max_patience, money):
    self.player_class = player_class
    self.time_remaining = time_remaining
    self.stamina = stamina
    self.max_stamina = max_stamina
    self.patience = patience
    self.max_patience = max_patience
    self.money = money

  def __repr__(self):
    player_desc = "The player is of \"{}\" class, and has a time factor of {}.  Their stamina is {}, their patience is {}, and their starting money is {}.".format(self.player_class, self.time_remaining, self.max_stamina, self.max_patience, self.money)
    return player_desc

  def lose_patience(amount):
    player.patience -= amount
    return player.patience

  def get_tired(amount):
    player.stamina -= amount
    return player.stamina

  def spend_money(amount):
    player.money -= amount
    return player.money

  def lose_time(amount):
    player.time_remaining -= amount
    return player.time_remaining


class StoreStaff:
  def __init__(self, role, speed, stroppiness):
    self.role = role
    self.speed = speed
    self.stroppiness = stroppiness

  def __repr__(self):
    store_staff_desc = "The Store Staff is a {}.  Their speed is {}, and their stroppiness is {} (out of 100).".format(self.role, self.speed, self.stroppiness)

  def go_slow(delay_to_player):
    player.time -= delay_to_player
    return player.time

  def argue_with_player(player_stamina_reduction):
    player.stamina -= player_stamina_reduction
    return player.stamina

  def annoy_player(player_patience_reduction):
    player.patience -= player_patience_reduction
    return player.patience


# Other methods not bound to classes

# Method that loads the next screen
def load_next_scene(scene_number):
  # Clear the screen
  clear_console()
  # Print current stats
  #print(display_stats(player))
  this_scene = scene_rows[scene_number]
  this_scene_title = this_scene[1]
  this_scene_text = this_scene[2]
  this_scene_option_one = this_scene[3]
  this_scene_option_one_redirect = this_scene[4]
  this_scene_option_two = this_scene[5]
  this_scene_option_two_redirect = this_scene[6]
  this_scene_option_three = this_scene[7]
  this_scene_option_three_redirect = this_scene[8]
  last_scene_outcome = this_scene[11]
  
  # Resolve any functions passed
  if this_scene[9] != "":
    this_scene_functions_passed = list(this_scene[9])
    this_scene_function_quantity = int("".join(list(this_scene[10])))
    if "".join(this_scene_functions_passed[0:]) == "patience":
      Player.lose_patience(this_scene_function_quantity)
    elif "".join(this_scene_functions_passed[0:]) == "stamina":
      Player.get_tired(this_scene_function_quantity)
    elif "".join(this_scene_functions_passed[0:]) == "money":
      Player.spend_money(this_scene_function_quantity)
    elif "".join(this_scene_functions_passed[0:]) == "time":
      Player.lose_time(this_scene_function_quantity)
    

  # Print current stats above scene
  print(display_stats(player))

  # Concatenate the data to print
  this_scene_concat = this_scene_title + "\n\n" + this_scene_text + "\n\n" + last_scene_outcome + "".join(list(this_scene[10])) + " " + "".join(list(this_scene[9][0:])) + "." + "\n\n1)" + this_scene_option_one + "\n\n2)" + this_scene_option_two + "\n\n3)" + this_scene_option_three
  trial_var = input(this_scene_concat)
  # Error check the input - if anything other than 1, 2, or 3, load same scene again
  if trial_var == "1":
    load_next_scene(int(this_scene_option_one_redirect))
  elif trial_var == "2":
    load_next_scene(int(this_scene_option_two_redirect))
  elif trial_var == "3":
    load_next_scene(int(this_scene_option_three_redirect))
  # This is an escape key, after a fashion, but needs a proper solution, rather than just asking it to do something it can't do...
  elif trial_var == "q":
    load_next_scene(100)
  else:
    load_next_scene(scene_number)
  return 

    
def create_player(player_choice_of_class):
  index_choice = int(player_choice_of_class) - 1
  init_player_class = startup_stats[index_choice][0]
  init_time_factor = startup_stats[index_choice][1]
  init_stamina = startup_stats[index_choice][2]
  init_max_stamina = startup_stats[index_choice][3]
  init_patience = startup_stats[index_choice][4]
  init_max_patience = startup_stats[index_choice][5]
  init_money = startup_stats[index_choice][6]
  # Create player as "new_player" with start-up data as drawn from startup stats list
  new_player = Player(init_player_class, init_time_factor, init_stamina, init_max_stamina, init_patience, init_max_patience, init_money)
  return new_player

  
# Shows character's current stats as a running item
def display_stats(player):
    stats = "Time Remaining: " + str(player.time_remaining) + "\n" + "Stamina: " + str(player.stamina) + "/" + str(player.max_stamina) + "\n" + "Patience: " + str(player.patience) + "/" + str(player.max_patience) + "\n" + "Money: £" + str(player.money) +"\n\n"
    return stats
   
# ################################# GAME LOOP ########################

# Ask player which player_class they want to play with

clear_console()
player_choice_of_class = input(start_up_message)
#print(player_choice_of_class)
player = create_player(player_choice_of_class)
#test_player = Player("Mum with kids", 0.8, 120, 120, 70, 70, 100)
clear_console()
#print(player)
#print(display_stats(player))

#Load first scene
load_next_scene(1)