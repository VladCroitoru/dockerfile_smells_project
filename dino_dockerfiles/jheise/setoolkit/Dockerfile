FROM ubuntu:latest

RUN apt-get update && apt-get --force-yes -y install git apache2 python-requests libapache2-mod-php python-pymssql build-essential python-pexpect python-pefile python-crypto python-openssl

RUN git clone https://github.com/trustedsec/social-engineer-toolkit/ /opt/set
WORKDIR /opt/set
RUN python setup.py install
CMD setoolkit
