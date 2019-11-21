import sys
import os
from PIL import Image

# grab first and second arguments
path = sys.argv[1]
directory = sys.argv[2]

# check if new folder exists. If not, create a new folder.
if not os.path.exists(directory):
    os.makedirs(directory)

# loop through existing Pokedex folder
for filename in os.listdir(path):
  # separate jpg extension from filename
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
  # convert images to PNG, save to the new folder and print when complete
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')
