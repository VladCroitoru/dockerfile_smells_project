FROM node:5.5.0-wheezy

ADD . /home

RUN apt-get update -y && \
    apt-get install zip unzip -y && \
    apt-get clean && \
    cd /home; npm install --production

EXPOSE 3000

CMD /bin/bash -c 'cd /home; node src/service.js -v -t $SECURE_TOKEN -m $MONGO_URL'