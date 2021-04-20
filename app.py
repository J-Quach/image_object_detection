import io
import os
import sys

from detect import localize_objects



if __name__ == "__main__":

    # File directory
    image_file = "original.png"
    path = os.path.abspath('resources/%s' % image_file)

    # path to write and store coordinates of detected objects in img
    coord_path = os.path.abspath('coordinates/%s' % image_file + 'coordinate.txt')

    original_stdout = sys.stdout
    # Write object coordinates into a text file
    with open(coord_path, 'w') as f:
        sys.stdout = f
        # Calls Google API to return a response with object confidence rate and their coordinates
        localize_objects(path)
        sys.stdout = original_stdout
        f.close()


    # TODO: Call a library to create a copy of the image and using the JSON response draw onto new image the detected object


