#!c:\users\lenovo\git\phoebe7979\intermediate-python\project3\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'coverage==3.7.1','console_scripts','coverage'
__requires__ = 'coverage==3.7.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('coverage==3.7.1', 'console_scripts', 'coverage')()
    )
