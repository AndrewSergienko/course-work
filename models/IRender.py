import sys
sys.path.insert(0, 'packages/')
from zope.interface import Interface


class IRender(Interface):

    def render():
        pass


