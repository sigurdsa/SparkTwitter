f1 = open('exampleFilter22.txt', 'r')
f2 = open('exampleFilter222.txt', 'w')
for line in f1:
    f2.write(line.replace('Tower Heist Takeover, BlackBerry', 'Tower Heist Takeover BlackBerry'))
    # f2.write(line.replace('Been there, done that', 'been there done that'))
f1.close()
f2.close()
