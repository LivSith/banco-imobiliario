# Banco Imobiliário

Jogo desenvolvido em Python3.5 e Django 2.2.

Uma execução do programa roda 300 simulações, imprime no console os dados referentes
às execuções. 
Mostrando as seguintes informações:
 - Quantas partidas terminam por time out (1000 rodadas);
 - Quantos turnos em média demora uma partida;
 - Qual a porcentagem de vitórias por comportamento dos jogadores;
 - Qual o comportamento que mais vence.


 ## Como rodar esta simulação?

1. Clone este repositorio.

2. Vá para a pasta do projeto.

>```
> $ cd banco-imobiliario/
>```

3. Criar uma maquina virtual chamada 'myvenv', dentro da pasta;

>```
> $ python3 -m venv myvenv
>```

4. Ativar maquina virtual;

>```
> $ source myvenv/bin/activate
>```


5. Instalar os requisitos do ambiente;
>```
>$ pip install -r requirements.txt
>```

6. Banco de dados;
>```
>$ python manage.py migrate
>```

7. Servidor local;
>```
>$ python manage.py runserver
>```

8. Abrir o navegador e acessar o servidor local. http://127.0.0.1:8000/


9. E começar a usar \0/