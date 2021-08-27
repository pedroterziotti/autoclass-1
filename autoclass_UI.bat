@echo off 
ECHO \n \n Essa parte do programa so server para configurar suas aulas. Pode fechar assim que terminar de configurar elas \n \n
START http://127.0.0.1:8000
python autoclass\manage.py runserver