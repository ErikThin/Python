#Prints Don't stop believing lyrics with as little lines of code as possible
import time

def sing(words):
    """
    [list] --> None
    Prints each element of list, followed by a newline.
    """
    for x in words:
        print (x)
    print ()
cho = ['Strangers waiting','Up and down the boulevard','Their shadows searching in the night','Streetlights, people','Living just to find emotion',
              'Hiding somewhere in the night']
verse1 = ["Just a small town girl","Livin' in a lonely world","She took the midnight train goin' anywhere","Just a city boy","Born and raised in south Detroit",
          "He took the midnight train goin' anywhere"]

verse2 = ["A singer in a smoky room","A smell of wine and cheap perfume","For a smile they can share the night","It goes on and on, and on, and on"]

verse3 = ["Working hard to get my fill","Everybody wants a thrill","Payin' anything to roll the dice","Just one more time","Some will win, some will lose",
          "Some were born to sing the blues","Oh, the movie never ends","It goes on and on, and on, and on"]
end = ["Don't stop believin'","Hold on to the feelin'","Streetlights, people"]


if __name__ == '__main__':
    for x in [verse1, verse2, cho, verse3, cho, end, [end[0],end[1][:7],end[2]], end]:
        sing(x)
        time.sleep(3)
    input()
