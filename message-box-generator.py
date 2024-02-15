import wcwidth
import os
import platform

def get_display_width(string):
    total_width = 0
    for char in string:
        width = wcwidth.wcwidth(char)
        if width == -1:
            width = 0
        total_width += width
    return total_width

dialogue1 = 'person1_dialogue'
dialogue2 = 'person2_dialogue'
systemMessage = 'system_event'
bubble = 'bubble'
def printBox(singleLineString,type):
    if str(type).lower() == bubble:
        singleLineString = str(singleLineString)
        localStringLength = get_display_width(singleLineString)
        new_input = ""
        spaces = 0
        spacesTotal = 0

        for i, letter in enumerate(singleLineString):
            width = wcwidth.wcwidth(letter)
            if width == -1:
                width = 0

            if letter == ' ':
                spacesTotal += 1
                spaces += 1
                if spaces == 9:
                    new_input += '\n'
                    spaces = 0
                else:
                    new_input += letter
            elif letter == '\n':
                new_input += ' '
                spaces += 1
                if spaces == 9:
                    new_input += '\n'
                    spaces = 0
            else:
                new_input += letter

        localStringArray = new_input.split('\n')
        if spacesTotal <9:
            spce = 0
            jing = ''
            for ii, object1 in enumerate(localStringArray):
                for iii, char in enumerate(object1):
                    if char == ' ':
                        spce += 1
                objLen = get_display_width(object1)
                if objLen > 59 and spce <= 7:
                    firstCharCheck = True
                    for iiii, char in enumerate(object1):
                        if iiii % 61 == 0 and not firstCharCheck:
                            jing = jing + char + '\n'
                        else:
                            jing = jing + char
                        
                        if firstCharCheck:
                            firstCharCheck = False
                else:
                    jing = jing + object1
            localStringArray = jing.split('\n')
        maxLineLength = max(get_display_width(line) for line in localStringArray)
        bht = ''

        for index, line in enumerate(localStringArray):
            fillLength = maxLineLength - get_display_width(line)
            filler = ' ' * fillLength
            line = ' │' + line + filler + '│\n'
            bht += line

        localTop = '─' * maxLineLength
        if get_display_width(localTop) > maxLineLength:
            localTop = localTop.replace('─', '', get_display_width(localTop) - maxLineLength)

        print('\n ╭' + localTop + '╮\n' + bht + ' ╰' + localTop + '╯')
    elif str(type).lower() == dialogue1:
        singleLineString = str(singleLineString)
        localStringLength = get_display_width(singleLineString)
        new_input = ""
        spaces = 0
        spacesTotal = 0

        for i, letter in enumerate(singleLineString):
            width = wcwidth.wcwidth(letter)
            if width == -1:
                width = 0

            if letter == ' ':
                spaces += 1
                spacesTotal += 1
                if spaces == 9:
                    new_input += '\n'
                    spaces = 0
                else:
                    new_input += letter
            elif letter == '\n':
                new_input += ' '
                spaces += 1
                if spaces == 9:
                    new_input += '\n'
                    spaces = 0
            else:
                new_input += letter

        localStringArray = new_input.split('\n')
        if spacesTotal <9:
            spce = 0
            jing = ''
            for ii, object1 in enumerate(localStringArray):
                for iii, char in enumerate(object1):
                    if char == ' ':
                        spce += 1
                objLen = get_display_width(object1)
                if objLen > 59 and spce <= 7:
                    firstCharCheck = True
                    for iiii, char in enumerate(object1):
                        if iiii % 61 == 0 and not firstCharCheck:
                            jing = jing + char + '\n'
                        else:
                            jing = jing + char
                        
                        if firstCharCheck:
                            firstCharCheck = False
                else:
                    jing = jing + object1
            localStringArray = jing.split('\n')
        maxLineLength = max(get_display_width(line) for line in localStringArray)
        bht = ''

        for index, line in enumerate(localStringArray):
            fillLength = maxLineLength - get_display_width(line)
            filler = ' ' * fillLength
            line = ' │' + line + filler + '│\n'
            bht += line

        localTop = '─' * maxLineLength
        if get_display_width(localTop) > maxLineLength:
            localTop = localTop.replace('─', '', get_display_width(localTop) - maxLineLength)

        print('\n ┌' + localTop + '┐\n' + bht + ' └' + localTop + '┴┐')
    elif str(type).lower() == dialogue2:
        singleLineString = str(singleLineString)
        localStringLength = get_display_width(singleLineString)
        new_input = ""
        spaces = 0
        spacesTotal = 0

        for i, letter in enumerate(singleLineString):
            width = wcwidth.wcwidth(letter)
            if width == -1:
                width = 0

            if letter == ' ':
                spaces += 1
                spacesTotal += 1
                if spaces == 9:
                    new_input += '\n'
                    spaces = 0
                else:
                    new_input += letter
            elif letter == '\n':
                new_input += ' '
                spaces += 1
                if spaces == 9:
                    new_input += '\n'
                    spaces = 0
            else:
                new_input += letter

        localStringArray = new_input.split('\n')
        if spacesTotal <9:
            spce = 0
            jing = ''
            for ii, object1 in enumerate(localStringArray):
                for iii, char in enumerate(object1):
                    if char == ' ':
                        spce += 1
                objLen = get_display_width(object1)
                if objLen > 59 and spce <= 7:
                    firstCharCheck = True
                    for iiii, char in enumerate(object1):
                        if iiii % 61 == 0 and not firstCharCheck:
                            jing = jing + char + '\n'
                        else:
                            jing = jing + char
                        
                        if firstCharCheck:
                            firstCharCheck = False
                else:
                    jing = jing + object1
            localStringArray = jing.split('\n')
        maxLineLength = max(get_display_width(line) for line in localStringArray)
        bht = ''

        for index, line in enumerate(localStringArray):
            fillLength = maxLineLength - get_display_width(line)
            filler = ' ' * fillLength
            line = ' │' + line + filler + '│\n'
            bht += line

        localTop = '─' * maxLineLength
        if get_display_width(localTop) > maxLineLength:
            localTop = localTop.replace('─', '', get_display_width(localTop) - maxLineLength)

        print('\n ┌' + localTop + '┐\n' + bht + '┌┴' + localTop + '┘')
    elif str(type).lower() == systemMessage:
        singleLineString = str(singleLineString)
        localStringLength = get_display_width(singleLineString)
        new_input = ""
        spaces = 0
        spacesTotal = 0

        for i, letter in enumerate(singleLineString):
            width = wcwidth.wcwidth(letter)
            if width == -1:
                width = 0

            if letter == ' ':
                spaces += 1
                spacesTotal += 1
                if spaces == 9:
                    new_input += '\n'
                    spaces = 0
                else:
                    new_input += letter
            elif letter == '\n':
                new_input += ' '
                spaces += 1
                if spaces == 9:
                    new_input += '\n'
                    spaces = 0
            else:
                new_input += letter

        localStringArray = new_input.split('\n')
        if spacesTotal <9:
            spce = 0
            jing = ''
            for ii, object1 in enumerate(localStringArray):
                for iii, char in enumerate(object1):
                    if char == ' ':
                        spce += 1
                objLen = get_display_width(object1)
                if objLen > 59 and spce <= 7:
                    firstCharCheck = True
                    for iiii, char in enumerate(object1):
                        if iiii % 61 == 0 and not firstCharCheck:
                            jing = jing + char + '\n'
                        else:
                            jing = jing + char
                        
                        if firstCharCheck:
                            firstCharCheck = False
                else:
                    jing = jing + object1
            localStringArray = jing.split('\n')
        maxLineLength = max(get_display_width(line) for line in localStringArray)
        bht = ''

        for index, line in enumerate(localStringArray):
            fillLength = maxLineLength - get_display_width(line)
            filler = ' ' * fillLength
            line = ' ' + line + filler + '\n' #│
            bht += line

        localTop = '═' * maxLineLength

        singleLineString = str(singleLineString)
        localStringLength = len(singleLineString)
        print('\n '+localTop+'\n'+bht+' '+localTop+'\n')

a=0
while a<1:
    print('String Boxifier || Made by Arson')
    inp = str(input('\nEnter a string to boxify:\n\n'))

    print('\n')
    b=0
    while b<1:
        boxType = str(input('\nBox style options:\n1) person1_dialogue\n2) person2_dialogue\n3) system_event\n4) bubble\n\nType a number to select a box type\n'))
        if str(boxType) != '1' and str(boxType) != '2' and str(boxType) != '3' and str(boxType) != '4':
            printBox('Invalid Value',systemMessage)
        else:
            if boxType == '1':
                boxType = 'person1_dialogue'
            elif boxType == '2':
                boxType = 'person2_dialogue'
            elif boxType == '3':
                boxType = 'system_event'
            else:
                boxType = 'bubble'
            break
    print('\n')
    printBox(inp,boxType)

    input('\n\nPress ENTER to boxify another string ')

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')