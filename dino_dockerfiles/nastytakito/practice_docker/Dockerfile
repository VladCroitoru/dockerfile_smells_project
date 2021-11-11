FROM node:7
RUN mkdir /practice_docker
ADD . /practice_docker
WORKDIR /practice_docker
RUN npm install
EXPOSE 80
CMD [ "npm", "start" ]
