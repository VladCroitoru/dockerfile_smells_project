# VERSION 1.0
FROM dockercisco/acitoolkit
MAINTAINER Chad Peterson, chapeter@cisco.com

#install tools
#RUN apt-get update
RUN apt-get install python-dev
RUN apt-get -y install autoconf g++ python2.7-dev libxml2-dev libxslt1-dev zlib1g-dev
RUN apt-get -y install build-essential libssl-dev
RUN apt-get -y install libffi-dev
#RUN apt-get -y install git python-pip 
RUN pip install --upgrade pip


#Testing here
RUN pip install GitPython
RUN pip install Jinja2
RUN pip install MarkupSafe
RUN pip install PyMySQL
RUN pip install SQLAlchemy
RUN pip install WTForms
RUN pip install argparse
RUN pip install dominate
RUN pip install ecdsa
RUN pip install gitdb
RUN pip install ipaddress
RUN pip install itsdangerous
RUN pip install lxml
RUN pip install ncclient
RUN pip install nxosNCRPC
RUN pip install paramiko
RUN pip install pycrypto
RUN pip install six
RUN pip install smmap
RUN pip install tabulate
RUN pip install visitor
RUN pip install websocket-client


#install download and run acimigrate
WORKDIR /opt
RUN git clone http://github.com/chapeter/acimigrate
WORKDIR acimigrate
#RUN pip install -r requirements.txt
FROM dockercisco/acitoolkit 
MAINTAINER Chad Peterson, chapeter@cisco.com

WORKDIR /opt
RUN git clone http://github.com/chapeter/acimigrate
WORKDIR acimigrate
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "python", "./main.py" ]
