from PIL import Image
import numpy
import cv

raw_bullet = Image.open('test/bullet.png')

def process_alpha(img):
	if img.mode == 'RGB':
		return
	if img.mode == 'RGBA':
		width, height = img.size
		pixels = img.load()
		r = 0
		g = 0
		b = 0
		avgCount = 0
		for x in range(width):
			for y in range(height):
				if pixels[x,y][3] == 255:
					r += pixels[x,y][0]
					g += pixels[x,y][1]
					b += pixels[x,y][2]
					avgCount += 1

		rAvg = r/avgCount
		gAvg = g/avgCount
		bAvg = b/avgCount

		for x in range(width):
			for y in range(height):
				if pixels[x,y][3] < 255:
					pixels[x,y] = (rAvg,gAvg,bAvg,0)

		return img.convert('RGB')

## Process the alpha channel of the bullet image
## From the opencv doc: 'In the case of a color image, template summation in the numerator and each sum in the denominator is done over all of the channels (and separate mean values are used for each channel).'

raw_bullet = process_alpha(raw_bullet)


## Convert PIL image to cv image

bullet = cv.CreateImageHeader(raw_bullet.size, cv.IPL_DEPTH_8U, 3)
cv.SetData(bullet, raw_bullet.tostring(), raw_bullet.size[0]*3)
cv.CvtColor(bullet, bullet, cv.CV_RGB2BGR)

pattern = cv.LoadImage('test/image.png')

## Prepare for the normalized cross-correlation

pattern_size = cv.GetSize(pattern)
bullet_size = cv.GetSize(bullet)
result_size = [ s[0] - s[1] + 1 for s in zip(pattern_size, bullet_size) ]
result = cv.CreateImage(result_size, cv.IPL_DEPTH_32F, 1)

## Do it!

cv.MatchTemplate(pattern, bullet, result, cv.CV_TM_CCOEFF_NORMED)

result_array = numpy.asarray(result[:])
locations = numpy.where(result_array > 0.99)

print 'Found '+str(len(locations[0]))+' bullets!'

for x,y in zip(locations[1],locations[0]):
	cv.Rectangle(pattern,(int(x),int(y)),(int(x)+bullet_size[0],int(y)+bullet_size[1]),(255,255,255),1,0)

cv.ShowImage("pattern", pattern)

cv.ShowImage("result", result)
cv.WaitKey()

