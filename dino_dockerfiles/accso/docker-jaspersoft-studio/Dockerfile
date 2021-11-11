# See https://github.com/accso/docker-jaspersoft-studio
FROM debian:buster-slim
MAINTAINER marcus.rickert@accso.de
RUN adduser --disabled-login --uid 1000 jaspersoft
RUN chown jaspersoft.jaspersoft /home/jaspersoft
ARG VERSION=6.5.1
ENV FILENAME=TIB_js-studiocomm_${VERSION}.final_linux_amd64.deb
ENV URL=https://netcologne.dl.sourceforge.net/project/jasperstudio/JaspersoftStudio-${VERSION}/${FILENAME}
#ENV URL=https://kent.dl.sourceforge.net/project/jaspersoft/JaspersoftStudio-${VERSION}/${FILENAME}

#COPY ./assets/TIB_js-studiocomm_6.5.1.final_linux_amd64.deb /opt

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
	   curl \
	   libwebkitgtk-1.0-0 \
	   libxtst6 \
    && mkdir -p /opt \
    && echo "Downloading ${URL}" \
    && curl -s -o /opt/${FILENAME} -L ${URL} \
    && dpkg -i /opt/${FILENAME} \
    && apt-get install -f \
    && rm /opt/${FILENAME}
COPY assets/docker-entrypoint.sh /docker-entrypoint.sh
ENV DOCKER_USER=jaspersoft
RUN mkdir -p /home/${DOCKER_USER}/home_on_host
ENTRYPOINT [ "/docker-entrypoint.sh" ]
