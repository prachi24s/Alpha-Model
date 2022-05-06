from action_execution import *

def enableIcon(action_name, act, location, message, default):
     action(f'EnableIcon("{action_name}", {act}, {location}, "{message}", {default})')
