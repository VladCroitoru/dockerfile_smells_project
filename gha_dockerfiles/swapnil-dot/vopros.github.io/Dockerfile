
FROM python

MAINTAINER Swapnil Chandra

RUN apt-get update && apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get update && apt-get install nginx -y
RUN apt-get update && apt-get install git
RUN apt-get install python3-pip -y
RUN python -m pip install django

RUN git clone https://github.com/swapnil-dot/vopros.github.io.git
WORKDIR /vopros.github.io
RUN pip install -r requirements.txt
CMD ["python3","manage.py","makemigrations"]
CMD ["python3","manage.py","migrate"]
CMD ["python3","manage.py","collectstatic","--noinput"]
CMD ["python3","manage.py","runserver","0.0.0.0:8080"]
EXPOSE 8080
