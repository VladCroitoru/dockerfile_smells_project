FROM openjdk:8-jre-alpine
MAINTAINER "S M Y ALTAMASH <smy.altamash@gmail.com>"
RUN apk update \
    && apk add  unzip \
    && apk add curl \
    && adduser -u 1001 -h /home/sunbird/ -D sunbird \
    && apk --no-cache add chromium \
    && mkdir -p /home/sunbird/
RUN apk add font-noto-gujarati font-noto-kannada font-noto-avestan font-noto-osage font-noto-kayahli font-noto-oriya font-noto-telugu font-noto-tamil font-noto-bengali font-noto-malayalam font-noto-arabic font-noto-extra \
    && fc-cache -f
ADD ./cert-service-1.2.0-dist.zip /home/sunbird/
RUN unzip /home/sunbird/cert-service-1.2.0-dist.zip -d /home/sunbird/
RUN chown -R sunbird:sunbird /home/sunbird
USER sunbird
EXPOSE 9000
WORKDIR /home/sunbird/
CMD java -XX:+PrintFlagsFinal $JAVA_OPTIONS -cp '/home/sunbird/cert-service-1.2.0/lib/*' play.core.server.ProdServerStart  /home/sunbird/cert-service-1.2.0
