FROM node:9.2

#install rethinkdb rabbitmq yarn
RUN echo "deb http://download.rethinkdb.com/apt jessie main" | tee /etc/apt/sources.list.d/rethinkdb.list && \
    curl https://download.rethinkdb.com/apt/pubkey.gpg | apt-key add - && \
    echo 'deb http://www.rabbitmq.com/debian/ testing main' | tee /etc/apt/sources.list.d/rabbitmq.list && \
    curl https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key add - && \
    echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -

RUN wget http://www.dotdeb.org/dotdeb.gpg && apt-key add dotdeb.gpg
RUN echo 'deb http://ftp.utexas.edu/dotdeb/ stable all' >> /etc/apt/sources.list
RUN echo 'deb-src http://ftp.utexas.edu/dotdeb/ stable all'  >> /etc/apt/sources.list

# Add the latest stable redis ppa.
#RUN apt-get install -y -qq python-software-properties
# RUN add-apt-repository ppa:chris-lea/redis-server

RUN apt-get update && apt-get upgrade -y && apt-get install -y software-properties-common yarn rabbitmq-server rethinkdb redis-server 

# Copy the rethinkdb configuration to start it with init.d
ADD rethinkdb.conf /etc/rethinkdb/instances.d/instance1.conf

#gosu
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

