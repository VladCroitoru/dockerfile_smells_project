FROM python:2.7.11

ENV PYTHONUNBUFFERED 1
ENV TERM=xterm

RUN add-apt-repository ppa:ondrej/php5-5.6
RUN apt-get update
RUN apt-get install python-software-properties

RUN apt-get update
RUN apt-get -y install php5 wget xz-utils build-essential openssl libssl-dev rsync mysql-client vim

# install easy_install then pip
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - > garb.py
RUN python2.7 garb.py

# pip
RUN /usr/local/bin/easy_install-2.7 pip

# install small base of modules to support code delivery - fabric, pythongit
ADD requirements.txt .
RUN /usr/local/bin/pip install -r ./requirements.txt

# a couple of mount points to link volumes
RUN mkdir /php-apps
RUN mkdir /python-apps
RUN mkdir /sql
RUN mkdir /backups
RUN rm requirements.txt garb.py setuptools-24.0.0.zip
# check php version
RUN php -v
