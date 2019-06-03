import sys
import os
import numpy as np

def progress_bar(progress, count ,message):
    sys.stdout.write('\r' + "{} of {}: {}".format(progress, count, message))