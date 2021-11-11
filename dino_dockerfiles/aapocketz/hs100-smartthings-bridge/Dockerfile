#1. put the files in a folder called hs-100
#2. sudo docker build -t hs-100:latest hs-100/.
#3. run the container
#4. sudo docker run -d -p 8083:8083 -v /etc/localtime:/etc/localtime:ro --restart=always --name hs-100 hs-100:latest
# or
#4. docker run -t -i -p 8083:8083 --entrypoint=/bin/bash --name hs-100  hs-100:latest
#5. docker exec -it hs-100 bash
#6. curl -H "x-hs100-command:on" -H "x-hs100-ip:<plugip>" -D - <gatewayip>:8083



FROM phusion/baseimage:latest

CMD ["/sbin/my_init"]

RUN apt-get -y update && apt-get install -y nodejs npm nano

RUN npm install -g n
RUN n stable

COPY . /hs-100
RUN cd /hs-100; npm install


EXPOSE 8083

CMD ["node", "/hs-100/hs100.js"]
