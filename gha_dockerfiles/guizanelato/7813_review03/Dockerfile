#1: indicar a imagem linux base
FROM python:3.6-alpine

#2: instalar as dependencias a nível de aplicação
#2.1 cópia do arquivo de dependencias
COPY ./requirements.txt /tmp

#2.2 instalação através do pip
RUN pip install -r /tmp/requirements.txt

#3. preparar diretório da app

RUN mkdir /app

#4. mudar o diretório padrão
WORKDIR /app

#5. copiar a app para conteiner
ADD app /app

#6. exportar flask na porta 5000
EXPOSE 5000

#7. qual o comando que o container vai executar 
# Entrypoint

CMD python app.py


