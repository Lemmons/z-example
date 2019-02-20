#!/usr/bin/env python3

import my_module.sub_module_2.yo
import sys

def main():
    my_module.sub_module_2.yo.whatup(sys.argv[1])

if __name__ == "__main__":
    main()
