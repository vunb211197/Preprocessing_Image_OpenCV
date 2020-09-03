import argparse

def getArgument():
    arg = argparse.ArgumentParser()
    # định nghĩa một tham số cần parse
    arg.add_argument('-i', '--image_path',
                     help='link to image')
    # Giúp chúng ta convert các tham số nhận được thành một object và gán nó thành một thuộc tính của một namespace.
    return arg.parse_args()