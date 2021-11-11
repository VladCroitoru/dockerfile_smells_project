FROM openjdk:8-jre-alpine3.7

RUN apk update \
	&& apk add ttf-dejavu \
	&& wget -q http://www.umlet.com/umlet_14_2/umlet-standalone-14.2.zip \
	&& unzip -q umlet-standalone-14.2.zip

RUN mkdir -p "/Umlet/?/.config/UMLet" && chown 1000:1000 "/Umlet/?/.config/UMLet" && mkdir -p "/root/.config/UMLet"

WORKDIR "/Umlet"

CMD ["java", "-jar", "umlet.jar", "-action=convert"]
