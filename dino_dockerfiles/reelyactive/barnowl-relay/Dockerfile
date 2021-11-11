FROM node

RUN apt-get update
RUN apt-get install build-essential python -y

WORKDIR /src
ADD . .

RUN npm install

EXPOSE 50000/udp
CMD ./barnowl-relay
