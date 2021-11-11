FROM node:7
RUN mkdir /bargain-hound
ADD . /bargain-hound
WORKDIR /bargain-hound
RUN npm i
EXPOSE 8000
CMD ["npm", "start"]
