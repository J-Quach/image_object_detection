import io
import os


# [START vision_localize_objects]
def localize_objects(path):
    """Localize objects in the local image.
    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
# [END vision_localize_objects]



if __name__ == "__main__":

    # File directory
    path = os.path.abspath('resources/wakeupcat.jpg')

    # Calls Google API to return a response with object confidence rate and their coordinates
    localize_objects(path)

    # TODO: Call a library to create a copy of the image and using the JSON response draw onto new image the detected object


