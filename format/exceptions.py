class TooLargeFileException(Exception):
    def __init__(self):
        self.message = 'The size of the file is too large'

    def __str__(self):
        return self.message


class WrongFileExtensionException(Exception):
    def __init__(self):
        self.message = 'Please, upload a docx file'

    def __str__(self):
        return self.message
