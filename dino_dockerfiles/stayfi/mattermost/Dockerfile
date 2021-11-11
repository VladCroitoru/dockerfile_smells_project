FROM debian:jessie
MAINTAINER Stayfi B. <stayfi@gmail.com>

ADD https://releases.mattermost.com/3.6.1/mattermost-team-3.6.1-linux-amd64.tar.gz .
RUN tar -zxvf ./mattermost-team-3.6.1-linux-amd64.tar.gz
RUN rm ./mattermost-team-3.6.1-linux-amd64.tar.gz
ADD config.json ./mattermost/config/config.json

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

WORKDIR /mattermost
VOLUME /mattermost

ENTRYPOINT ["/entrypoint.sh"]