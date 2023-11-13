import chardet

def verdict_file_encode(file_path):
    """
    Function to encode the verdict file
    :param file_path: path to the verdict file
    :return: encoded verdict file
    """
    with open(file_path, 'rb') as f:
        content = f.read()
        return chardet.detect(content)['encoding']

def euckr2utf8(file_path):
    """
    Function to convert euckr to utf-8
    :param file_path: path to the verdict file
    :return: utf-8 encoded verdict file
    """
    with open(file_path, 'rb') as f:
        content = f.read()
        return content.decode('euc-kr').encode('utf-8')

def find_files(path, extension):
    """
    Function to find files with specific extension
    :param extension: file extension
    :return: list of files with specific extension
    """
    import os
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    return file_list


if __name__ == '__main__':
    for file in find_files('./', '.properties'):
        if verdict_file_encode(file) == 'EUC-KR':
            print('Encoding file: ' + file)
            raw = euckr2utf8(file)
            with open(file, 'wb') as f:
                f.write(raw)