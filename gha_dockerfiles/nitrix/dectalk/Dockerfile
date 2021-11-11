FROM suchja/wine

USER root
RUN apt-get update && apt-get install -y golang Xvfb

COPY . /opt/say
RUN mkdir /opt/say/wavs && chmod 777 /opt/say/wavs

# Bypassing the xclient user
RUN chown root:root /home/xclient

WORKDIR /opt/say

RUN go build

CMD /opt/say/say