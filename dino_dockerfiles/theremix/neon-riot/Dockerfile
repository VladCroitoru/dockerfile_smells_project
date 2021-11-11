FROM node:alpine
MAINTAINER Jon Borgonia "jon@gomagames.com"
EXPOSE 80

RUN mkdir /app
COPY components /app/components
COPY lib /app/lib
COPY pages /app/pages
COPY package.json /app/

WORKDIR /app

RUN npm install
RUN npm run build

CMD ["npm", "start", "--", "-p", "80"]
