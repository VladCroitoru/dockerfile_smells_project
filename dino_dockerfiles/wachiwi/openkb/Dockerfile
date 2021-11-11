FROM node:lts-alpine

EXPOSE 4444

WORKDIR /var/openKB
VOLUME /var/openKB/data

COPY locales/ /var/openKB/locales/
COPY public/ /var/openKB/public/
COPY routes/ /var/openKB/routes/
COPY views/ /var/openKB/views/
COPY config/ /var/openKB/config/
COPY app.js /var/openKB/
COPY package.json /var/openKB/

RUN npm install

ENTRYPOINT ["npm", "start"]
