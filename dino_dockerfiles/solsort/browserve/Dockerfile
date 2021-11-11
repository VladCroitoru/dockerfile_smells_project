FROM node:latest

RUN apt-get update && apt-get install -y xvfb libgtk2.0-0 libnotify4 libgconf2-4 libxss1 libnss3 dbus-x11
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN npm install
ENTRYPOINT ["npm", "start"]
EXPOSE 8888
