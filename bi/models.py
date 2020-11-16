from django.db import models


PERSONALITY = (
    ('I', 'Inpulsivo'),
    ('E', 'Exigente'),
    ('C', 'Cauteloso'),
    ('A', 'Aleatório'),
)


class Board(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tabuleiro'
        verbose_name_plural = 'Tabuleiros'
        ordering = ['name',]


class Property(models.Model):
    name = models.CharField(max_length=255,verbose_name='Nome da propriedade', blank=True, null=True)
    board = models.ForeignKey(Board, models.CASCADE, related_name='board', verbose_name='Tabuleiro')
    to_buy = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    to_rent = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Propriedade'
        verbose_name_plural = 'Propriedades'


class Player(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    personality = models.CharField(max_length=50, choices=PERSONALITY, verbose_name='Personalidade')
    purchase_balance = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Saldo', blank=False, null=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
        ordering = ['name',]
