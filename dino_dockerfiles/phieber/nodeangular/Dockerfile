FROM node:latest

LABEL Description="This image speeds up Angular2 development inside a container" Vendor="Patrick Hieber" Version="0.1"

#RUN npm cache clean -f; npm install -g npm; npm install -g bower
RUN npm cache clean -f ; npm install -g bower

CMD [ "npm", "start" ]

EXPOSE 8080
