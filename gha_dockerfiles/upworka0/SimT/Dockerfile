FROM ubuntu:latest
MAINTAINER jeff labonte "jflabonte@ideoconcepts.ca"

ENV MYSQL_IP_ADDRESS=172.18.0.3

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev libmysqlclient-dev locales apt-utils \
    && apt-get -y dist-upgrade \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && ln -s /usr/bin/pip3 pip \
    && pip3 install --upgrade pip \
    && mkdir /code

RUN apt install -y nodejs npm

WORKDIR /code
COPY simbt /code
COPY changeIpAddress.sh /usr/local/bin/

ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
VOLUME /code
RUN chmod 777 /usr/local/bin/changeIpAddress.sh \
    && ln -s /usr/local/bin/changeIpAddress.sh /

#Set the locale
RUN locale-gen en_CA.UTF-8  
ENV LANG en_CA.UTF-8  
ENV LANGUAGE en_CA:en  
ENV LC_ALL en_CA.UTF-8  

EXPOSE 8000
ENTRYPOINT ["changeIpAddress.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
