from PIL import Image
import numpy
import cv

pattern = cv.LoadImage('test/image.png')
bullet = cv.LoadImage('test/bullet.png')


pattern_size = cv.GetSize(pattern)
bullet_size = cv.GetSize(bullet)
result_size = [ s[0] - s[1] + 1 for s in zip(pattern_size, bullet_size) ]
result = cv.CreateImage(result_size, cv.IPL_DEPTH_32F, 1)
# cv.MatchTemplate(pattern, bullet, result, cv.CV_TM_CCORR_NORMED)
cv.MatchTemplate(pattern, bullet, result, cv.CV_TM_CCOEFF_NORMED)

result_array = numpy.asarray(result[:])
locations = numpy.where(result_array > 0.8)

for x,y in zip(locations[1],locations[0]):
	cv.Rectangle(pattern,(int(x),int(y)),(int(x)+bullet_size[0],int(y)+bullet_size[1]),(255,255,255),1,0)

cv.ShowImage("pattern", pattern)

cv.ShowImage("result", result)
cv.WaitKey()

