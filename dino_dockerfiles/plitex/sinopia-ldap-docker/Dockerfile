# Pull base image.
FROM rnbwd/node-io:1.7.1

MAINTAINER PliTeX <plitex@gmail.com>

# Sinopia Version / Path / Backup

ENV version master

RUN git clone https://github.com/plitex/sinopia.git
WORKDIR /sinopia
RUN git checkout $version
RUN npm install --production

RUN npm install --production https://github.com/plitex/sinopia-ldap.git

# Clean

RUN rm -rf .git
RUN npm cache clean

ADD config.yaml /sinopia/config.yaml

CMD ["./bin/sinopia"]

EXPOSE 4873

VOLUME /sinopia/storage
