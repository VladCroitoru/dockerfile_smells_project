FROM node

RUN  apt-get update -y  \
     && apt-get install -y vim \
     && apt-get install -y git
     
      
WORKDIR /opt
RUN git clone https://github.com/timeoff-management/application.git  timeoff-management


ENV WORK_DIR=/opt/timeoff-management
WORKDIR $WORK_DIR
RUN git checkout v0.6.2

ADD  application/views/partials/footer.hbs  /opt/timeoff-management/views/partials/footer.hbs
ADD  application/views/partials/header.hbs  /opt/timeoff-management/views/partials/header.hbs
ADD  application/views/index.hbs  /opt/timeoff-management/views/index.hbs

RUN npm install mysql && npm install


EXPOSE 3000
VOLUME /opt/timeoff-management/config
ADD docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT [ "bash", "/docker-entrypoint.sh"]
