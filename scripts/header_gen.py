#!/usr/bin/env python

import inspect
import os

dirname = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


def main():
    header = os.path.join(dirname, "../include/dumux/dumux.h")

    with open(header, "w") as header_file:
        header_file.write("#ifndef INCLUDE_DUMUX_DUMUX_H_\n")
        header_file.write("#define INCLUDE_DUMUX_DUMUX_H_\n")

        for path, dirs, files in os.walk("../include/dumux/"):

            for file in files:
                if file.split('.')[-1] == "hh" or file.split('.')[-1] == "h" and file != "dumux.h":
                    path_temp = path.split('/')[3:]
                    header_path = ""
                    for name in path_temp:
                        header_path = header_path + "/" + name

                    header_file.write(f"#include \"{header_path[1:]}/{file}\"\n")

        header_file.write("#endif  // INCLUDE_DUMUX_DUMUX_H_\n")
    header_file.close()


if __name__ == "__main__":
    main()
