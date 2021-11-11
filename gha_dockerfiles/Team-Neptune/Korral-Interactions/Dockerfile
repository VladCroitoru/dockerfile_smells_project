FROM node:14
COPY . /korral-interactions
WORKDIR /korral-interactions
RUN mkdir storage
RUN npm i
RUN npm run build
CMD npm start
EXPOSE 3000