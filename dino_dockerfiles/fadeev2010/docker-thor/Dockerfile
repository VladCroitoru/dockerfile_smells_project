FROM node:9

RUN mkdir /app
WORKDIR /app

RUN git clone https://github.com/observing/thor.git .
RUN npm install -g .

CMD /bin/bash
