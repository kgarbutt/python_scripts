
#!/usr/bin/python3
from PIL import Image
import os, sys

new_dir = '/opt/icons/'

for file in os.listdir(os.getcwd() + '/images/'):
	if file.endswith('dp'):

		im = Image.open(os.getcwd() + '/images/' + file)
		new_im = im.convert('RGBA').resize((128,128)).rotate(-90)
		background = Image.new('RGBA', new_im.size, (255,255,255))
		final = Image.alpha_composite(background, new_im).convert("RGB")
		new_im = new_dir + file
		final.save(new_im, 'JPEG', quality=80)

