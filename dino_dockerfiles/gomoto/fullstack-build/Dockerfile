FROM gomoto/node-docker-compose:0.0.2

VOLUME ["/src", "/build"]

# LiveReload port
EXPOSE 35729

WORKDIR /fullstack

RUN npm install --global gulp

COPY package.json ./
RUN npm install

COPY build ./
RUN chmod +x ./build

COPY watch ./
RUN chmod +x ./watch

COPY clean ./
RUN chmod +x ./clean

COPY config.js ./
COPY docker-compose.js ./
COPY docker-service.js ./
COPY gulpfile.js ./

CMD ["./build"]
