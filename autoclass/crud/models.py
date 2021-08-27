from django.db import models
import datetime
from django.core.validators import MaxValueValidator
import time

from django.db.models.fields.related import ManyToManyField
# Create your models here.


PLATAFORMAS_DISPONIVEIS= ('Zoom','Blackboard','Teams','Classroom')

WEEK_DAY_TUPLE=('Segunda','Terça','Quarta','Quinta','Sexta','Sabado','Domingo')

class Aula(models.Model):
    '''Classe que representa o bjeto aulça na base de dados'''

    nome =models.CharField(max_length=300)

    plataforma = models.CharField(max_length=22, choices=zip(PLATAFORMAS_DISPONIVEIS,PLATAFORMAS_DISPONIVEIS),default='Teams')

    dia_da_aula= models.CharField(choices=zip(WEEK_DAY_TUPLE,WEEK_DAY_TUPLE),max_length=20,default=WEEK_DAY_TUPLE[datetime.datetime.today().weekday()])
    
    horario_de_inicio=models.TimeField(default=datetime.datetime.now)

    duracao_da_aula_minutos= models.PositiveSmallIntegerField(validators=[MaxValueValidator(600,message='Sua aula deve durar menos de 10 horas')],default=90)

    link = models.URLField(default='https://teams.microsoft.com/_?tenantId=e1d017cf-c2a8-456e-8bb9-4199fc1d75bf#/conversations/Geral?threadId=19:Sk1-OVIVySVukhzW6i3uV5dw9_YbqpJOM14QIevik-41@thread.tacv2&ctx=channel')

    login = models.CharField(max_length=300,default="")
    
    senha = models.CharField(max_length=30, null=False,default='') 