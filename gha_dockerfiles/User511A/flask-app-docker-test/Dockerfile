#FROM ubuntu:latest
#RUN apt-get update -y
#RUN apt-get install -y python3.9 python3-pip python3-dev #проверить
#COPY . /app
#WORKDIR /app
#RUN pip3 install -r requirements.txt
#ENTRYPOINT ['python3'] #выдает ошибку - проверить
#CMD ['main.py'] #проверить

#FROM ubuntu:16.04
#MAINTANER Your Name "youremail@domain.tld"
#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev
#your Dockerfile is missing this line
#COPY ./requirements.txt /app/requirements.txt
#WORKDIR /app
#RUN pip install -r requirements.txt
#COPY . /app
#ENTRYPOINT [ "python" ]
#CMD [ "app.py" ]

FROM python:3.4-alpine 
ADD . /app 
WORKDIR /app 
RUN pip install -r requirements.txt 
CMD ["python", "main.py"]
