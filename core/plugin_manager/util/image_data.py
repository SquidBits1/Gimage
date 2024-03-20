"""
image_data.py -
This file contains the ImageData class, which contains the image queue. The image queue contains iterations of edited
images so that edits can be undone.
"""

from collections import deque


class ImageData:
    """
    Represents the image data of an image.
    The main part of this class is the processed_image_data deque that contains the image queue.
    """

    def __init__(self, filepath='No Image Loaded', source_image_data=None):
        """
        :param filepath: The name of the file loaded in
        :param source_image_data: The image data before editing of a file loaded in
        """
        self.source_filepath = filepath
        self.filetype = None
        self.has_edited_image = False
        self.maxlength = 8
        self.source_image_data = source_image_data
        # Using the deque data structure, images that are before 4 edits get deleted automatically
        self.image_queue = deque([self.source_image_data], maxlen=self.maxlength)

        self.filename = self.source_filepath.split('/')[-1]
        self.extensionless = self.filename.split('.')[0]

    def add_image(self, image_data):
        """
        Adds an image to the deque
        :param image_data: numpy image data
        :return:
        """
        self.has_edited_image = True
        self.image_queue.append(image_data)

    def undo_change(self):
        """
        Removes item in index [-1] from the processed_image_data
        :return:
        """
        if len(self.image_queue) < 2:
            raise IndexError('Image has not been edited')

        self.image_queue.pop()

    def __repr__(self):
        """
        ImageData class is represented by the filename
        :return:
        """
        return self.filename
