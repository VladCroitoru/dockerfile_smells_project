FROM python:3
MAINTAINER nsdont "haodewanan@gmail.com"

RUN apt-get -qq update

RUN apt-get install -y build-essential binutils-doc autoconf flex bison libjpeg-dev
RUN apt-get install -y libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev libncurses5-dev
RUN apt-get install -y automake libtool libffi-dev curl git tmux
RUN apt-get install -y rabbitmq-server redis-server

RUN apt-get install --no-install-recommends -y -q  nodejs npm ruby
RUN apt-get install -y python-dev python-setuptools git-core locales python-pip
RUN apt-get install -y libxml2-dev libxslt-dev
RUN pip2 install circus
RUN gem install sass scss-lint
RUN npm install -g gulp bower
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN echo "LANG=en_US.UTF-8" > /etc/default/locale
RUN echo "LC_MESSAGES=POSIX" >> /etc/default/locale
RUN echo "LANGUAGE=en" >> /etc/default/locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN mkdir -p /taiga/logs

# install taiga front
WORKDIR /taiga
RUN git clone https://github.com/taigaio/taiga-front.git front
WORKDIR /taiga/front
RUN git checkout stable
RUN npm install
RUN bower install --allow-root
RUN gulp deploy

# install taiga back
WORKDIR /taiga
RUN git clone https://github.com/taigaio/taiga-back.git backend
WORKDIR /taiga/backend
RUN git checkout stable
RUN pip install -r /taiga/backend/requirements.txt
RUN python manage.py collectstatic --noinput

# install taiga events
WORKDIR /taiga
RUN git clone https://github.com/taigaio/taiga-events.git events
WORKDIR /taiga/events
RUN git checkout stable
RUN pip install -r /taiga/backend/requirements.txt

RUN (echo "alias ll='ls -atrhlF'" >> ~/.bashrc)

VOLUME ["/taiga"]

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
