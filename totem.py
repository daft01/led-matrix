from PIL import Image, ImageFilter
from IPython.display import display

def rotate(matrix):
      temp_matrix = []
      column = len(matrix)-1
      for column in range(len(matrix)):
         temp = []
         for row in range(len(matrix)-1,-1,-1):
            temp.append(matrix[row][column])
         temp_matrix.append(temp)
      for i in range(len(matrix)):
         for j in range(len(matrix)):
            matrix[i][j] = temp_matrix[i][j]
      return matrix

def convert_pixels(square):
	fullImage = [square]

	readyImage = []
	for temp in fullImage:
		for y in range(16):
			t = []
			for x in range(16):
				if temp[y][x][3]:
					t.append((temp[y][x][0], temp[y][x][1], temp[y][x][2]))
				else:
					t.append(temp[y][x])
			readyImage.append(t)

	# print(readyImage)
	readyImage = rotate(readyImage)
	readyImage = rotate(readyImage)
	readyImage = rotate(readyImage)
	for i in range(len(readyImage)):
		if i % 2:
			readyImage[i].reverse()

	test = []
	for y in range(16):
		for x in range(16):
			test.append(readyImage[y][x])

	return test

def convert_frame(frame):
	chunks = [frame[x:x+16] for x in range(0, len(frame), 16)]

	l1 = chunks[:48]
	a1 = []
	b1 = []
	c1 = []

	for i in range(48):
		if i%3 == 0:
			a1.append(l1[i])
		elif i%3 == 1:
			b1.append(l1[i])
		else:
			c1.append(l1[i])

	l2 = chunks[48:]
	a2 = []
	b2 = []
	c2 = []

	for i in range(48):
		if i%3 == 0:
			a2.append(l2[i])
		elif i%3 == 1:
			b2.append(l2[i])
		else:
			c2.append(l2[i])
	# got all squares

	c1 = convert_pixels(c1)
	c2 = convert_pixels(c2)
	b2 = convert_pixels(b2)
	b1 = convert_pixels(b1)
	a1 = convert_pixels(a1)
	a2 = convert_pixels(a2)

	for c in c2:
		c1.append(c)

	for b in b2:
		c1.append(b)

	for b in b1:
		c1.append(b)

	for a in a1:
		c1.append(a)

	for a in a2:
		c1.append(a)

	return c1

name = "illenium"
im = Image.open('gifs/' + name + '.gif')

frames = im.n_frames
frames_pixels = []

for z in range(frames):
	im.seek(z)
	frame = []
	rgb_im = im.convert('RGBA')

	for x in range(im.width):
		for y in range(im.height):
			frame.append(rgb_im.getpixel((x, y)))
	frames_pixels.append(frame)

output_frames = []

for fp in frames_pixels:
	output_frames.append("[" + ",".join(str(x) for x in convert_frame(fp)) + "]")

gif = "gif = [" + ",".join(str(x) for x in output_frames) + "]"
f = open('code/' + name + ".py", "w")
f.write(gif)
f.close()