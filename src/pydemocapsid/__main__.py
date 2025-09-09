#!/usr/bin/env python3

import sys

from .cli import parse_args
from .democapsid import main

main(parse_args(sys.argv[1:]))
