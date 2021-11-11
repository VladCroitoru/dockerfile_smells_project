FROM node:7
RUN mkdir /pickUp
ADD . /pickUp
WORKDIR /pickUp
RUN apt-get -q update && apt-get install -y -qq \
   git \
   && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN  npm i
RUN npm i --quiet -g bower  \
   && npm cache clean
COPY bower.json .
RUN  bower install --allow-root
RUN npm i -g grunt-cli
EXPOSE 7000
CMD ["grunt", "bypass"]
