def action(cmd):
    print('start ' + cmd)
    while 1:
        received = input()
        if received == 'succeeded ' + cmd:
            return True
        elif 'failed ' in received:
            return False
        elif 'error' in received:
            return False
