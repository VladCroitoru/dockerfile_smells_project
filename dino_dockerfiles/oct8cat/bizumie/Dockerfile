FROM node:8

ENV DB_URI mongodb://bizumie-mongo/bizumie
ENV URL http://localhost:3000

WORKDIR /opt/bizumie
COPY package.json package-lock.json ./
RUN npm install
COPY . .

VOLUME /opt/bizumie/public/uploads
EXPOSE 80

CMD npm start
