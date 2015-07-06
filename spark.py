import os, string
#~~~~Logicless pre-alpha~~~~#

whatsay = "Say something> "
st1 = 0
#0 = input as string #Default
#1 = input as number
Ssplit = True
#Determines wether to split things into arries.
S2 = " "
#What does it split?
SRemove = [""]
def inputi(): #inputi version 2. This uses less varables than the last inputi
    global whatsay, out #Varables
    global st1, Ssplit, S2, SRemove #Settings
    d = False
    out = ""
    if st1 == 0:
        while d == False:
            try:
                out = input ( whatsay )
                d = True
            except:
                print ("Input not valid")
    if st1 == 1:
        while d == False:
            try:
                out = int ( input ( whatsay ) )
                d = True
            except:
                print("Input not valid")
    if st1 != 0 and st1 != 1:
        print ( "Logic error (st1 setting)" )
    if Ssplit == True:
        out = out.split(S2)
    tick = 0
    if SRemove[0] != "":
        while done == False:
            out.split[tick](SRemove)
            tick = tick + 1
            out.remove(out[tick])
            if tick == len ( out ):
                done = True


def WordToNum():
    global out, nall
    
    n1 = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    nteen = [ "eleven", "twelve", "thirteen", "forteen", "fithteen", "sixteen","seventeen" ,"eighteen", "nineteen" ]
    n10 = [ "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
    n11 = [ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    #here I will make all the numbers as are
    nall = []
    tick = 0
    while tick < 10:
        nall.append(n1[tick])
        tick = tick + 1
    tick = 0
    nall.append(n10[tick])
    while tick < 9:
        nall.append(nteen[tick])
        tick = tick + 1
    tick = 10
    while tick < 90:
        tick1 = str ( tick ) [0]
        tick2 = str ( tick ) [1]
        tick1 = int ( tick1 ) #converting number strings to ints !!!!DONT FUCK THIS UP!!!!
        tick2 = int ( tick2 )
        if tick2 != 0:
            into = str ( n10[tick1] ) + " " + str ( n11[tick2] )
        if tick2 == 0:
            into = str ( n10[tick1] )
        nall.append( into )
        tick = tick + 1
    test = 0
    
    #a = []
    #leno = len ( out )
    #tick = 0
    #while leno > tick: #Lowers all strings in array
    #    a.append(out[tick].lower())
    #    tick = tick + 1
    #    print ( a )
    #tick = 0
    #while leno > tick:
        
                
finish = False

def c():
    os.system( "cls" )

#Load Abliv for words#

loaderFunTick = 0
loadErrorList = [ ]
loadError = 0

def l_fun(): #These will be needed in the future for a dictionary (a word like
    #"hello" could mean "hi", "morning", "evning", "greetings", etc.) 
    global fileOut, loadContent, f, loadError, loaderFunTick
    loaderFunTick = loaderFunTick + 1
    try:
        f.close()
    except:
        y = 1 + 1
        
    try:
        f = open ( loadContent )
        fileOut = f.readlines()
    except:
        print ( loadContent, " failed to load!" )
        loadError = loadError + 1
        a = str ( loaderFunTick ) + " " + loadContent 
        loadErrorList.append( a )
        
    try:
        f.close()
    except:
        y = 1 + 1

    
    
loadContent = "content/what.txt"
l_fun()
what = fileOut

loadContent = "content/why.txt"
l_fun()
why = fileOut

loadContent = "content/where.txt"
l_fun()
where = fileOut

loadContent = "content/when.txt"
l_fun()
when = fileOut

c()
if loadError > 0:
    pro = ( loadError / loaderFunTick ) * 100
    pro = "(" + str ( pro ) + "% out of " + str (  loaderFunTick ) + ")"
    a = "scripts have"
    if loadError == 1:
        a = "script has"
    print ( loadError , pro , a , "not loaded properly." )
    print ( "Simple substitutions will only be made." )
    print ( "" )
            
#logical operations and maths#

numb1 = ""
numb2 = ""
ans = ""
pt = False  #print solution?   
plmn = "" #0 for plus, 1 for minus, 2 for divide, 3 for times, 4 for root, 5 for square
solut = "" #solution
shows = True #show the solution

def Math():
    global numb1, numb2, ans, plmn, shows, solut #plus/minus = pl(us)-m(i)n(us)
    #(as well as other things that have been missed.)
    #Square will use numb1 as number to square and numb2 will
    #be used to find the square root e.g. ( numb1 ** ( 1 / numb2 )

    if plmn == "+":
        plmn = 0
    elif plmn == "-":
        plmn = 1
    elif plmn == "/":
        plmn = 2
    elif plmn == "*":
        plmn = 3
    elif plmn == "**":
        plmn = 5
    else:
        print ( plmn, "not valid!" )
                
    if plnm == 0:
        sotsi = "+"
    elif plmn == 1:
        sotsi = "-"
    elif plmn == 2:
        sotsi = "/"
    elif plmn == 3:
        sotsi = "*"
    elif plmn == 3 or plmn == 4:
        sotsi = "**"
    else:
        print ( plmn, "not valid!" )
    
    try:
        numb1 = int ( numb1 )
        numb2 = int ( numb2 )
        if plmn == 0:
            ans = numb1 + numb2
            
            if shows == True:
                if numb1 > ( numb2 + 1 ):
                    biggerNum = 1
                    bigger = len ( numb1 )
                else:
                    biggerNum = 2
                    bigger = len ( numb2 )
                
                part1 = numb1
                part2 = "+" + numb2
                part3 = "-" * bigger
                part4 = ans
                a = [ len ( part1 ), len ( part2 ), len ( part3 ), len ( part4 ) ]
                b = a
                a.sort()
                a.reverse()
                long = a[0]

                tick = 0
                while tick < 4:
                    b[tick] = b[tick] - long
                    tick = tick + 1

                part1 = " " * b[0] + part1
                part2 = " " * b[1] + part2
                part3 = " " * b[2] + part3
                part4 = " " * b[3] + part4
                
                solut = part1 + "\n" + part2 + "\n" + part3 + "\n" + part4

                
        if plmn == 1:
            ans = numb1 - numb2
        try:
            if plmn == 2:
                ans = numb1 / numb2
                
        except:
            if numb1 == 0 or numb2 == 0:
                if numb1 == numb2:
                    c()
                    print ("As Siri explains, imagine that you\nhave zero cookies and you split them evenly among\nzero friends.\nHow many cookies does each person get?")
                    print ("See? It doesn't make sense.\nAnd Cookie Monster is sad that there are no cookies.\nAnd you are sad that you have no friends.")
                else:
                    c()
                    print ("You cannot use zeros in dividing")
            else:
                print ("Math error")
        if plmn == 3:
            ans = numb1 * numb2
        if plmn == 4:
            try:
                ans = numb1 ** ( 1 / numb2 )
            except:
                print ("Math error")
        if plmn == 5:
            ans = numb ** numb2
    except:
        print ( numb1, "and", numb2, "are not numbers" )

        
while finish == False:
    ti = 0
    inputi()
    whatsay = "> "
    c()
    leno = len ( out )
    print ( out )
    if leno > ti:
        if out[ti].lower() == "debug":
            ti = ti + 1
            if leno > ti:
                if out[ti].lower == "mode":
                    debug = True
            debug = True
        


            
    if debug == True:
        finish = True
        print ( "Debug enabled (just commands mode)" )
    
