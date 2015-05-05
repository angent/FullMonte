#!/usr/bin/env
# To run tests in a docker container:
# >$ docker-compose build && docker-compose run fullmontetests

# To profile, decorate functions with @profile
# kernprof -l FMMC.py tests/fixtures/astex_1g9v.mol
# python -m line_profiler FMMC.py.lprof > results.txt
# See https://github.com/rkern/line_profiler

import sys
import unittest

try:
    import FMMC
except ImportError, e:
    sys.stdout.write("Failed importing FMMC.\nAre libraries installed?\n'%s'\n" % e)
    sys.exit(1)

from tests.test_sdfwriter import TestSDFWriter
from tests.test_main      import TestFMMCMain

if __name__ == '__main__':
    unittest.main()