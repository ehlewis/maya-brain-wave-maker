import maya.cmds as cmds
#/Users/evanlewis/Desktop/EEGDataLogger.csv
#C:\Users\Evan\Desktop\waveVis\EEGDataLoggerEdited.csv
#C:\Users\Evan\Desktop\waveVis\data\GoodData.csv


DATA = []
LENGTH = 0
TOTALCHANNELS = 0

def intake():
    global DATA, LENGTH, TOTALCHANNELS
    filename = raw_input('Path to CSV file')
    input_file = open(filename, 'r')
    TOTALCHANNELS = int(raw_input('# of channels'))

    temp = ''
    currNum = ''
    for line in input_file:  # Get one line at a time.
        if LENGTH == 0:
            LENGTH = LENGTH + 1
        else:
            DATA.append([])
            for i in range(len(line)):
                if line[i].isdigit() or str(line[i]) == ".":
                    currNum = currNum + str(line[i])
                elif currNum != '':
                    DATA[LENGTH-1] += [float(currNum)]
                    currNum = ''
                else:
    				currNum = ''
            LENGTH += 1
    print(LENGTH)


def createPlanes():
    global LENGTH
    total = LENGTH
    pos = 0
    input_file.close()
    while total > 1000:
        waves = cmds.polyPlane(w=10, h=1, sx=1000, sy=7)
        cmds.move( 10*pos, x=True )
        pos += 1
        total -= 1000

    waves = cmds.polyPlane(w=10, h=1, sx=total, sy=7)
    cmds.move( 10*pos, x=True )


def impressOnPlanes():
    global DATA, LENGTH, TOTALCHANNELS
    discon = i = x = channel =0
    pplane = 1
    KMult = 1000
    while channel < TOTALCHANNELS:
        while i < LENGTH-1:
              if i % (1000 + discon) == 0 and i != 0: #the discon only affects channel rows not x rows between planes
                  pplane += 1
                  x = KMult + discon
              cmds.select("pPlane" + str(pplane) + ".vtx[" + str(x+1) + "]")
              cmds.move( (DATA[i][channel]/100), y=True )
              i += 1
              x += 1
        discon += 1
        channel += 1
        KMult += 1000
        i = 0
        x = KMult + discon
        pplane = 1

def createCurve(channel, offset = 0):
    global DATA
    global LENGTH
    channelData = []
    for i in range(LENGTH-1):
        channelData.append((float(i), DATA[i][channel]/100, float(offset)))
    print (channelData)
    #cmds.curve(p=[(0, 0, 0), (3, 5, 6), (5, 6, 7), (9, 9, 9)])
    cmds.curve(p=channelData)

def createCurveAllChannels():
    global TOTALCHANNELS
    for i in range(TOTALCHANNELS): #idk whats wrong here   if 5 channels its out of range after the 5th curve but if its 5-1 only 4 are made
        createCurve(i - 1, i)

def revolve():
    #revolve the first (hopefully only) curve made
    cmds.revolve('curve1', ax=(1, 0, 0), p=(0, 0, 0))

def loft(channels = 5):
    #select curves and loft them
    if channels == 2:
        cmds.loft('curve1', 'curve2', ch=True, rn=True, ar=True)
    elif channels == 3:
        cmds.loft('curve1', 'curve2', 'curve3', ch=True, rn=True, ar=True)
    elif channels == 4:
        cmds.loft('curve1', 'curve2', 'curve3', 'curve4', ch=True, rn=True, ar=True)
    elif channels == 5:
        cmds.loft('curve1', 'curve2', 'curve3', 'curve4', 'curve5', ch=True, rn=True, ar=True)
    elif channels == 6:
        cmds.loft('curve1', 'curve2', 'curve3', 'curve4', 'curve5', 'curve6', ch=True, rn=True, ar=True)
    elif channels == 7:
        cmds.loft('curve1', 'curve2', 'curve3', 'curve4', 'curve5', 'curve6', 'curve7', ch=True, rn=True, ar=True)
    elif channels == 8:
        cmds.loft('curve1', 'curve2', 'curve3', 'curve4', 'curve5', 'curve6', 'curve7', 'curve8', ch=True, rn=True, ar=True)

'''
intake()
createPlanes()
impressOnPlanes()
channel = int(raw_input('Which channel?'))'''
intake()
createCurveAllChannels()
loft()