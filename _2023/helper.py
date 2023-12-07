from typing import List

def read_file(file_name:str = 'data.txt') -> List[str]:
    """reads in a file and returns an list with each
    line as an entry in the list

    Args:
        file_name (str, optional): file name. Defaults to 'data.txt'.

    Returns:
        list[str]: list of lines in the file
    """
    ret_val = []
    with open(file_name) as f:
        ret_val = f.readlines()
    return [line.replace('\n', '').strip() for line in ret_val]
