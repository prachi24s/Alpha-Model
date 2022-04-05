import sys
def check_for_success(command):

    # Keep getting responces until the success of fail the given command is received
    while True:

        # Get response from Camelot
        received = input()

        # Return True if success response, else false for fail response
        if received == 'succeeded ' + command:
            return True
        elif received.startswith('failed ' + command):
            return False      
        


def action(command):
    print('start ' + command, flush=True)
    #sys.stdout.flush()
    # Call function to check for its success
    return check_for_success(command)

action('EnableInput()')
action('ShowMenu()')
action('HideMenu()')
action('CreateCharacter(james)')
action('SetClothing(james, peasant)')
action('SetExpression(james, Happy)')
action('SetHairStyle(james, Short)')
action('SetCameraFocus(james)')
action('CreatePlace(City, City)')
action('SetPosition(james, City)')



while(True):
    input()
