FROM ubuntu
MAINTAINER  ylzmax


RUN apt-get update  && apt-get install -y git python-paramiko python-pip
RUN pip install django==1.8 
RUN pip install django-crontab
RUN cd /opt && git clone https://github.com/ylzmax/vncmanager
#RUN python /opt/vncmanager/manage.py migrate
#ENTRYPOINT ["cd /opt/vncmanager &&python manage.py runserver 80"]
