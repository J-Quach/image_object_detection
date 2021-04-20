import io
import os

from detect import localize_objects


if __name__ == "__main__":

    # File directory
    path = os.path.abspath('resources/wakeupcat.jpg')

    # Calls Google API to return JSON coordinate results and identifies objects
    localize_objects(path)

    # TODO: Call a library to create a copy of the image and using the JSON response draw onto new image the detected object

    