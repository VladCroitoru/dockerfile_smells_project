FROM node:14
WORKDIR /src
ADD package* /src/
RUN npm i
ADD Makefile .
CMD npm run build
