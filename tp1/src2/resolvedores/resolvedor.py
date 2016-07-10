import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from abc import ABCMeta, abstractmethod

class Resolvedor(object):
    __metaclass__ = ABCMeta

    def continuarConFallo(self, unTurno, unSimulador):
        pass

    def continuarConExito(self, unaAccion, unTurno, unSimulador):
        pass
