FROM node

ENV NODE_ENV=docker

RUN apt-get install git
RUN git clone https://github.com/floriansimon1/holidays.git

WORKDIR holidays

RUN npm i --production

EXPOSE 80

ENTRYPOINT ["npm", "start"]
