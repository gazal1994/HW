class FileType:
    def __init__(self, file_type, file_category, file_description):
        self.file_type = file_type
        self.file_category = file_category
        self.file_description = file_description

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value

    @property
    def file_category(self):
        return self._file_category

    @file_category.setter
    def file_category(self, value):
        self._file_category = value

    @property
    def file_description(self):
        return self._file_description

    @file_description.setter
    def file_description(self, value):
        self._file_description = value
