FROM node

RUN git clone https://github.com/rivayama/docbot.git
RUN cd docbot && npm install
RUN npm install -g forever
RUN apt-get update
RUN apt-get install -y mongodb

#ENTRYPOINT ["/usr/local/bin/forever", "start", "/docbot/docbot.js"]
ENTRYPOINT /usr/local/bin/forever start /docbot/docbot.js && /bin/bash
#ENTRYPOINT /usr/local/bin/forever start /docbot/docbot.js

EXPOSE 80
