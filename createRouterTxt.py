from tkinter import *

gui = Tk()
gui.title("Subnetteador 3000")


textPort = []
textRIP = []


listaDeIdentificadores = []
listaDeIPS =[]
listaDeMascaras = []
listaDeTiposDePuerto=[]

direcciones = []

id = StringVar()
br = StringVar()
redInicial = StringVar()
cdp = BooleanVar()
cdp.set(False)
lldp = BooleanVar()
lldp.set(False)
noip = BooleanVar()
noip.set(False)
username = StringVar()
password = StringVar()
loginlocal = BooleanVar()
red = StringVar()
mask = StringVar()
tel = BooleanVar()
rd = StringVar()
hostname = StringVar()
puerto = StringVar()
dirPuerto = StringVar()
maskPuerto = StringVar()
rip = StringVar()
test = StringVar()
motd = StringVar()
numMask = StringVar()

def nextI():
    dirPuerto.set(direcciones[0])
    direcciones.pop(0)

def addPort():
    textPort.append("int "+puerto.get()+"\n ip address "+ dirPuerto.get() + " " + maskPuerto.get() + "\n no shutdown \n exit \n")
    #test.set("int "+puerto.get()+"\n ip address "+ dirPuerto.get() + " " + maskPuerto.get() + "\n exit \n")
def addRIP():
    textRIP.append("network " + rip.get() + "\n")
    #test.set("network " + rip.get() + "\n")

def resetTodo():
    id.set("")
    br.set("")
    username.set("")
    red.set("")
    mask.set("")
    password.set("")
    hostname.set("")
    motd.set("")
    puerto.set("")
    dirPuerto.set("")
    maskPuerto.set("")
    rip.set("")
    cdpCheck.deselect()
    lldpCheck.deselect()
    noipCheck.deselect()
    telnet.deselect()
    localCheck.deselect()
    textPort.clear()
    textRIP.clear()
    direcciones.clear()
    rd.set("")
def repMask():
    maskPuerto.set(mask.get())

def useID():
    rip.set(id.get())

def reset():
    f = open("Subnet.txt", "w+")
    f.close()

def subnet():
    redBase = red.get().split(".")
    m = mask.get().split(".")
    redesResultantes = []
    broad = []
    for i in range(4):
        redesResultantes.append(str(int(redBase[i]) & int(m[i])))
        broad.append(str(int(redesResultantes[i]) | (~int(m[i]) & 255)))
    id.set(".".join(redesResultantes))
    br.set(".".join(broad))
    X = list()
    for i in range(int(redesResultantes[3])+1, int(broad[3])):
        X.append(redesResultantes[:3]+[str(i)])
    Y = list(map(lambda x: ".".join(x), X))
    Z = "IP's disponibles: \n "

    for i in Y[:30]:
        Z += str(i) + "\n"
        direcciones.append(str(i))
    rd.set(Z)


def añadir():
    

    direcciones = []
    f = open("Subnet.txt", "a")
    f.write("\n")
    f.write("\n")
    f.write("enable \n")
    f.write("configure terminal \n")
    if lldp.get() == True:
        f.write("lldp run \n")
    if cdp.get() == True:
        f.write("cdp run \n")
    if noip.get() == True:
        f.write("no ip domain-lookup \n")
    if username.get() != "" and password.get() != "":
        s = "username " + username.get() + " "
        f.write(s)
        s = "password " + password.get() + "\n"
        f.write(s)
    if loginlocal.get() == True and username.get() != "" and password.get() != "":
        f.write("line vty 0 15 \n")
        f.write("login local \n")
        if tel.get() == True:
            f.write("transport input telnet \n")
        f.write("exit \n")
    if hostname.get() != "":
        s = "hostname " + hostname.get() + "\n"
        f.write(s)
    if len(textPort) != 0:
        for i in textPort:
            f.write("\n")
            f.write(i)
            f.write("\n")
    textPort.clear()
    if len(textRIP) != 0:
        f.write("\n")
        f.write("router rip \n")
        for i in textRIP:
            f.write(i)
        f.write("version 2 \n")
        f.write("no auto-summary \n")
        f.write("exit \n")
    textRIP.clear()
    if motd.get() != "":
        f.write("banner motd | \n")
        f.write(motd.get() +"|\n")

    f.close()




miFrame = Frame(gui, width = 1000, height = 1000, bg = "red")
miFrame.pack()

# A partir de aquí son los botones y demás elementos.

text1 = Label(miFrame, text = "Red a subnettear:", bg = "red")
text1.grid(row = 1, column = 1, padx = 10, pady = 10)

entryRed = Entry(miFrame, textvariable = red)
entryRed.grid(row = 1, column = 2, padx = 10, pady = 10)

text4 = Label(miFrame, text = "Máscara:", bg = "red")
text4.grid(row = 2, column = 1, padx = 10, pady = 10)

entryMask = Entry(miFrame, textvariable = mask)
entryMask.grid(row = 2, column = 2, padx = 10, pady = 10)

text2 = Label(miFrame, text = "ID de red:", bg = "red")
text2.grid(row = 3, column = 1, padx = 10, pady = 10)

entryID = Entry(miFrame, state = "disabled", textvariable = id)
entryID.grid(row = 3, column = 2, padx = 10, pady = 10)

text3 = Label(miFrame, text = "Broadcast:", bg = "red")
text3.grid(row = 4, column = 1, padx = 10, pady = 10)

entryBroadcast = Entry(miFrame, state = "disabled", textvariable = br)
entryBroadcast.grid(row = 4, column = 2, padx = 10, pady = 10)

cdpCheck = Checkbutton(miFrame, text = "CDP", variable = cdp, onvalue = True, offvalue = False, bg = "red")
cdpCheck.grid(row = 1, column = 3, padx = 10, pady = 10, sticky = "W")

lldpCheck = Checkbutton(miFrame, text = "LLDP", variable = lldp, onvalue = True, offvalue = False, bg = "red")
lldpCheck.grid(row = 2, column = 3, padx = 10, pady = 10, sticky = "W")

noipCheck = Checkbutton(miFrame, text = "No IP Domain-Lookup", variable = noip, bg = "red")
noipCheck.grid(row = 3, column = 3, padx = 10, pady = 10, sticky = "W")

userText = Label(miFrame, text = "Username:", bg = "red")
userText.grid(row = 1, column = 4, padx = 10, pady = 10)

userEntry = Entry(miFrame, textvariable = username)
userEntry.grid(row = 1, column = 5, padx = 10, pady = 10)

passText = Label(miFrame, text = "Password:", bg = "red")
passText.grid(row = 2, column = 4, padx = 10, pady = 10)

passEntry = Entry(miFrame, textvariable = password)
passEntry.grid(row = 2, column = 5, padx = 10, pady = 10)

localCheck = Checkbutton(miFrame, text = "Login Local", variable = loginlocal, onvalue = True, offvalue = False, bg = "red")
localCheck.grid(row = 4, column = 3, padx = 10, pady = 10, sticky = "W")

finalizar = Button(miFrame, text = "Añadir configuración actual al archivo de texto.", command = añadir)
finalizar.grid(row = 14, column = 5, padx = 10, pady = 10)

subnettear = Button(miFrame, text = "Subnettear", command = subnet)
subnettear.grid(row = 5, column = 1, padx = 10, pady = 10)

telnet = Checkbutton(miFrame, text = "Telnet", variable = tel, onvalue = True, offvalue = False, bg = "red")
telnet.grid(row = 5, column = 3, padx = 10, pady = 10, sticky = "W")

redesDisponibles = Label(miFrame, text = "", textvariable = rd, bg = "red")
redesDisponibles.grid(row = 6, column = 1, padx = 10, pady = 10, rowspan = 15, sticky = "N")

texthost = Label(miFrame, text = "Hostname:", bg = "red")
texthost.grid(row = 3, column = 4, padx = 10, pady = 10)

hostEntry = Entry(miFrame, textvariable = hostname)
hostEntry.grid(row = 3, column = 5, padx = 10, pady = 10)

resetTotal = Button(miFrame, text = "Restablecer Archivo de Texto", command = reset)
resetTotal.grid(row = 15, column = 5, padx = 10, pady = 10)

textPuerto = Label(miFrame, text = "Puerto a asignar:", bg = "red")
textPuerto.grid(row = 6, column = 4, padx = 10, pady = 10)

puertoEntry = Entry(miFrame, textvariable = puerto)
puertoEntry.grid(row = 6, column = 5, padx = 10, pady = 10)

textDirPuerto = Label(miFrame, text = "Dirección del Puerto:", bg = "red")
textDirPuerto.grid(row = 7, column = 4, padx = 10, pady = 10)

dirPuertoEntry = Entry(miFrame, textvariable = dirPuerto)
dirPuertoEntry.grid(row = 7, column = 5, padx = 10, pady = 10)

textMaskPuerto = Label(miFrame, text = "Máscara:", bg = "red")
textMaskPuerto.grid(row = 8, column = 4, padx = 10, pady = 10)

maskPuertoEntry = Entry(miFrame, textvariable = maskPuerto)
maskPuertoEntry.grid(row = 8, column = 5, padx = 10, pady = 10)

exRouters = Label(miFrame, text = "OPCIONES EXCLUSIVAS PARA ROUTERS", bg = "red")
exRouters.grid(row = 5, column = 4, columnspan = 2, padx = 10, pady = 10)

nextIP = Button(miFrame, text = "Usar siguiente IP disponible", command = nextI)
nextIP.grid(row = 7, column = 3, padx = 10, pady = 10, sticky = "E")

textRouterRip = Label(miFrame, text = "Red para Router RIP:", bg = "red")
textRouterRip.grid(row = 10, column = 4, padx = 10, pady = 10)

routerRipEntry = Entry(miFrame, textvariable = rip)
routerRipEntry.grid(row = 10, column = 5, padx = 10, pady = 10)

repeatMask = Button(miFrame, text = "Usar máscara actual", command = repMask)
repeatMask.grid(row = 8, column = 3, padx = 10, pady = 10, sticky = "E")

UseCurrentID = Button(miFrame, text = "Usar ID de red actual", command = useID)
UseCurrentID.grid(row = 10, column = 3, padx = 10, pady = 10, sticky = "E")

addPuerto = Button(miFrame, text = "Añadir puerto", command = addPort)
addPuerto.grid(row = 9, column = 5, padx = 10, pady = 10)

addRIP = Button(miFrame, text = "Añadir RIP", command = addRIP)
addRIP.grid(row = 12, column = 5, padx = 10, pady = 10)


textBanner = Label(miFrame, text = "MoTD:", bg = "red")
textBanner.grid(row = 4, column = 4, padx = 10, pady = 10)

bannerEntry = Entry(miFrame, textvariable = motd)
bannerEntry.grid(row = 4, column = 5, padx = 10, pady = 10)

masterReset = Button(miFrame, text = "Restablecer todas las entradas.", command = resetTodo)
masterReset.grid(row = 13, column = 5, padx = 10, pady = 10)

gui.mainloop()