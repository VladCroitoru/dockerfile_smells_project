FROM node:12.10.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN npm install -g @angular/cli
RUN npm install
RUN npm install node-sass
EXPOSE 4200
CMD ng serve --host 0.0.0.0