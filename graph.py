import tkinter
xgmax = int(input("zadaj sirku platna: "))
ygmax = int(input("zadaj dlzku platna: "))
canvas = tkinter.Canvas(width = xgmax+20, height = ygmax+20)
canvas.pack()

xmin, xmax, ymin, ymax = -10, 10, -10, 10

def tx(x):
    tx = xgmax * (x-xmin) / (xmax-xmin) + 10
    return tx

def ty(y):
    ty = ygmax * (ymax-y) / (ymax-ymin) + 10
    return ty

def osi():
    canvas.create_line(tx(xmax),ty(0),tx(xmin),ty(0))
    canvas.create_line(tx(0),ty(ymax),tx(0),ty(ymin))

def popis_osi():
    for i in range(xmin,xmax+1):
        canvas.create_line(tx(i),ty(0)+3,tx(i),ty(0)-3)
        canvas.create_line(tx(0)-3,ty(i),tx(0)+3,ty(i))
        canvas.create_text(tx(i),ty(0)+10,text = str(i))
        if i != 0:
            canvas.create_text(tx(0)+10,ty(i),text=str(i))

def graf_funkcie():
    print("Zadaj parametre funkcie f(x) = ax**2 + bx + c ")
    a = int(input("parameter a: "))
    b = int(input("parameter b: "))
    c = int(input("parameter c: "))
    x1, x = xmin, xmin + 0.2
    y1 = a*x1**2 + b*x1 + c
    while x <= xmax:
        y = a*x**2 + b*x + c
        canvas.create_line(tx(x1), ty(y1), tx(x), ty(y), fill="red", width = 3)
        x1, y1 = x, y
        x = x + 0.2
osi()
popis_osi()
graf_funkcie()
