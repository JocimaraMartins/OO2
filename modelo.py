class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return "Nome: {}\nAno: {}\nLikes {}".format(self._nome, self.ano, self._likes)

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "Nome: {}\nAno: {}\nDuração: {} minutos\nLikes {}".format(self._nome, self.ano, self.duracao, self._likes)

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return "Nome: {}\nAno: {}\nTemporadas: {}\nLikes {}".format(self._nome, self.ano, self.temporadas, self._likes)

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme("vingadores", 2018, 160)
perdido_em_marte = Filme("perdido em marte", 2015, 141)
interstellar = Filme("interstellar", 2014, 169)
minha_mae_e_uma_peca = Filme("minha mãe é uma peça", 2013, 85)

vingadores.nome = "vingadores: ultimato".title()

perdido_em_marte.dar_likes()
perdido_em_marte.dar_likes()
perdido_em_marte.dar_likes()
perdido_em_marte.dar_likes()
perdido_em_marte.dar_likes()
perdido_em_marte.dar_likes()
interstellar.dar_likes()
interstellar.dar_likes()
interstellar.dar_likes()
interstellar.dar_likes()
interstellar.dar_likes()
interstellar.dar_likes()
minha_mae_e_uma_peca.dar_likes()
minha_mae_e_uma_peca.dar_likes()
minha_mae_e_uma_peca.dar_likes()
minha_mae_e_uma_peca.dar_likes()
minha_mae_e_uma_peca.dar_likes()
minha_mae_e_uma_peca.dar_likes()
minha_mae_e_uma_peca.dar_likes()
minha_mae_e_uma_peca.dar_likes()
minha_mae_e_uma_peca.dar_likes()


the_big_Bang_theory = Serie("the big bang theory", 2007, 12)
the_good_place = Serie("the good place", 2016, 4)
how_i_met_your_mother = Serie("how i met your mother", 2005, 9)
good_girls = Serie("good girls", 2018, 4)
friends = Serie("friends", 1994, 10)





the_big_Bang_theory.dar_likes()
the_big_Bang_theory.dar_likes()
the_big_Bang_theory.dar_likes()
the_big_Bang_theory.dar_likes()
the_big_Bang_theory.dar_likes()
the_big_Bang_theory.dar_likes()
good_girls.dar_likes()
good_girls.dar_likes()
good_girls.dar_likes()
good_girls.dar_likes()
good_girls.dar_likes()
good_girls.dar_likes()
how_i_met_your_mother.dar_likes()
how_i_met_your_mother.dar_likes()
how_i_met_your_mother.dar_likes()
how_i_met_your_mother.dar_likes()
how_i_met_your_mother.dar_likes()
how_i_met_your_mother.dar_likes()
the_good_place.dar_likes()
the_good_place.dar_likes()
the_good_place.dar_likes()
the_good_place.dar_likes()
the_good_place.dar_likes()
the_good_place.dar_likes()
friends.dar_likes()
friends.dar_likes()
friends.dar_likes()
friends.dar_likes()
friends.dar_likes()
friends.dar_likes()

filmes_e_series = [vingadores, the_big_Bang_theory, perdido_em_marte, the_good_place, interstellar, how_i_met_your_mother, minha_mae_e_uma_peca, good_girls, friends]

playlist_maratonar = Playlist("Maratonar", filmes_e_series)

print("tamanho da playlist: {}".format(len(playlist_maratonar)))


print(playlist_maratonar[5])

len(playlist_maratonar)

for programa in playlist_maratonar:
    print(programa)


