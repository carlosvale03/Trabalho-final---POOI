import abc

class Iarrecadacao(abc.ABC):

    @abc.abstractmethod
    def arrecada(self): 
        '''Método abstrato para arrecadar os valores.
        Esse método vai retornar cada valor arrecadado.'''