import ricardo

name = "ricardo"
gif = ricardo.gif

for i in range(len(gif)):
    for x in range(len(gif[i])):
        print(gif[i][x][0] == 0, gif[i][x][1] == 255, gif[i][x][2] == 0)
        if gif[i][x][0] == 0 and gif[i][x][1] == 255 and gif[i][x][1] == 0:
            gif[i][x] = (0, 0, 0)
            print("lol")

# for frame in gif:
#     for px in frame:
#         print(str(tu) + " " + str(px))
#         if tu == px:
#             print("in")
#             px = (0, 0, 0)
#             #print(px)

gif = "gif = " + str(gif)
f = open(name + ".py", "w")
f.write(gif)
f.close()
