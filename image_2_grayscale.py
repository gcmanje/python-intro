from PIL import Image

img =Image.open ("images/background image.jpg")

black_n_white_img = img.convert('L')
black_n_white_img.show()

black_n_white_img.save("images/black_n_white_background image.jpg")

