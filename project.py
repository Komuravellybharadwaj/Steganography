# function to decode data
def decode(self, image):
image_data = iter(image.getdata())
data = ''
while (True):
pixels = [value for value in image_data. next ()[:3] +
image_data. next ()[:3] +
image_data. next ()[:3]]
binary_str = ''
for i in pixels[:8]:
if i % 2 == 0:
binary_str += '0'
else:
binary_str += '1'
data += chr(int(binary_str, 2))
if pixels[-1] % 2 != 0:
return data
# - function to modify the pixels of image
def modify_Pix(self,pix, data):
dataList = self.generate_Data(data)
dataLen = len(dataList)
imgData = iter(pix)
for i in range(dataLen):
# Extracting 3 pixels at a time
pix = [value for value in imgData. next__()[:3] +
imgData. next ()[:3] +
imgData. next ()[:3]]
for j in range(0, 8):
if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
if (pix[j] % 2 != 0):
pix[j] -= 1
elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
pix[j] -= 1
if (i == dataLen - 1):
if (pix[-1] % 2 == 0):
pix[-1] -= 1
else:
if (pix[-1] % 2 != 0):
pix[-1] -= 1
pix = tuple(pix)
yield pix[0:3]
yield pix[3:6]
yield pix[6:9]