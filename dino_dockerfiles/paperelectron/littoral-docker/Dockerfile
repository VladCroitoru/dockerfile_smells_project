#Get baseimage up and running.

FROM phusion/baseimage:0.9.16

RUN apt-get update && apt-get -y install \
  build-essential \
  curl

RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo 'deb https://deb.nodesource.com/node012 trusty main' > /etc/apt/sources.list.d/nodesource.list && \
  echo 'deb-src https://deb.nodesource.com/node012 trusty main' >> /etc/apt/sources.list.d/nodesource.list  

RUN apt-get update && apt-get install -y nodejs && node -v && npm -v
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LITTORAL_HOME /var/littoral
ENV LITTORAL_ROUTES $LITTORAL_HOME/.littoral

# If you bind mount a volume from host/volume from a data container, 
# ensure you use same uid

RUN useradd -d "$LITTORAL_HOME" -u 1000 -m -s /bin/bash littoral

RUN mkdir /etc/service/littoral
ADD littoral.sh /etc/service/littoral/run

EXPOSE 8080

WORKDIR $LITTORAL_HOME
RUN npm install -g littoral && \
  mkdir .littoral 

VOLUME $LITTORAL_ROUTES
RUN chown -R littoral "$LITTORAL_HOME"
CMD ["/sbin/my_init"]
