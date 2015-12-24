FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def number_repr(num):
    number = abs(num)
    """Returns a string repr number (-999 -> 999)"""
    string = ''
    if num < 0:
        string += 'negetive '
    if number > 99:
        string += "%s %s"%(FIRST_TEN[(number//100)-1], HUNDRED)
    if number%100 > 19:
        string += "%s%s"%(('',' ')[number>99], OTHER_TENS[((number%100)//10)-2])
    elif 9 < number%100 < 20:
        string += "%s%s"%(('',' ')[number>99], SECOND_TEN[(number%100)-10])
        return string
    if number%10 > 0:
        string += "%s%s"%(('',' ')[number>20], FIRST_TEN[(number%10)-1])
    if len(string) == 0:
        return 'zero'
    return string

if __name__ == '__main__':
    print ("This program takes a number and prints it in words.")
    print ("Accepted numbers are from -999 to 999.")
    print ()
    while True:
        number = input("Number (-999 -> 999) {'exit' to quit}: ")
        if number.lower() == 'exit':
            print("Leaving...")
            break
        try:
            print("In words:", number_repr(int(number)))
            print('_'*20)
            print()
        except:
            print("Number (-999 -> 999) or the word 'exit', please.")
            print('_'*20)
            print()
