FROM node:0.12
MAINTAINER "Patrick DeVivo" <patrick.devivo@gmail.com>

COPY . /home/val-api
EXPOSE 80
EXPOSE 43554

RUN cd /home/val-api; npm install
RUN npm install pm2 -g
RUN chmod 755 /home/val-api/start
CMD ["/home/val-api/start"]