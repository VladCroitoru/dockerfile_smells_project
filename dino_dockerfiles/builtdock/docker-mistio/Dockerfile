FROM ubuntu:14.04

MAINTAINER cloud.admin@builtdock.com

RUN apt-get update

RUN apt-get install -y python-dev build-essential git erlang libpcre3-dev

RUN apt-get install -y python-virtualenv

## create a homedir for mist code and create an user because mist doesnt run as root 
## memcaches wont work ,etc also more secure to run as a different user

RUN mkdir -p /home/mist
 
RUN useradd mist

RUN chown mist:mist /home/mist -R

## fetch source
RUN git clone https://github.com/mistio/mist.io.git /home/mist

### run the mist in a virtualenv as adviced by their github page
RUN cd /home/mist && virtualenv --no-site-packages .

RUN cd /home/mist && ./bin/python bootstrap.py

RUN cd /home/mist && ./bin/buildout -v

## after compiling as root change all files to the mist user
RUN chown mist:mist /home/mist -R

## start the supervisor as a mist user and thats it 
CMD su -c "/home/mist/bin/supervisord -n" mist
