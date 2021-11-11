FROM openjdk:8-jre-alpine
MAINTAINER Peter McConnell <me@petermcconnell.com>

RUN apk upgrade && \
	apk add --update \
	  wget \
	  ca-certificates

# burp (free)
RUN wget -O /burp.jar https://portswigger.net/burp/releases/download?productid=100&version=1.7.22&type=jar

ENTRYPOINT ["java", "-jar", "-Xmx1024m", "/burp.jar"]
