FROM docker-nginx-amplify

# fork from https://github.com/spujadas/elk-docker.git
MAINTAINER William Chong <williamchong@like.co>
ENV REFRESHED_AT 2021-03-23


###############################################################################
#                                INSTALLATION
###############################################################################

RUN rm /etc/apt/sources.list.d/nginx-amplify.list

### install Filebeat

ENV FILEBEAT_VERSION 7.9.3


RUN apt-get update -qq \
 && apt-get install -qqy curl \
 && apt-get clean

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-amd64.deb \
 && dpkg -i filebeat-${FILEBEAT_VERSION}-amd64.deb \
 && rm filebeat-${FILEBEAT_VERSION}-amd64.deb

###############################################################################
#                                    DATA
###############################################################################

### add dummy HTML file

COPY html /usr/share/nginx/html


###############################################################################
#                                    START
###############################################################################

ADD ./start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh
ENTRYPOINT ["/usr/local/bin/start.sh"]
