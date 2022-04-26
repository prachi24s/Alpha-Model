def check_for_success(command):
	while True:
		received = input()
		if received == 'succeeded ' + command:
			return True
		elif received.startswith('failed ' + command):
			return False
		elif received.startswith('error'):
			return False

def action(command):
	print('start ' + command, flush=True)
	return check_for_success(command)

def waitForChoice(choices_list):
	while True:
		dialog_input = input().strip()
		for c in choices_list:
			if c in dialog_input:
				return c

def Leave(character, place_from, place_to, fade_in = True, fade_out = True):
    action(f'Exit({character.name}, {place_from}, {fade_in})')
    action(f'Enter({character.name}, {place_to}, {fade_out})')

def Open(character, furniture_name):
    action(f'OpenFurniture({character.name}, {furniture_name})')

def Close(character, entity_name):
    action(f'CloseFurniture({character.name}, {entity_name})')

def Take(character, item, position_name):
	action(f'Take({character.name}, {item.item_name}, {position_name})')

def Give(character_from, item, character_to):
	action(f'Give({character_from.name}, {item.item_name}, {character_to.name})')

def Fight(character_win, character_lose):
	action(f'Attack({character_win.name}, {character_lose.name}, false)')
	action(f'Attack({character_lose.name}, {character_win.name}, false)')
	action(f'Attack({character_win.name}, {character_lose.name}, true)')

def Put(character, item, place):
    action(f'Put({character.name},{item.item_name},{place})')


def Die(character):
    action(f'Die({character.name}')
    
def pocket(char, item):
    action(f'Pocket({char.name}, {item.item_name}')
    
def sit(character, place):
    action(f'Sit({character.name}, {place}')
    
def drink(character):
    action(f'Drink({character.name}))')

