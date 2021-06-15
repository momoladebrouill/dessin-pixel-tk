from tkinter import *

f = Tk()
a = Frame(f).place(relx=.5, rely=.5, anchor="center") #ça je l'ai surrement pické quelque part
c = Canvas(a, bg="black", height=800, width=1500, border=0)
c.pack(side=LEFT)

for t in range(10, 750, 50):
    for w in range(10, 1500, 50):
        c.create_rectangle(w, t, w, t, outline="white")

dico = {}


def hex(dec):
    if dec == 0:
        return "00"
    lili = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hex = []
    while dec != 0:
        reste = int(dec % 16)
        hex.append(lili[reste])
        dec = (dec - reste) / 16
    if len(hex) == 1:
        hex.append("0")
    hex.reverse()
    hex = ''.join(hex)
    return hex


g = Canvas(a, bg="white", width=50, height=800)
g.pack(side=RIGHT)
r, v, b = 254, 1, 1
lr = []
lv = []
lb = []
lr.append(r)
lv.append(v)
lb.append(b)
for i in range(127):
    v += 2
    lr.append(r)
    lv.append(v)
    lb.append(b)
# 255 255 000 jaune
for i in range(127):
    r -= 2
    lr.append(r)
    lv.append(v)
    lb.append(b)
# 000 255 000 vert
for i in range(127):
    b += 2
    lr.append(r)
    lv.append(v)
    lb.append(b)
    # 000 255 255 bleu clair
for i in range(127):
    v -= 2
    lr.append(r)
    lv.append(v)
    lb.append(b)
    # 000 000 255 bleu
for i in range(127):
    r += 2
    lr.append(r)
    lv.append(v)
    lb.append(b)
    # 255 000 255 violet
for i in range(127):
    b -= 2
    lr.append(r)
    lv.append(v)
    lb.append(b)
    # 255 000 000 rouge
for i in range(20):
    lr.append(0)
    lv.append(0)
    lb.append(0)
for i in range(20):
    lr.append(255)
    lv.append(255)
    lb.append(255)
print(len(lr))
ya = 0
yb = 1
colo = []

count = 250
for i in range(len(lr)):
    err = str("#" + hex(lr[i]) + hex(lv[i]) + hex(lb[i]))
    colo.append(err)
    g.create_rectangle(0, ya, 50, yb, width=0, fill=err)
    ya += 1
    yb += 1
j = g.create_rectangle(0, count - 10, 50, count + 10, outline="white", width=5)


def roulette(event):
    global count, ya, yb, lr, lv, lb, j
    if event.num == 5 or event.delta == -120:
        if not count == 790:
            count += 10
    if event.num == 4 or event.delta == 120:
        if not count == 10:
            count -= 10
    g.delete(j)
    for i in range(len(lr)):
        err = str("#" + hex(lr[i]) + hex(lv[i]) + hex(lb[i]))
        colo.append(err)
        g.create_rectangle(0, ya, 50, yb, width=0, fill=err)
        ya += 1
        yb += 1
    j = g.create_rectangle(0, count - 10, 50, count + 10, outline="white", width=5)
    f.configure(background=colo[count])

def arr(a):
    n = 10
    return int(a/n)*n

def mouvement(event):
    x, y = event.x, event.y
    c.create_rectangle(arr(x - 5), arr(y - 5), arr(x + 5), arr(y + 5), width=0, fill=colo[count])
    dico[str(   str(   int(arr(x))  ) + str(int(arr(y))))] = colo[count]


def effacer(event):
    x, y = event.x, event.y
    c.create_rectangle(arr(x - 5), arr(y - 5), arr(x + 5), arr(y + 5), width=0, fill="black")


def recup(event):
    x, y = event.x, event.y
    print(dico.get(str(str(int(arr(x))) + str(int(arr(y))))))


f.configure(background=colo[count])
c.bind('<Button-1>', mouvement)
c.bind('<B1-Motion>', mouvement)
c.bind('<Button-2>', recup)
c.bind('<Button-3>', effacer)
c.bind('<B3-Motion>', effacer)
f.bind("<MouseWheel>", roulette)

f.mainloop()
