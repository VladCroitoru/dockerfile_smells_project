# Run with
#   docker run -it --rm -p 4200:4200 locdb-frend-app
# then navigate to 
#   localhost:4200
#
FROM node:7-slim
#FROM node:7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install && npm cache clean
COPY . /usr/src/app

# This is necessary to make the output accessible from outside the container
RUN sed -i -e "s/ng serve/ng serve --host 0.0.0.0/" package.json

CMD [ "npm", "start" ]