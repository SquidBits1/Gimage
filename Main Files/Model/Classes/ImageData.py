class ImageData:

    def __init__(self, filename, source_image_data):
        self.source_filename = filename
        self.filetype = None

        self.source_image_data = source_image_data
        self.processed_image_datas = [None]

        self.image_height = None
        self.image_width = None

        self._process()

    def _process(self):
        self.no_path = self.source_filename.split('/')[-1]
        self.no_extension = self.no_path.split('.')[0]

    def add_image(self, image_data):
        self.processed_image_datas[0] = image_data

    def __repr__(self):
        return self.no_path
