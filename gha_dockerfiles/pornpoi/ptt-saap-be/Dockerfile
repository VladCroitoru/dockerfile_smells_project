FROM node:10 
ENV NODE_ENV=development NODE_PATH=/usr/src/app
VOLUME [ "/data" ]
RUN mkdir -p /data/saap/images/

#Set timezone
ARG TIMEZONE="Asia/Bangkok"
RUN ln -snf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && echo ${TIMEZONE} > /etc/timezone

WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
# RUN npm audit fix
# Bundle app source
COPY . .
COPY ormconfig.ts ./src/

RUN rm ormconfig.ts

CMD [ "npm", "start" ]
