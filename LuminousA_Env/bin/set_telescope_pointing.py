#!/Users/promisedland/Desktop/CompSci/My_Github/LuminousAccumulation/LuminousA_Env/bin/python3.11
# -*- coding: utf-8 -*-
import re
import sys
from jwst.scripts.set_telescope_pointing import deprecated_name
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(deprecated_name())
