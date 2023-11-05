image_formats = {'bmp', 'cur', 'gif', 'icns', 'ico', 'jpeg', 'jpg', 'pbm', 'pgb', 'png', 'ppm', 'svg', 'svgz', 'tga',
                 'tif', 'tiff', 'wbmp', 'webp', 'xbm', 'xpm'
                 }


def is_valid_image_file(filename):
    valid = False
    image_format = None

    if not filename or '.' not in filename:
        valid = False
    elif filename.split('.')[1] not in image_formats:
        valid = False
    else:
        valid = True
        image_format = filename.split('.')[1]

    return valid, image_format



