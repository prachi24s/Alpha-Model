from action_execution import *


def create_item(name, item):
     action('CreateItem(' + name + ' ,' + item + ')')

def set_position(name, Position):
    action('SetPosition(' + name + ',' + Position + ')')

def take_item(item, char, Position):
	action('Take('+ char +', '+ item +', '+ Position +')')

def give_item(item, char1, char2):
	action('Give('+ char1 +', '+ item +', '+ char2 +')')
