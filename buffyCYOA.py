# This is a Buffy-themed choose you own adventure game.


import pyinputplus as pyip, os


# TODO: check if this function is really necessary.
# TODO: remove '\n' from game over and ending text that gets displayed.
# TODO: check grammar, vocab and punctuation.
def blank_line():
    input('...')


def input_choice(reply):
    # have to use 'and' operator here instead of 'or'. Otherwise it will keep
    # equating to true and therefore have a never ending loop. The loop will exit when the condition
    # equates to false.
    while reply != 'A' and reply != 'B':
        reply = input('A or B? ').upper()
    return reply


def play_or_quit():
    reply = pyip.inputYesNo('\nWould you like to play again? ')
    if reply == 'no':
        return True
    else:
        # file.close()
        global alt_path
        alt_path = 0


def player_file():
    file.write('\nQuestion: ' + question)
    file.write('\nAnswer: ' + choice)


def filename_exist(folder):
    number = 1
    while True:
        check_name = os.path.basename(folder) + '_' + str(number) + '.txt'
        if not os.path.exists(folder + '\\' + check_name):
            break
        number = number + 1
    return check_name


path = 'C:\\buffyFiles'
if not os.path.exists(path):
    os.mkdir('C:\\buffyFiles')
filename = filename_exist(path)
# Creates file that keeps track of questions, choices and endings.
file = open(path + '\\' + filename, 'w')

welcome = """
                        _            __  __       
                        | |          / _|/ _|      
                        | |__  _   _| |_| |_ _   _ 
                        | '_ \| | | |  _|  _| | | |
                        | |_) | |_| | | | | | |_| |
                        |_.__/ \__,_|_| |_|  \__, |
                                              __/ |
                                             |___/ 

        Welcome to Buffy The Vampire Slayer: Choose Your Own Adventure!
        """
print(welcome)
file.write(welcome)
# user-info
name = pyip.inputStr(prompt='What is your first name? ', blockRegexes=[r'[^A-Za-z]+'])
age = pyip.inputInt(prompt='What is your age? ', min=0)
file.write(f'\nPlayer: {name}     Age: {age}\n')

# certain items can save the player from death or perhaps make them stronger. In this case a necklace from Giles.
inventory_slayer = []

# The game loop, only exits (break) when player chooses to not replay the game.
# alt_path to check whether player picked up an item (necklace) before 
# if player has necklace in inventory, first choice will be skipped to avoid repeating same scenario. 
alt_path = 0
while True:
    if alt_path != 1:
        print(f'\nYou are {name} Summers, the vampire slayer.')
        blank_line()

        print('Even though you take your destiny seriously, '
              'sometimes you just want to hang out with your friends and be a regular teenager.')
        blank_line()
        question = 'Are you going to patrol at the cemetery like you watcher asked you to (A) or chill ' \
                   'at the Bronze (B)?'
        print(question)
        choice = input_choice('')
        player_file()

    if choice.upper() == 'A' or alt_path == 1:
        print('\nAt the cemetery you are bored out of your mind.')
        blank_line()
        print('At least you feel like you are doing something useful, instead of just partying.')
        blank_line()
        print('Your slayer instinct kicks in, and you feel like you should check out the Mausoleum.')
        blank_line()
        question = 'Are you staying where you are right now like you promised your watcher (A), or are you going to ' \
                   'investigate (B)?'
        print(question)
        choice = input_choice('')
        player_file()

        if choice.upper() == 'A':
            print('\nYou decide to stay and walk around, kinda hoping that a vampire will show up.')
            blank_line()
            print('Suddenly you feel the flesh on your back melting...')
            blank_line()
            print('Before you can scream, everything turns black...')
            blank_line()
            print('\nGAME OVER')
            file.write('\nGAME OVER')
            input()
            if play_or_quit():
                break

        elif choice.upper() == 'B':
            print('\nYou trust Giles, but you trust yourself more.')
            blank_line()
            print('You are almost at the entrance of the Mausoleum.')
            blank_line()
            print('Something is not right...')
            blank_line()
            question = 'Are you going to sneak in (A) or wait outside in the bushes (B)?'
            print(question)
            choice = input_choice('')
            player_file()

            if choice.upper() == 'A':
                print('\nYou do not want to take any risks and decide to find a silent way in.')
                blank_line()
                print('At the right of the mausoleum you spot a small hole.')
                blank_line()
                question = 'Are you going to climb through the hole (A) or try to look through it(B)?'
                print(question)
                choice = input_choice('')
                player_file()

                if choice.upper() == 'A':
                    print('\nYou cannot help but smile at the thought of surprising whoever is inside.')
                    blank_line()
                    print('Very...slowly... you try to squeeze yourself through the hole.')
                    blank_line()
                    print('Emphasis on TRYING. You vastly overestimated the size of that damn hole.')
                    blank_line()
                    print('you keep pulling and pulling and eventually you fall into the mausoleum.')
                    blank_line()
                    print('Unfortunately, your fall made quite some noise. Your instincts go haywire.')
                    blank_line()
                    print('Before you are able to prepare yourself, you feel an intense heat.')
                    blank_line()
                    print('And then NOTHING.')
                    print('\nGAME OVER')
                    file.write('\nGAME OVER')
                    input()
                    if play_or_quit():
                        break

                elif choice.upper() == 'B':
                    print('\nYou slowly get closer to the hole.')
                    blank_line()
                    print('You look through the hole, but it its quite dark.')
                    blank_line()
                    print('But then you notice a figure who is crouching over some books.')
                    blank_line()
                    print('A faint red light makes the outlines of his figure visible.')
                    blank_line()
                    print('Suddenly the mysterious guy stands up.')
                    blank_line()
                    print('Your heart jumps, but you are pretty sure he has not spotted you (yet).')
                    blank_line()
                    question = 'Are you going to continue to look through the hole (A) or ' \
                               'try to find a way inside (B)?'
                    print(question)
                    choice = input_choice('')
                    player_file()

                    if choice.upper() == 'A':
                        print('\nBefore you can blink, the mysterious figure looks straight at you.')
                        blank_line()
                        print('You feel an enormous heat, and then... you vanish.')
                        blank_line()
                        print('Like they say...')
                        blank_line()
                        print('Curiosity killed the cat...')
                        blank_line()
                        print('GAME OVER')
                        file.write('\nGAME OVER')
                        input()
                        if play_or_quit():
                            break

                    elif choice.upper() == 'B':
                        print('\nYou slowly back away, and try to find an alternative way in.')
                        blank_line()
                        print('You climb on top of the Mausoleum, trying to be as silent as you can.')
                        blank_line()
                        print('what a coincidence, another hole, but this time it is a lot bigger.')
                        blank_line()
                        print('You make your way inside. it is time to come up with a plan.')
                        blank_line()
                        question = 'Are you going for a sudden and vicious attack (A) or a silent kill (B)?'
                        print(question)
                        choice = input_choice('')
                        player_file()

                        if choice.upper() == 'A':
                            print('\nYou have already wasted enough time, and decide to make it quick.')
                            blank_line()
                            print('You try to orientate yourself and realize the figure is around the corner.')
                            blank_line()
                            print('you reach for your stake and focus all of your energy.')
                            blank_line()
                            print('It is showtime!')
                            blank_line()
                            print('You run towards the corner and make a sharp turn to the right.')
                            blank_line()
                            print('The figure turns out to be a nerdy vampire, with glasses and an X-men shirt.')
                            blank_line()
                            question = 'Are you going to kick him in the face (A) or right in the groin (B)?'
                            print(question)
                            choice = input_choice('')
                            player_file()

                            if choice.upper() == 'A':
                                print('\nWithout thinking twice, you kick him right in his face.')
                                blank_line()
                                print('His glasses shatters on the floor and the vampire '
                                      'squeezes his eyes out of agony.')
                                blank_line()
                                question = 'Are you going to stake him (A) or torture him for information first (B)?'
                                print(question)
                                choice = input_choice('')
                                player_file()

                                if choice.upper() == 'A':
                                    print('\nYou immediately stake him right in the heart.')
                                    blank_line()
                                    print('After a second only red ashes are left.')
                                    blank_line()
                                    print('Weird, looks like you will never find out the reason for this odd color.')
                                    blank_line()
                                    print('Guess it is time to hit the Bronze after all.')
                                    blank_line()
                                    print('\nTHE END | ENDING C')
                                    file.write('\nENDING C')
                                    input()
                                    if play_or_quit():
                                        break

                                elif choice.upper() == 'B':
                                    print('\nYou grab him by his shirt and toss him on the ground.')
                                    blank_line()
                                    print('You ask: \"What are you doing here mister?\"')
                                    blank_line()
                                    print('He gives you a sinister smile.')
                                    blank_line()
                                    print('He says: \"My destiny...\"')
                                    blank_line()
                                    print('Before you can reply with a catchphrase,everything turns bright red.')
                                    blank_line()
                                    print('You scream for mere seconds, but it feels like minutes while your '
                                          'face burns off...')
                                    print('GAME OVER')
                                    file.write('\nGAME OVER')
                                    input()
                                    if play_or_quit():
                                        break
                            elif choice.upper() == 'B':
                                print('\nThis will teach it.')
                                blank_line()
                                print('Unfortunately for you, it looks like he is prepared.')
                                blank_line()
                                print('Even vampires protect their jewels at all costs.')
                                blank_line()
                                print('He grabs your leg and throws you on your back.')
                                blank_line()
                                print('You try to get back up, but he kicks you in the face.')
                                blank_line()
                                print('He slowly removes his glasses and stares right at you.')
                                blank_line()
                                print('Calmly he says: \"No one can stop my destiny.\"')
                                blank_line()
                                # If player has necklace in their inventory they will be saved from their death
                                if 'necklace' in inventory_slayer:
                                    print('Freaking laser eyes erupt from his eyes.')
                                    blank_line()
                                    print('You instantly close your eyes ,hoping the painful process of dying '
                                          'will not last long.')
                                    blank_line()
                                    print('You always knew life as a slayer would not last long.')
                                    blank_line()
                                    print(f'It has been a pretty good {age} year run.')
                                    blank_line()
                                    print('A huge scream breaks the silence, but it is not yours!')
                                    blank_line()
                                    print('You open your eyes only to see that the laser is being reflected by your'
                                          ' over-the-top necklace! Right back to the vamps stomach.')
                                    blank_line()
                                    print('Not willing to take any chances, you throw one of your lovely stakes'
                                          ' at his heart for good measure.')
                                    blank_line()
                                    print('The screaming stops and only a pile of RED ashes remains.')
                                    blank_line()
                                    print('You are too shaken up to wonder about the weird color. Time to go home. '
                                          'You are no longer in the mood to hang out with your friends.')
                                    blank_line()
                                    print('\nTHE END | ENDING ALT A')
                                    file.write('\nENDING ALT A')
                                    if play_or_quit():
                                        break
                                else:
                                    print('Laser beams from his eyes start to burn in your stomach.')
                                    blank_line()
                                    print('Your eyes roll back and in seconds your short life flashes'
                                          ' before your eyes.')
                                    blank_line()
                                    print(f'You are just a {age} year old.')
                                    blank_line()
                                    print(f'You WERE just a {age} year old.')
                                    blank_line()
                                    print('GAME OVER')
                                    file.write('\nGAME OVER')
                                    input()
                                    if play_or_quit():
                                        break

                        elif choice.upper() == 'B':
                            print('\nYou can be silent AND a badass...')
                            blank_line()
                            print('With small steps, while being hyper aware of your environment, '
                                  'you explore the area.')
                            blank_line()
                            print('BANG')
                            blank_line()
                            print('A loud noise comes from around the corner. You freeze and try to breathe as '
                                  'silently as you can.')
                            blank_line()
                            print('Suddenly you hear a man (slayer instincts scream vamp) talking to himself while'
                                  ' shuffling something.')
                            blank_line()
                            question = 'Are you going to overhear him (A) or sneak up behind him for the KILL (B)?'
                            print(question)
                            choice = input_choice('')
                            player_file()

                            if choice.upper() == 'A':
                                print('\nYou decide to wait until you get some intel before you kill him.')
                                blank_line()
                                print('You peek a little bit around the corner and see '
                                      ' a vampire shuffling X-men comics.')
                                blank_line()
                                print('It seems the comics fell of an alter on which a huge picture of James Marsden'
                                      ' is displayed.')
                                blank_line()
                                print('You are too surprised to roll your eyes at this bizarre event.')
                                blank_line()
                                print('The vampire growls when he notices one of the candles on the altar are not lit'
                                      ' anymore.')
                                blank_line()
                                print('Just when you are about to stop peeking you see that the vampire lit the candle'
                                      ' with his freaking LASER eyes!!!')
                                blank_line()
                                question = 'Are you going to kill him in a sneak attack (A) or retreat ' \
                                           'back to Giles with this intel (B)?'
                                print(question)
                                choice = input_choice('')
                                player_file()

                                if choice.upper() == 'A':
                                    print('\nAlmost as an cat you silently find your way behind the vamps back.')
                                    blank_line()
                                    print('The vampire is still sorting out the correct order of the comics'
                                          ' on the ground.')
                                    blank_line()
                                    print('He seemingly has no idea of what is about to happen.')
                                    blank_line()
                                    print('Without any further hesitation you stake him in the back.')
                                    blank_line()
                                    print('With a mighty scream and a second of laser eyes he dissolves into RED dust.')
                                    blank_line()
                                    print('Weird... Guess you will never find out the reason for this odd color.')
                                    blank_line()
                                    print('Unless it has something to do with his X-men obsession?')
                                    blank_line()
                                    print('Oh well, looks like you can chill at the Bronze after all.')
                                    blank_line()
                                    print('THE END | ENDING B')
                                    file.write('\nENDING B')
                                    input()
                                    if play_or_quit():
                                        break

                                elif choice.upper() == 'B':
                                    print('\nTrying to kill a vamp with lasers eyes does not sound '
                                          'like a good time to you.')
                                    blank_line()
                                    print('Besides, it would not hurt to ask your watcher without any fashion'
                                          ' sense for some advice.')
                                    blank_line()
                                    print('Retreat it is.')
                                    blank_line()
                                    print('You slowly back away.')
                                    blank_line()
                                    print('Out of nowhere the undead geek starts laughing.')
                                    blank_line()
                                    print('He rambles about some kind of destiny that will be fulfilled tomorrow.')
                                    blank_line()
                                    print('You do not want to risk him smelling you, so you back away faster'
                                          ' and eventually make your way outside.')
                                    blank_line()
                                    print('You look over your shoulder to make sure he has not followed you.')
                                    blank_line()
                                    print('NOTHING.')
                                    blank_line()
                                    print('Relieved you walk towards the main gate.')
                                    blank_line()
                                    print('Hopefully Giles has the info you need.')
                                    blank_line()
                                    print('The last thing Sunnydale needs is a cult of laser-eyes-vampire nerds.')
                                    blank_line()
                                    print('TO BE CONTINUED.| ENDING A')
                                    file.write('\nTO BE CONTINUED.| ENDING A')
                                    input()
                                    if play_or_quit():
                                        break

                            elif choice.upper() == 'B':
                                print('\nAlmost as an cat you silently find your way behind the vamps back.')
                                blank_line()
                                print('You take a glimpse at what he is shuffling: comic books.')
                                blank_line()
                                print('The vampire is seemingly trying to sort them chronologically.')
                                blank_line()
                                print('It sure looks like he has no idea of what is about to happen.')
                                blank_line()
                                print('Without any further hesitation you stake him in the back.')
                                blank_line()
                                print('With a mighty scream and a beaming red light he dissolves into RED dust.')
                                blank_line()
                                print('WHAT THE HELL!?')
                                blank_line()
                                print('Weird, guess you will never find out the reason for this odd color.')
                                blank_line()
                                print('Oh well, time to show your best moves at the Bronze.')
                                blank_line()
                                print('THE END | ENDING D')
                                file.write('\nENDING D')
                                input()
                                if play_or_quit():
                                    break

            elif choice.upper() == 'B':
                print('\nWhatever of whoever is inside should eventually come out....Right?')
                blank_line()
                print('You sit in the center of the biggest bush you could find and try to make yourself '
                      'somewhat comfortable.')
                blank_line()
                print('A few minutes pass...')
                blank_line()
                print('You suddenly feel something crawling at the back of you neck.')
                blank_line()
                print('It cannot be...')
                blank_line()
                print('A freaking spider!!!')
                blank_line()
                print('You jump up and down while screaming hysterically.')
                blank_line()
                print('Suddenly a faint red light catches your eyes.')
                blank_line()
                print('In front of the mausoleum a figure with bright red eyes stares right at you.')
                blank_line()
                # If player has necklace in their inventory they will be saved from their death
                if 'necklace' in inventory_slayer:
                    print('You have no idea why they are red, but you do know it probably has nothing to do with'
                          ' the latest beauty trends.')
                    blank_line()
                    print('You realize you have no time to get into cover.')
                    blank_line()
                    print('As if the eyes were not creepy enough, the figure comes closer and reveals not only a smile'
                          ' but also the classic pointy fangs.')
                    blank_line()
                    print('Oh and now you feel an intense heat, as if the air is being put on fire.')
                    blank_line()
                    print(f'Looks like that is a wrap for {name} the vampire slayer...')
                    blank_line()
                    print('The vampire laughs, not even having the decency of explaining his evil plan to you.')
                    blank_line()
                    print('Oh but it gets even worse!')
                    blank_line()
                    print('FREAKING LASER EYES ERUPT FROM HIS EYES!')
                    blank_line()
                    print('The rude bastard does not even give you the chance to scream.')
                    blank_line()
                    print('Instead he does the screaming for you!')
                    blank_line()
                    print('Your tacky necklace reflects his attack right back at him.')
                    blank_line()
                    print('In the blink of an eye only a pile of RED ashes remains.')
                    blank_line()
                    print('You are not sure if you are more shocked about the events that have just transpired or'
                          ' the realization that you did not get the opportunity to make a pun.')
                    blank_line()
                    print('Either way, you head back home, promising yourself to never take off the ugly necklace.')
                    blank_line()
                    print('THE END | ENDING ALT B')
                    file.write('\nENDING ALT B')
                    if play_or_quit():
                        break
                else:
                    print('Before you can get into cover, you feel an intense heat.')
                    blank_line()
                    print('You want to cry, but it is already to late.')
                    print('GAME OVER')
                    file.write('\nGAME OVER')
                    input()
                    if play_or_quit():
                        break

    elif choice.upper() == 'B':
        print('\n\'The Devil you Know (God is a Man)\' by Face to Face is playing while you enter the Bronze.')
        blank_line()
        print('You are wondering whether your \'sorta\' boyfriend Angel is going to show up.')
        blank_line()
        print('Before you can overthink your last conversation with him one of your best friends, Xander,'
              ' drags you to the dance floor.')
        blank_line()
        print('While you are are being dragged away, a nervous looking Giles at the balcony above you, '
              'is trying to get your attention by waving his arms frantically.')
        blank_line()
        question = 'Are you joining Xander on the dance floor (A) or will you go to Giles, your watcher (B)?'
        print(question)
        choice = input_choice('')
        player_file()

        if choice.upper() == 'A':
            print('You sign to Giles that you are going to catch up with him later and turn around before '
                  'you can see his disappointment, or well, anger.')
            blank_line()
            print('Shy Willow joins the group. Looking lost, but trying to show off some of her moves.')
            blank_line()
            print('Angel is a no show, however.')
            blank_line()
            print('Oh well, maybe he is too busy with brooding in the shadows again.')
            blank_line()
            print('A FEW HOURS LATER.')
            blank_line()
            print('The alarm clock has not even gone off yet.')
            blank_line()
            print('How weird is it then that you wake up because of the increase of daylight?')
            blank_line()
            print('Even more weird, is that you remember your curtains normally block all semblances of light.')
            blank_line()
            print('You get out of bed and walk towards the window.')
            blank_line()
            print('In just a few seconds the light has gotten even brighter and.... More red.')
            blank_line()
            print('Just before reaching for some sunglasses you feel a sharp hot pain.')
            blank_line()
            print('The last thing you SEE is your arms rapidly getting covered by big bright red blisters.')
            blank_line()
            print('The last thing you HEAR is your screams harmonizing with those of your mom and neighbours.')
            blank_line()
            print('GAME OVER')
            file.write('\nGAME OVER')
            if play_or_quit():
                break

        elif choice.upper() == 'B':
            print('Although the temptation to jump on the dance floor is Huge with a capital \'H\', you decide to '
                  'check in with Giles first.')
            blank_line()
            print('He immediately looks relieved.')
            blank_line()
            print('So relieved in fact, that he hands over a necklace with a gigantic diamond in the middle.')
            blank_line()
            print('WAIT WHAT!?')
            blank_line()
            print('Before you get the chance to get rid of the tacky thing, Giles explains you must wear it '
                  'during patrol tonight.')
            blank_line()
            print('Apparently one of his blue demon friends warned him that something big might happen soon.')
            blank_line()
            print('Lucky for him, you are already used to all that is vague...')
            blank_line()
            print('You wear the necklace and head to the cemetery.')
            inventory_slayer.append('necklace')
            file.write('\nITEM ADDED TO INVENTORY: NECKLACE.')
            alt_path = 1
            blank_line()
            continue

print('\nThank you for playing!')
print('''               
                     _____ _            _____          _ 
                    |_   _| |          |  ___|        | |
                      | | | |__   ___  | |__ _ __   __| |
                      | | | '_ \ / _ \ |  __| '_ \ / _` |
                      | | | | | |  __/ | |__| | | | (_| |
                      \_/ |_| |_|\___| \____/_| |_|\__,_|                             
''')
file.close()
input()
