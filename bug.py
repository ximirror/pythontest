
import io


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
        pos = line.find('=')
        print (f"position = {pos}")
        if pos == -1:
            continue
        component: str = line[0:pos+1]  # >abcd =< 1234
        version: str = line[pos+2:len(line)] # abcd = >1234<
        print(f"{component} : {version}")

    ## break:
    file.close()


if __name__ == "__main__":
    read_file("ricard.txt")
