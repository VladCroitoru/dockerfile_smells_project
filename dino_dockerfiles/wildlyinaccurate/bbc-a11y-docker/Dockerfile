FROM node
MAINTAINER joseph@wildlyinaccurate.com

ENV DISPLAY=:99.0

RUN apt-get update && \
    apt-get -f install && \
    apt-get -y install wget gnupg2 apt-utils libgconf-2-4 xvfb libgtk-3-0 libxss1 libnss3 libasound2 && \
    apt-get clean

WORKDIR /ws

RUN npm install bbc-a11y

COPY start.sh /ws/start.sh

ENTRYPOINT ["/ws/start.sh"]
