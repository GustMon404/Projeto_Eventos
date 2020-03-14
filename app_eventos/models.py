from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome',max_length = 128)
    email = models.EmailField('E-mail', null=True, blank = True)

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.IntegerField()
    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField('Nome',max_length = 128)
    sigla = models.CharField('Sigla',max_length = 128)
    data_inicio = models.DateTimeField('Data de Inicio',blank=True, null = True)
    realizador = models.ForeignKey(Pessoa, on_delete = models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Ingresso(models.Model):
    descricao = models.CharField('Descrição',max_length = 128)
    valor = models.DecimalField('Valor',decimal_places = 2,max_digits = 4)
    evento = models.ForeignKey(Evento, on_delete = models.CASCADE)

    def __str__(self):
        return self.descricao

class Inscricao(models.Model):
    pessoa = models.OneToOneField(Pessoa,on_delete = models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete = models.CASCADE)
    ingresso = models.ForeignKey(Ingresso,  on_delete = models.CASCADE)


# Create your models here.