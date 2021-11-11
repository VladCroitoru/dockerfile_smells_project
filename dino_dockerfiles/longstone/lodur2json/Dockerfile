FROM node:0.12

RUN apt-get install python

# replace this with your application's default port
EXPOSE 3000

# copy app to src
COPY . /src
WORKDIR /src

# Install app dependencies

RUN cd /src; npm install

CMD [ "npm", "start" ]
