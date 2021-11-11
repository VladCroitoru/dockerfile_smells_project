FROM mhart/alpine-node

WORKDIR /var/app
COPY ./app/package.json /var/app/package.json
RUN npm install --production
COPY ./app /var/app
COPY ./db/leveldb/geoAddTC /db/leveldb/geoAddTC
EXPOSE 3000

CMD ["npm", "start"]