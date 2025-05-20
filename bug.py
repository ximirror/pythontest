
import io
import string
import time
from platform import system


def read_file(path: str) -> None:
    """
    prints out the component and version like this
    1.comp : 1.version
    2.comp : 2.version
    ...
    :param path:
    :return:
    """
    file = open(path, "r")

    ## continue:
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        ## when break it stops and go to 'file.close ()
        pos = line.find('=')
        ## search line with = symbol
        if not pos == -1:
            print(f"position = {pos}")
            component: str = line[0:pos-1]  # >abcd =< 1234
            ##output first character till = sign
            version: str = line[pos+2:len(line)] # abcd = >1234<
            print(f"{component} {version}")
            component_strip= component.strip()
            version_strip= version.strip()
            print (f"{component_strip} {version_strip}")




    ## break:
    file.close()

def replace_s(_str: str, previous_pos = 0) -> str:
    pos =_str.lower().find('s')
    if not pos == -1:
        print(_str[previous_pos:pos], end="")
        return replace_s(_str[0:pos] + '_' + _str[pos+1:len(_str)], pos)
    print(_str[previous_pos:len(_str)])
    return _str

if __name__ == "__main__":
    read_file("ricard.txt")
    #replace_s("These SSses shall be safely replaced") ## function would be called
    print (replace_s("These SSses shall be safely replaced"))
    new_string = replace_s("These SSses shall be safely replaced")
    print(new_string)




