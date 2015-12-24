def words_collide(words):
    '''Slam two words together and the one with most remaining is the winner'''
    #words = <1st word> <2nd word>
    first, second = words.split()
    remove = []
    for x in first:
        if x in second:
            idx = second.index(x)
            remove.append(x)
            second = second[:idx] + second[idx+1:]
    for y in remove:
        idx = first.index(y)
        first = first[:idx] + first[idx+1:]
    if len(first) > len(second):
        winner = 'First'
        loser = second
    elif len(first) < len(second):
        winner = 'Second'
        loser = first
    else:
        return 'It\'s a tie!\nLetters left:\n First: %s\n Second: %s'%(first,second)
    return '%s word wins at %s to %s!\nLetters left:\n First: %s\n Second: %s'%(winner, len(eval(winner.lower())),len(loser),first,second)

#print(words_collide('Hello Hello'))

if __name__ == '__main__':
    while True:
        print(words_collide(input('The fighting words!\n'))+'\n')
