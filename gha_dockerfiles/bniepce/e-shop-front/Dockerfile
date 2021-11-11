FROM node

RUN mkdir -p /Users/WebstromProjects/e-comm/front

WORKDIR /Users/WebstromProjects/e-comm/front

COPY package.json /Users/WebstromProjects/e-comm/front

RUN npm install

COPY . /Users/WebstromProjects/e-comm/front

EXPOSE 8080

CMD ["npm", "start"]