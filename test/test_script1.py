#include parent folder 
import os,sys,inspect 
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))) 

import pytest

from scripts.common import *


def test_paths():
    os.path.exists(DIR_ROOT)
    os.path.exists(DIR_OUT)



if __name__ == "__main__":
    test_paths()