import sys
import os
from PIL import Image

# grab first and second arguments 
image_folder = sys.argv[1]
output_folder = sys.argv[2] 
# check is new/exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through pokedex 

# convert images to png 

# save to the new folder 
