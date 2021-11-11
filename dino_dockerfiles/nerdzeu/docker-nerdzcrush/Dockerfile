# From the "orginal" (the one with working ffmpeg-full)
FROM nerdzeu/docker-nerdzcrush:0.0.1
MAINTAINER Paolo Galeone <nessuno@nerdz.eu>

COPY startup.sh /opt/new.sh

EXPOSE 9999
VOLUME /home/mediacrush

# Create a group with a well-known id to work correctly with volumes
# and add the correct user to the group
USER root
RUN groupadd -g 7777 nerdz && \
        gpasswd -a mediacrush -g nerdz

RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

USER mediacrush
ENTRYPOINT bash /opt/new.sh
