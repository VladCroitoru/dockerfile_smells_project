FROM  ubuntu

#RUN   apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
RUN   echo 'deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list
RUN   sed -i 's/main$/main universe/' /etc/apt/sources.list

#Packages
RUN   apt-get update
RUN   apt-get install git-core python-pip build-essential python-dev libevent1-dev mongodb-10gen rabbitmq-server python-dev wget build-essential supervisor -y --force-yes

#RabbitMQ
RUN   /usr/lib/rabbitmq/bin/rabbitmq-plugins enable rabbitmq_stomp
RUN   /usr/lib/rabbitmq/bin/rabbitmq-plugins enable rabbitmq_management

RUN mkdir -p /data/db/

ADD docker/alerta.conf /root/alerta.conf
ADD docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

ADD . /alerta
RUN cd /alerta && pip install -r requirements.txt && python setup.py install

RUN chmod +x /alerta/bin/alerta-dashboard

EXPOSE 8080
EXPOSE 5000 
EXPOSE 27017
EXPOSE 5672 15672

CMD ["supervisord", "-n"]
