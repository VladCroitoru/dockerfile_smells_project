FROM 1science/sbt:0.13.8-oracle-jre-8

ENV VINDINIUM_REPO https://github.com/ornicar/vindinium.git
ENV VINDINIUM_VERSION 728c10684b2ee2e145991021f331f957b5f9c848
ENV GIT_VERSION 2.2.1-r0

WORKDIR /
RUN apk update
RUN apk upgrade
RUN apk add git=$GIT_VERSION
RUN apk add nodejs
RUN npm install -g bower grunt-cli

RUN git clone $VINDINIUM_REPO
WORKDIR /vindinium
RUN git checkout $VINDINIUM_VERSION
WORKDIR /vindinium/client
RUN ./build.sh
WORKDIR /vindinium
RUN pwd
COPY application.conf conf/application.conf
RUN sbt compile dist
RUN unzip target/universal/vindinium-1.1.zip

CMD ["vindinium-1.1/bin/vindinium"]