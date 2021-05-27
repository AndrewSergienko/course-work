from zope.interface import Interface, Attribute


class IRender(Interface):

    def render(self):
        pass


