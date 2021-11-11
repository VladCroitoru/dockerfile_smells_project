FROM node:8.1
WORKDIR /app

COPY package.json ./
RUN npm install

RUN rm package.json
RUN rm package-lock.json

CMD /bin/true
