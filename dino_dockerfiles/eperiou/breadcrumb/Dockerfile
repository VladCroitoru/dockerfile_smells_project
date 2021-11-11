FROM kahatie/ionic

RUN mkdir -p /app
WORKDIR /app
COPY package.json /app/
COPY . /app
RUN apt-get -q update && apt-get install -y -qq \
   git \
   && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN  npm install
RUN npm install --quiet -g bower  \
   && npm cache clean
COPY bower.json /app/
RUN  bower install --allow-root


RUN cd /app
EXPOSE 8100 35729

CMD ionic serve --nolivereload --nogulp --lab
