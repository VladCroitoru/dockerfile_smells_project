FROM ubuntu:17.04

ENV MM_USERNAME mmuser
ENV MM_PASSWORD mmuser_password
ENV MM_DBNAME mattermost

RUN apt-get update && \
    apt-get -y install curl netcat

RUN mkdir -p /mattermost/data
RUN curl https://releases.mattermost.com/3.6.2/mattermost-team-3.6.2-linux-amd64.tar.gz | tar -xvz

RUN rm /mattermost/config/config.json
COPY config.template.json /

COPY docker-entry.sh /
RUN chmod +x /docker-entry.sh
ENTRYPOINT ["/docker-entry.sh"]

EXPOSE 80
