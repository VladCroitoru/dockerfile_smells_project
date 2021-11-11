FROM madkom/node-npm:latest

RUN npm install hackmyresume -g
RUN npm install http-server -g

COPY ./start.sh /
COPY ./rebuild.sh /
EXPOSE 8080
CMD bash -C '/start.sh'
