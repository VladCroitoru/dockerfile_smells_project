FROM node

RUN mkdir -p /opt/strichliste

WORKDIR /opt/strichliste

COPY package.json /opt/strichliste/

RUN npm install

COPY . /opt/strichliste

EXPOSE 8080

CMD [ "npm", "start" ]
