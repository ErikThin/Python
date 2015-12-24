def morse_clock(time_string):
    """
    Returns the binary form of time_string. 'HH:MM:SS'.
    """
    string = ['..','....','...','....','...','....']
    time = time_string.split(':')
    for z in range(len(time)):
        print (time[z])
        time[z] = (2-len(time[z]))*'0' + time[z]
    time = ''.join(time)
    print (time)
    for x in range(len(time)):
        temp = bin(int(time[x]))[2:]
        binary = (len(string[x])- len(temp))*'0' + temp
        for y in range(len(binary)):
            binary = binary[:y] + ('.','-')[int(binary[y])] + binary[y+1:]
        string[x] = binary
    return '%s %s : %s %s : %s %s'%(string[0],string[1],string[2],string[3],string[4],string[5])
