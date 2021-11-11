FROM node:7.8.0-alpine
RUN mkdir Galvanize_Staff
ADD package.json /Galvanize_Staff
WORKDIR /Galvanize_Staff
RUN npm install -qqq
ADD . .
EXPOSE 3000

CMD ["npm", "start"]
