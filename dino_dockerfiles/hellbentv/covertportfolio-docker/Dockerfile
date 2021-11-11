FROM node:7.10-slim

RUN apt-get update\
    && apt-get install -y git-core

RUN npm install -g bower\
    && npm install -g nodemon\
    && npm install -g typescript

RUN git clone https://github.com/hellbentv/node-yahoo-finance\
    && cd node-yahoo-finance\
    && npm install

RUN npm install -g bower nodemon typescript

RUN git clone https://github.com/hellbentv/covertportfolio\
    && cd covertportfolio\
    && npm install\
    && cd client\ 
    && npm install

RUN cd covertportfolio\
    && bower --allow-root install bootstrap

CMD node /covertportfolio/server
