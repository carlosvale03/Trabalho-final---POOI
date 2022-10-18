class Jogos:
    def __init__(self, data_hora, t_casa, t_visitante, compeonato):
        self._data_hora = data_hora
        self._time_casa = t_casa
        self._time_visitante = t_visitante
        self._campeonato = compeonato

    def __str__(self):
        return f'[{self.data_hora}, {self.time_casa}, {self.time_visitante}, {self.campeonato}]'

    @property
    def data_hora(self):
        return self._data_hora

    @property
    def time_casa(self):
        return self._time_casa

    @property
    def time_visitante(self):
        return self._time_visitante

    @property
    def campeonato(self):
        return self._campeonato