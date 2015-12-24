#Reddit dailyprogrammer challenge #7 easy
#Morse code translator
#...---... SOS
#Bonus points for string to Morse code
#short mark, dot or "dit" (·) : "dot duration" is one time unit long
#longer mark, dash or "dah" (–) : three time units long
#inter-element gap between the dots and dashes within a character : one dot duration or one unit long
#short gap (between letters) : three time units long
#medium gap (between words) : seven time units long

MORSE = ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.', #for numbers from 0 to 9
         '.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..', #A - L
         '--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..'
         ]

def translate(code, mode='letter'):
    '''Default is morse to letters. Mode 'morse' to do the reverse'''
    if mode == 'letter':
        code_list = code.split()
        message = ''
        for x in code_list:
            if x == '/':
                message+=' '
            else:
                try:
                    idx = MORSE.index(x) #Find where the character is in the list
                except:
                    print('Error. Invalid character for mode: %s'%(x))
                    return 'Error. Invalid character for mode: %s'%(x)
                if idx < 10:
                    message+=str(idx)
                else:
                    message+=chr(idx+55)
    elif mode == 'morse':
        codeC = code.upper() #Make everything capitalized
        message = []
        for x in codeC:
            if x == ' ':
                message.append('/')
            else:
                if x.isnumeric():
                    message.append(MORSE[int(x)])
                else:
                    message.append(MORSE[int(ord(x))-55])
        message = ' '.join(message)
    else:
        message = 'Mode Error'
    print(message)

translate(".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--")
translate("SOS",'morse')
