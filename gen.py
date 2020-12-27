from itertools import permutations

lett  ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = 0
dic=[""]
w =["",""]
let1= ""
let2= ""
for w in permutations(lett, 2):
    let1=w[0]
    let2=w[1]
    for x in range(0,1000):
        if x < 10:
            url ="00" + str(x)

        if x>9:
            if x<100:
                url= "0"+ str(x)

        if x>99:
            url= str(x)
        f = open("demofile2.txt", "a")
        f.write(url+let1+let2+"\n")
        f.close()
for dic in permutations(lett, 1):
    let1=dic[0]
    let2 = dic[0]
    for x in range(0,1000):
        if x < 10:
            url ="00" + str(x)

        if x>9:
            if x<100:
                url= "0"+ str(x)

        if x>99:
            url= str(x)
        f = open("demofile2.txt", "a")
        f.write(url+let1+let2+"\n")
        f.close()
