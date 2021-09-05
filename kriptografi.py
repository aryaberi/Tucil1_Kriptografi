from tkinter import *
from tkinter import filedialog


def convert_alfabet(X):
    if(X == "A" or X == "a"):
        return 1
    elif(X == "B" or X == "b"):
        return 2
    elif(X == "C" or X == "c"):
        return 3
    elif(X == "D" or X == "d"):
        return 4
    elif(X == "E" or X == "e"):
        return 5
    elif(X == "F" or X == "f"):
        return 6
    elif(X == "G" or X == "g"):
        return 7
    elif(X == "H" or X == "h"):
        return 8
    elif(X == "I" or X == "i"):
        return 9
    elif(X == "J" or X == "j"):
        return 10
    elif(X == "K" or X == "k"):
        return 11
    elif(X == "L" or X == "l"):
        return 12
    elif(X == "M" or X == "m"):
        return 13
    elif(X == "N" or X == "n"):
        return 14
    elif(X == "O" or X == "o"):
        return 15
    elif(X == "P" or X == "p"):
        return 16
    elif(X == "Q" or X == "q"):
        return 17
    elif(X == "R" or X == "r"):
        return 18
    elif(X == "S" or X == "s"):
        return 19
    elif(X == "T" or X == "t"):
        return 20
    elif(X == "U" or X == "u"):
        return 21
    elif(X == "V" or X == "v"):
        return 22
    elif(X == "W" or X == "w"):
        return 23
    elif(X == "X" or X == "x"):
        return 24
    elif(X == "Y" or X == "y"):
        return 25
    elif(X == "Z" or X == "z"):
        return 26
    else:
        return None

def convert_Back(X):
    if(X == 1):
        return "A"
    elif(X == 2):
        return "B"
    elif(X == 3):
        return "C"
    elif(X == 4):
        return "D"
    elif(X == 5):
        return "E"
    elif(X == 6):
        return "F"
    elif(X == 7):
        return "G"
    elif(X == 8):
        return "H"
    elif(X == 9):
        return "I"
    elif(X == 10):
        return "J"
    elif(X == 11):
        return "K"
    elif(X == 12):
        return "L"
    elif(X == 13):
        return "M"
    elif(X == 14):
        return "N"
    elif(X == 15):
        return "O"
    elif(X == 16):
        return "P"
    elif(X == 17):
        return "Q"
    elif(X == 18):
        return "R"
    elif(X == 19):
        return "S"
    elif(X == 20):
        return "T"
    elif(X == 21):
        return "U"
    elif(X == 22):
        return "V"
    elif(X == 23):
        return "W"
    elif(X == 24):
        return "X"
    elif(X == 25):
        return "Y"
    else:
        return "Z"

arrV = [["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
        ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A"],
        ["C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B"],
        ["D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C"],
        ["E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D"],
        ["F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E"],
        ["G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F"],
        ["H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G"],
        ["I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H"],
        ["J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I"],
        ["K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J"],
        ["L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K"],
        ["M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L"],
        ["N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M"],
        ["O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N"],
        ["P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"],
        ["Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"],
        ["R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q"],
        ["S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"],
        ["T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"],
        ["U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"],
        ["V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U"],
        ["W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V"],
        ["X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W"],
        ["Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X"],
        ['Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
        ]
arrVfull = [
        ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
        ["A","C","P","U","F","G","J","I","H","K","L","X","N","O","Q","D","R","S","T","E","V","W","M","Y","Z","B"],
        ["H","I","J","K","U","V","W","L","M","N","O","C","D","E","F","G","P","Q","R","S","T","X","Y",'Z',"A","B"],
        ["D","E","F","G","L","J","K","R","S","T","U","V","M","N","O","P","Q","H","I","W","X","Y",'Z',"A","B","C"],
        ["R","S","T","U","C","D","E","F","G","H","I","J","K","V","W","X","Y",'Z',"A","B","L","M","N","O","P","Q"],
        ["K","L","O","P","Q","R","S","F","G","M","N","H","I","J","T","Y",'Z',"A","B","C","D","E","U","V","W","X"],
        ["L","M","N","O","P","Q","R","S","G","H","I","J","K","B","C","D","E","F","T","U","V","W","X","Y",'Z',"A"],
        ["M","O","P","H","I","N","J","K","L","Q","R","S","T","U","V","C","D","E","F","G","W","X","Y",'Z',"A","B"],
        ["J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I"],
        ["K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J"],
        ["L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K"],
        ["N","O","P","X","M","Y",'Z',"F","G","H","Q","R","S","T","U","V","W","I","J","K","L","A","B","C","D","E"],
        ["R","S","N","O","P","Q","X","Y",'Z',"A","T","U","V","G","H","I","J","W","B","C","D","E","F","M","K","L"],
        ["A","B","C","D","O","P","Q","R","S","T","U","V","W","J","K","L","M","N","X","Y",'Z',"E","F","G","H","I"],
        ["X","I","J","K","N","O","M","T","U","V","P","Q","L","W","R","S","Y",'Z',"A","B","C","D","E","F","G","H"],
        ["U","E","F","G","H","V","W","X","Y",'Z',"Q","R","S","T","M","N","O","P","A","B","C","D","I","J","K","L"],
        ["S","T","U","V","A","B","C","M","N","O","W","X","Y",'Z',"P","Q","R","D","E","F","G","H","I","J","K","L"],
        ["T","U","V","W","X","Y",'Z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"],
        ["B","V","W","X","Y",'Z',"A","G","H","C","D","E","F","U","O","P","Q","R","S","T","I","J","K","L","M","N"],
        ["I","X","Y",'Z',"A","B","J","K","D","E","F","G","V","W","C","H","L","M","N","O","P","Q","R","S","T","U"],
        ["A","J","K","D","E","W","X","Y",'Z',"F","G","H","I","N","O","P","Q","R","L","M","B","C","S","T","U","V"],
        ["A","C","J","K","L","M","N","O","P","D","X","B","Y",'Z',"E","F","U","V","W","G","H","I","Q","R","S","T"],
        ["Y","A","B","K",'Z',"L","M","N","C","D","E","J","T","U","V","W","F","G","H","I","X","O","P","Q","R","S"],
        ["C","F",'Z',"A","D","E","B","G","H","R","S","T","L","W","X","I","J","K","P","Q","Y","M","N","O","U","V"]
        ]

def convert_int(Text):
    answer = []
    for i in Text:
        if(convert_alfabet(i) != None ):
            answer.append(convert_alfabet(i))
    return answer
def convert_char(int):
    answer = []
    for i in int:
        answer.append(convert_Back(i))
    return answer
def generateKey(Text,Key):
    nKey = []
    j = len(Key)
    for i in range(len(Text)):
        nKey.append(Key[i % j])
    return nKey

def generateAutoKey(Text,Key):
    nKey = []
    j = len(Key)
    for k in range (j):
        nKey.append(Key[k])
    if(j < len(Text)):
        for i in range(len(Text)-(j)):
            nKey.append(Text[i])
    return nKey

def vegenChip(Text,Key,m):
    i = convert_alfabet(Text)
    j = convert_alfabet(Key)
    if(m == 1):
        return arrV[j-1][i-1]
    else:
        return arrVfull[j-1][i-1]

    
def dekChip(Text,Key,m):
    find = True
    k = convert_alfabet(Text)
    j = convert_alfabet(Key)
    i = 0
    while(find == True and i < 26):
        if(m == 1):
            if(arrV[i][j-1] == Text):
                find = False
            else:
                i+=1
        else:
            if(arrVfull[j-1][i] == Text):
                find = False
            else:
                i+=1
    return i+1

def vegenChipextend(Text,Key):
    i = int(ord(Text))
    j = int(ord(Key))
    return (i+j%26)
def dVegenChiperExtend(Text,Key):
    i = int(ord(Text))
    j = int(ord(Key))
    return(i-j%26)


def dekautochiper(Text,Key,i):
    final = []
    nText = []
    if((len(Text) > len(Key))):
        for i in range(len(Key)):
            X = dekChip(Text[i],Key[i],1)
            final.append(convert_Back(X))
        for k in range(i+1,len(Text)):
            nText.append(Text[k])
        beforeFinal = dekautochiper(nText,final,i-(len(Key)-1)) 
        for h in range(len(beforeFinal)):
            final.append(beforeFinal[h])
    else:
        for i in range(len(Text)):
            X = dekChip(Text[i],Key[i],1)
            final.append(convert_Back(X))
    return final

def anyXinarr(X,arr):
    find = False
    i = 0
    while((i < len(arr)) and find == False):
        if(arr[i] == X):
            find = True
        else:
            i+=1
    return find


def makePlainKey(Text):
    matrix=[["A","B","C","D","E"],["F","G","H","I","K"],["L","M","N","O","P"],["Q","R","S","T","U"],["V","W","X","Y","Z"]]
    nKey =[]
    arr = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(len(Text)):
        if(Text[i] != "J" and anyXinarr(Text[i],nKey)== False):
            nKey.append(Text[i])
    for j in range(len(arr)):
        if(arr[j]!= "J" and anyXinarr(arr[j],nKey)== False):
            nKey.append(arr[j])
    for k in range(5):
        for l in range(5):
            matrix[k][l] = nKey[((4+1)*k)+l]
    return matrix

def makePleferText(Text):
    nText = []
    for i in range(len(Text)):
        if(Text[i] != "J"):
            nText.append(Text[i])
        else:
            nText.append("I")
    for k in range(len(nText)-1):
        if(nText[k+1] == nText[k]):
            nText.insert(k+1,"X") 
    if(len(nText)%2 != 0): 
        nText.append("X")
    return nText

def findH(H1,matrix):
    i=0
    find = False
    while(i < 5 and find == False):
        j=0
        while(j < 5) and find == False:
            if(matrix[i][j] == H1):
                find = True
                return i,j
            else:
                j+=1
        i+=1
    

def encripPlefer(H1,H2,matrix):
    i,j = findH(H1,matrix)
    k,l = findH(H2,matrix)
    if(j == l):
        if((i+1) < 5 and (k+1) < 5):
            return matrix[i+1][j],matrix[k+1][l]
        elif((i+1) > 5):
            return matrix[0][j],matrix[k+1][l]
        elif((k+1) > 5):
            return matrix[i+1][j],matrix[0][l]
        else:
            return matrix[0][j],matrix[0][l]
    elif(i == k):
        if((j+1) < 5 and (l+1) < 5):
            return matrix[i][j+1],matrix[k][l+1]
        elif((j+1) >= 5):
            return matrix[i][0],matrix[k][l+1]
        elif((l+1) >= 5):
            return matrix[i][j+1],matrix[k][0]
        else:
            return matrix[i][0],matrix[k][0]
    else:
        return matrix[i][l],matrix[k][j]

def dencripPlefer(H1,H2,matrix):
    i,j = findH(H1,matrix)
    k,l = findH(H2,matrix)
    if(j == l):
        if((i-1) >= 0 and (k+1) >= 0):
            return matrix[i-1][j],matrix[k-1][l]
        elif((i-1) < 0):
            return matrix[4][j],matrix[k-1][l]
        elif((k-1) < 0):
            return matrix[i-1][j],matrix[4][l]
        else:
            return matrix[4][j],matrix[4][l]
    elif(i == k):
        if((j-1) >= 0 and (l+1) >= 0):
            return matrix[i][j-1],matrix[k][l-1]
        elif((j-1) < 0):
            return matrix[i][4],matrix[k][l-1]
        elif((l-1) < 0):
            return matrix[i][j-1],matrix[k][4]
        else:
            return matrix[i][4],matrix[k][4]
    else:
        return matrix[i][l],matrix[k][j]

def affineEnkrip(Text,a,b):
    encript = []
    for i in range (len(Text)):
        encript.append((int(a)*int(Text[i])+int(b))%26+1)
    return encript

def egcd(a, b):
    a = int(a)
    b = int(b)
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
    


def affineDekrip(Text,a,b):
    decrip = []
    inverse = modinv(a,26)
    for i in range(len(Text)):
        decrip.append(((int(inverse)*(int(Text[i]-int(b))))%26)+1)
    return decrip


def showHasil(text,Key,m,r):
    
    if(m == 1):
        array = convert_int(text)
        array2 = convert_char(array)
        nKey = generateKey(array2,Key)
        anwer = []
        for i in range(len(nKey)):
            anwer.append(vegenChip(array2[i],nKey[i],1))
        anwer2 = []
        for i in range(len(nKey)):
            anwer2.append(dekChip(array2[i],nKey[i],1))
        danswer = convert_char(anwer2)
    if(m == 2):
        array = convert_int(text)
        array2 = convert_char(array)
        nKey = generateKey(array2,Key)
        anwer = []
        for i in range(len(nKey)):
            anwer.append(vegenChip(array2[i],nKey[i],2))
        anwer2 = []
        for i in range(len(nKey)):
            anwer2.append(dekChip(array2[i],nKey[i],2))
        danswer = convert_char(anwer2)
    
    if(m == 3):
        array = convert_int(text)
        array2 = convert_char(array)
        nKey = generateAutoKey(array2,Key)
        anwer = []
        for i in range(len(nKey)):
            anwer.append(vegenChip(array2[i],nKey[i],1))
        danswer = []
        danswer = (dekautochiper(array2,Key,0))
    
    if(m == 4):
        array2 = text
        nKey = generateKey(array2,Key)
        anwers = []
        for i in range(len(nKey)):
            anwers.append(vegenChipextend(text[i],nKey[i]))
        anwer = []
        for i in range(len(nKey)):
            anwer.append(chr(anwers[i]))
        danswer = []
        for i in range(len(nKey)):
            danswer.append(chr(dVegenChiperExtend(text[i],nKey[i])))
        

    
    
    if(m == 5):
        array = convert_int(text)
        array2 = convert_char(array)
        plaintext = makePleferText(array2)
        converKey = convert_int(Key)
        convertKey = convert_char(converKey)
        nKey = makePlainKey(convertKey)
        answer = []
        for i in range(0,len(plaintext),2):
            answer.append(encripPlefer(plaintext[i],plaintext[i+1],nKey))
        anwer = []
        for i in range (int(len(plaintext)/2)):
            for j in range(2):
                anwer.append(answer[i][j])
        danwer=[]
        for i in range(0,len(array2),2):
            danwer.append(dencripPlefer(array2[i],array2[i+1],nKey))
        danswer = []
        for i in range (int(len(danwer))):
            for j in range(2):
                if(danwer[i][j] != "X"):
                    danswer.append(danwer[i][j])
                
    if(m == 6):
        array = []
        array = convert_int(text)
        array2 = convert_char(array)
        nArray = []
        for  i in range(len(array)):
            nArray.append(int(array[i]-1))
        answer = affineEnkrip(nArray,a.get(),b.get())
        anwer = convert_char(answer)
        array3 = affineDekrip(nArray,a.get(),b.get())
        danswer = convert_char(array3)


    if(r == 1):
        global plain,Label1,chiper,Label2
        plain.pack_forget()
        Label1.pack_forget()
        chiper.pack_forget()
        Label2.pack_forget()
        Label1 = Label(main, text = "Ini Plain Text")
        Label1.pack()
        plain = Label(main, text = array2)
        plain.pack()
        Label2 = Label(main, text = "Ini Chiper Text")
        Label2.pack()
        if(c.get() == 1):
            chiper = Label(main,text=anwer)
            chiper.pack()
        else:
            count = 0
            for i in range(len(anwer)):
                if(anwer[i] != " "):
                    count+=1
                if(count == 6):
                    anwer.insert(i," ")
                    count = 0
            chiper = Label(main,text=anwer)
            chiper.pack()

    else:
        plain.pack_forget()
        Label1.pack_forget()
        chiper.pack_forget()
        Label2.pack_forget()
        Label1 = Label(main, text = "Ini Chiper Text")
        Label1.pack()
        plain = Label(main, text = array2)
        plain.pack()
        Label2 = Label(main, text = "Ini Plain Text")
        Label2.pack()
        chiper = Label(main,text=danswer)
        chiper.pack()
    


    



main = Tk()
main.geometry('500x450+10+200')
plain = Label(main)
Label1 = Label(main)
chiper = Label(main)
Label2 = Label(main)

def pilihFile():
    global f_content
    main.filename = filedialog.askopenfilename(initialdir="/c",title="Pilih file")
    with open(main.filename,'r') as f:
        f_content = f.read()
    fileLabel=Label(main,text=main.filename)
    fileLabel.pack()

m = IntVar()
mrd1 = Radiobutton(main,text="Vigenere standar" ,variable=m, value = 1)
mrd2 = Radiobutton(main,text="Vigenere Full", variable=m, value = 2)
mrd3 = Radiobutton(main,text="Vigenere auto", variable=m, value = 3)
mrd4 = Radiobutton(main,text="Vigenere extend", variable=m, value = 4)
mrd5 = Radiobutton(main,text="plefer chiper", variable=m, value = 5)
mrd6 = Radiobutton(main,text="affine chiper", variable=m, value = 6)

label = Label(main, text = "Masukan Text")
entry = Entry(main,width=30)

openFile = Button(main, text="Pilih File", command=pilihFile)


label2 = Label(main, text = "Masukan Key")
entry2 = Entry(main,width=30)

label3 = Label(main, text = "Masukan Key a affine chiper")
a = Entry(main)
label4 = Label(main, text = "Masukan Key b affine chiper")
b = Entry(main)

r = IntVar()
rd1 = Radiobutton(main,text="Enkrip" ,variable=r, value = 1)
rd2 = Radiobutton(main,text="Dekrip", variable=r, value = 2)

c = IntVar()
rd3 = Radiobutton(main,text="Rapet" ,variable=c, value = 1)
rd4 = Radiobutton(main,text="per 5 item", variable=c, value = 2)

button1 = Button(main, text="Ubah dari iput", command=lambda : showHasil(entry.get(),entry2.get(),m.get(),r.get()))
button2 = Button(main, text="Ubah dari file", command=lambda : showHasil(f_content,entry2.get(),m.get(),r.get()))


rd = Label(main,text="Pilih Jenis Kripto")
rd.pack()
rd.place(x=10,y=10)
mrd1.pack()
mrd1.place(x=10,y=40)
mrd2.pack()
mrd2.place(x=10,y=70)
mrd3.pack()
mrd3.place(x=10,y=100)
mrd4.pack()
mrd4.place(x=10,y=130)
mrd5.pack()
mrd5.place(x=10,y=160)
mrd6.pack()
mrd6.place(x=10,y=190)
label.pack()
entry.pack(ipady=5)
openFile.pack()
label2.pack()
entry2.pack(ipady=5)
label3.pack()
a.pack()
label4.pack()
b.pack()
r2 =Label(main,text="Pilih Ekrip atau Dekrip")
r2.pack()
r2.place(x=10,y=220)
rd1.pack()
rd1.place(x=10,y=250)
rd2.pack()
rd2.place(x=10,y=280)
r3=Label(main,text="Pilih tampilan text")
r3.pack()
r3.place(x=10,y=310)
rd3.pack()
rd3.place(x=10,y=340)
rd4.pack()
rd4.place(x=10,y=370)
button1.pack()
button2.pack()


main.mainloop()