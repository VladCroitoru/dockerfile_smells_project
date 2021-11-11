FROM ubuntu:14.04
MAINTAINER hlxnd
VOLUME ["/home/kallithea/"]
ENV kpass admin
ENV kemail admin@nowhere.com
RUN useradd kallithea

RUN apt-get update
RUN apt-get update --fix-missing
RUN apt-get upgrade -y

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev python-pip \
        python-virtualenv virtualenvwrapper git

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y curl

# This will get hg
RUN pip install --upgrade pip setuptools
RUN pip install kallithea
EXPOSE 5000
ADD ./setup_kallithea.sh /
WORKDIR /home/kallithea
CMD bash /setup_kallithea.sh
