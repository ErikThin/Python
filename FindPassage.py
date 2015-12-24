#find = "rugged Russian bear"

def find_passage(text, find):
    act = ''
    scene = ''
    actor = ''
    actor_log = []
    passage = ''
    for line in text:
        if line.startswith('ACT'):          #Logs what act it is in
            act = line[:line.index('.')]
        if line.startswith('SCENE'):
            scene = line[:line.index('.')]  #Logs what scene it is in
            actor_log = []
        if line.startswith(' '*2) and not line[2] == ' ':
            actor = line[2:-2]              #Logs current actor
            if not actor in actor_log:
                actor_log.append(actor)
        if line[:4] == ' '*4: #or line.startswith('['):
            passage = passage + line        #'If' evals to true when within passage, therefore the full passage is logged
        elif find in passage:               #Evals at end of passage
            for extra in text:
                if not extra.startswith('SCENE') or extra.startswith('ACT'):
                    if extra.startswith(' '*2) and not extra[2] == ' ':
                        actor = extra[2:-2]
                        if not actor in actor_log:
                            actor_log.append(actor)
                else:
                    break
            temp = ', '.join(actor_log) #list of actors
            temp = 'Actors: ' + temp
            quote = '%s\n%s\n%s\nSpoken by %s:\n%s'%(act, scene, temp, actor, passage) #formats output
            return quote
        else:
            passage = ''
    return 'No results.'


if __name__ == '__main__':
    while True:
        text = open("macbeth.txt")
        find = input('Input phrase: ')
        print(find_passage(text, find))
        text.close()

    text.close()

