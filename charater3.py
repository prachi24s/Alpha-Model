def talktolily(character1, character2):
     character_walk(character1, character2)
     set_right(character1)
     set_left(character2)
     set_dialog('Lily: You found the key...I want it..just give it to me otherwise it will not be good for you.')
     set_dialog('Kate: No.. I cant give it to you.')
     set_dialog('Lily: Okay! Lets see...\\n[ Attack | Attack]')
     show_dialog()
     while 1:
         if 'Attack' in input():
            select ='Attack'
            break
     if select == 'Attack':
        hide_dialog()
        draw('Kate', 'Sword')
        draw('Lily', 'lily_sword')
        character_attack('Lily', 'Kate')
        character_attack('Kate', 'Lily')
        character_attack('Kate', 'Lily')
        character_attack_success('Kate', 'Lily')
        die_character('Lily')
        pocket('Kate', 'Sword')


def talktokim( character1, character2):
    character_walk(character1, character2)
    set_right(character1)
    set_left(character2)
    set_dialog('Kim: Who are you?')
    set_dialog('Kate: I am Kate')
    set_dialog('Kim: why did you come here ?')
    set_dialog('Kate: I need your help....')
    set_dialog('Kim:  What help do you need ?')
    set_dialog('Kate: I need direction of a place for that I need Campass can you please give me campass')
    set_dialog('Kim:  ok..I will help you..here is the compass\\n[continue | continue]')
    show_dialog()
    while 1:
        if 'continue' in input():
           select ='continue'
           break
    if select == 'continue':
        hide_dialog()
        take_item('Kim', 'Compass', 'Tavern.RoundTable' )
        give_item('Compass', 'Kim', 'Kate')
        action('AddToList(Compass, "Compass for getting direction")')
        pocket('Kate', 'Compass')
