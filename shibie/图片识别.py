import sys, Image

img = Image.open(sys.argv[1]).convert('YCbCr')

w, h = img.size

data = img.getdata()

cnt = 0

for i, ycbcr in enumerate(data):

    y, cb, cr = ycbcr

    if 86 <= cb <= 117 and 140 <= cr <= 168:
        cnt += 1

print('%s %s a porn image.' % (sys.argv[1], 'is' if cnt > w * h * 0.3 else 'is not'))
