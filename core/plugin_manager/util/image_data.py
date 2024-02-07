from collections import deque


class ImageData:

    def __init__(self, filename='No Image Loaded', source_image_data=None):
        self.source_filename = filename
        self.filetype = None
        self.has_image = False

        self.source_image_data = source_image_data
        # Using the deque data structure, images that are before 4 edits get deleted automatically
        self.processed_image_data = deque([self.source_image_data], maxlen=4)

        self.image_height = None
        self.image_width = None

        self._process()

    def _process(self):
        self.no_path = self.source_filename.split('/')[-1]
        self.no_extension = self.no_path.split('.')[0]

    def add_image(self, image_data):
        self.has_image = True
        self.processed_image_data.append(image_data)

    def undo_change(self):
        if len(self.processed_image_data) < 2:
            raise IndexError('Image has not been edited')

        self.processed_image_data.pop()

    def __repr__(self):
        return self.no_path
