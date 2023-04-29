import os
import shutil

from FileType import FileType

directory_path = 'input-dir'


def get_file_type(filename):
    extension = os.path.splitext(filename)[1].upper().replace(".", "")
    file_types = {
        'Text files': {
            'TXT': 'Plain text file',
            'HTML': 'Web page file',
            'CSS': 'Stylesheet file',
            'XML': 'Data interchange format file',
            'Markdown': 'Lightweight markup language file'
        },
        'Document files': {
            'DOC': 'Microsoft Word document file',
            'DOCX': 'Microsoft Word document file',
            'ODT': 'OpenDocument Text file',
            'RTF': 'Rich Text Format file',
            'PDF': 'Portable Document Format file'
        },
        'Spreadsheet files': {
            'XLS': 'Microsoft Excel spreadsheet file',
            'XLSX': 'Microsoft Excel spreadsheet file',
            'ODS': 'OpenDocument Spreadsheet file',
            'CSV': 'Comma-separated values file'
        },
        'Image files': {
            'JPG': 'Joint Photographic Experts Group file',
            'JPEG': 'Joint Photographic Experts Group file',
            'PNG': 'Portable Network Graphics file',
            'GIF': 'Graphics Interchange Format file',
            'BMP': 'Bitmap file',
            'TIFF': 'Tagged Image File Format file'
        },
        'Audio files': {
            'MP3': 'MPEG-1 Audio Layer III file',
            'WAV': 'Waveform Audio file',
            'AIFF': 'Audio Interchange File Format file',
            'FLAC': 'Free Lossless Audio Codec file'
        },
        'Video files': {
            'MP4': 'MPEG-4 video file',
            'AVI': 'Audio Video Interleave file',
            'WMV': 'Windows Media Video file',
            'MOV': 'QuickTime movie file',
            'FLV': 'Flash video file'
        },
        'Other files': {
            'ZIP': 'Compressed archive file',
            'RAR': 'Compressed archive file',
            'ISO': 'Disc image file',
            'EXE': 'Executable file',
            'DLL': 'Dynamic link library file'
        }
    }
    for i in file_types:
        if file_types.get(i).get(extension) is not None:
            return FileType(extension, i, file_types.get(i).get(extension))


def read_files():
    for filename in os.listdir(directory_path):
        file_type = get_file_type(filename)
        get_create_category_dir(f'{file_type.file_category}/{file_type.file_type}')
        move_file_to_dir(f'{directory_path}/{filename}', f'{file_type.file_category}/{file_type.file_type}')
        print(
            f'"Type ": {file_type.file_type}, " Category ": {file_type.file_category}, " description ": {file_type.file_description}')


def get_create_category_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def move_file_to_dir(file_path, directory):
    shutil.move(file_path, directory)


if __name__ == '__main__':
    read_files()
