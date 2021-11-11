FROM openjdk:8-jre-alpine

MAINTAINER ValentinDeville <contact@valentin-deville.eu>

# Create directory and start JD2 for the initial update and creation of config files.
RUN mkdir -p /opt/JDownloader/ && \
    wget -O /opt/JDownloader/JDownloader.jar http://installer.jdownloader.org/JDownloader.jar && \
    java -Djava.awt.headless=true -jar /opt/JDownloader/JDownloader.jar && \
    apk add --no-cache --quiet tini

COPY startJD2.sh /opt/JDownloader/
RUN chmod +x /opt/JDownloader/startJD2.sh

# Run this when the container is started
ENTRYPOINT ["/sbin/tini", "-g", "--", "/opt/JDownloader/startJD2.sh"]
CMD ["java", "-Djava.awt.headless=true", "-jar", "/opt/JDownloader/JDownloader.jar", "-norestart"]
