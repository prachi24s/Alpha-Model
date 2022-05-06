from action_execution import *

def set_dialog(dialog):
    action('SetDialog('+ dialog +')')

def set_right(character_name):
    action('SetRight('+ character_name +')')

def set_left(character_name):
   action('SetLeft('+ character_name +')')

def show_dialog():
    action('ShowDialog()')

def hide_dialog():
    action('HideDialog()')
