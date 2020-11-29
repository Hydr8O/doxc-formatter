from zipfile import ZipFile
from pathlib import Path
from django.conf import settings

class ImageExtractor:
    '''Extract images in docx files'''
    def __init__(self, path_to_file):
        self.document = ZipFile(path_to_file, 'r')
        self.image_paths = self.__get_images()
        Path(settings.MEDIA_ROOT / 'images').mkdir(parents=True, exist_ok=True)
    

    def extract_images(self):
        '''Extracts an image from docx'''
        image_names = []
        image_folder = Path(settings.MEDIA_ROOT / 'images')
        for image_path in self.image_paths:
            image = self.document.open(image_path).read()
            image_name = image_path.split('/')[-1]
            image_names.append(image_name)
            with open(image_folder / image_name, 'wb') as file:
                file.write(image)
        return image_names

    def __get_images(self):
        '''Returns list of image paths in docx'''
        all_files = self.document.namelist()
        image_paths = list(filter(lambda x: x.startswith('word/media/'), all_files))
        return image_paths

    
