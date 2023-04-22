from PIL import ImageColor, Image, ImageDraw, ImageFont
import os
im = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(im)
'''
draw.point([0,2,0,3,0,4,0,5,0,6,0,7], 'blue')
draw.line([(0,0),(199,0),(199,199), (0, 199), (0,0)], 'black')

im.save('imagePoint.png')
'''
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'C:\\Windows\\Fonts'

arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100,150), 'Howdy', fill = 'grey', font=arialFont)
im.save('text.png')

'''
catIm = Image.open('zophie.png')
width, height = catIm.size
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20,20))
im2.save('transparentImage.png')

croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')
catCopyIm = catIm.copy()
catCopyIm.paste(croppedIm, (0,0))
catCopyIm.paste(croppedIm, (400,500))
catCopyIm.save('pasted.png')

faceWidth, faceHeight = croppedIm.size
catCopyTwo = catIm.copy()
for left in range(0, width, faceWidth):
    for top in range(0, height, faceHeight):
        print(left, top)
        catCopyTwo.paste(croppedIm, (left, top))

catCopyTwo.save('tiled.png')

quartersizedIm = catIm.resize((int(width/2), int(height/2)))
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height+300))
svelteIm.save('svelte.png')

catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
#expand enlarges the dimensions of the image all together to fit the whole new rotated image - so all image pixels and the black fit
ro_and_exp_Im = catIm.rotate(6, expand=True)
ro_and_exp_Im.save('rotated6_expanded.png')

catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')

newIm = Image.new('RGBA', (100,100))
for x in range(100):
    for y in range(50):
        newIm.putpixel((x,y), (210, 210, 210))
for x in range(100):
    for y in range(50, 100):
        newIm.putpixel((x, y), (245, 245, 245))
newIm.save('putPixel.png')
'''
