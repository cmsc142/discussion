"""
package docstring here
"""
# star means import all names
# .queue represents the subdirectory queue, and within that subdirectory
# there is another __init__.py that imports all the names from queue.py
# main benefit is you can directly access StatelessQueue without doing
# cmsc142.queue.StatelessQueue

from .misc import *
from .queue import *
from .stack import *