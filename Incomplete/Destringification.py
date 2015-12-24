def destringification(text):
    for x in text:
        print(x)
        if x == '\\':
            print("Yes")

destringification('\\')
