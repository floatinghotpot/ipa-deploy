# -*- coding: utf-8; py-indent-offset:4 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import sys

__version__ = '2.0.1'

__hqversion__ = tuple(int(x) for x in __version__.split('.'))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'bump':
        fp = open(__file__, 'r')
        lines = fp.readlines()
        fp.close()

        text = ''
        for line in lines:
            if line.startswith('__version__'):
                items = line.split("'")
                current_version = items[1]
                vers = items[1].split('.')
                vers[-1] = str(int(vers[-1]) +1)
                new_version = items[1] = '.'.join(vers)
                line = "'".join(items)
            text += line

        fp = open(__file__, 'w')
        fp.write(text)
        fp.close()
        print('Current version:', current_version)
        print('Bumped to:', new_version)
        print('File updated:', __file__, '\n')
