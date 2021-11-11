# Profit Trailer Crypto Trading Bot Dockerfile
#
# build with --build-arg PT_VERSION=2.1.12 to define the version number to build
#

# FROM openjdk:8-jre-alpine
FROM openjdk:8-jdk-alpine

ARG PT_VERSION=${PT_VERSION:-2.3.12}

ENV PT_FILENAME=ProfitTrailer-${PT_VERSION}.zip

ENV JAVA_HOME=/usr/lib/jvm/default-jvm
ENV PATH /usr/local/bin:$PATH
ENV FC_LANG en-US
ENV LC_CTYPE en_US.UTF-8

# install tools
RUN apk add --update wget bash java-cacerts \
  ; ln -sf "${JAVA_HOME}/bin/"* "/usr/bin/"

# fix broken cacerts
RUN rm -f /usr/lib/jvm/default-jvm/jre/lib/security/cacerts \
  ; ln -s /etc/ssl/certs/java/cacerts /usr/lib/jvm/default-jvm/jre/lib/security/cacerts

RUN mkdir -p /profit-trailer 

WORKDIR /profit-trailer 

RUN wget https://github.com/taniman/profit-trailer/releases/download/${PT_VERSION}/${PT_FILENAME}

# unzip the app
RUN unzip ${PT_FILENAME} -j \
  ; rm ${PT_FILENAME} \
#  ; rm application.properties \
#  ; mkdir config \
#  ; ls -la config/ \
#  ; ln -s ./config/application.properties . \
  ; chmod +x ProfitTrailer.jar

# add the application source to the image
COPY start /profit-trailer
RUN chmod +x /profit-trailer/start

# tidy up
RUN rm -rf /tmp/* /var/cache/apk/*

# expose our default runtime port
EXPOSE 8081

# run it
ENTRYPOINT ["./start"]