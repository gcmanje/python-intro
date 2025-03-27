# write some text at the centre of the image using pillow
from PIL import Image, ImageDraw, ImageFont

img =Image.open ("images/background image.jpg")

draw = ImageDraw.Draw(img)
Font= ImageFont.truetype("fonts/Big_Shoulders/BigShoulders-VariableFont_opsz,wght.ttf", size=30)

text="Python is cool"
position=(50,50)

draw.text(position, text, font=Font)

img.save("images/background image2.jpg")
