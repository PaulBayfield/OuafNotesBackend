__version__ = "v1.0.0"
__title__ = "OuafIntranet"
__author__ = "Paul Bayfield"



from .client import Client
from .objects import *
from .exceptions import *

from .utils import getMatiere, getCompetenceByMatiere