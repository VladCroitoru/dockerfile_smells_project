FROM google/nodejs

RUN mkdir /app
COPY ./app.js /app/
COPY ./package.json /app/
COPY ./app /app/app/
COPY ./config /app/config/

WORKDIR /app
RUN npm install

EXPOSE 18080
CMD npm start