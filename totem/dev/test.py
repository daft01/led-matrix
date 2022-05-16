import display.ricardo

name = "ricardo"
gif = ricardo.gif
m = {}

for frame in gif:
    for pix in frame:
        if pix in m:
            m[pix] = m[pix] + 1
        else:
            m[pix] = 1

background = max(m, key=m.get)
newGif = []

for frame in gif:
    newFrame = []
    for pix in frame:
        if background == pix:
            newFrame.append((0, 0, 0))
        else:
            newFrame.append(pix)
    newGif.append(newFrame)

f = open(name + ".py", "w")
f.write("gif = " + str(newGif))
f.close()
