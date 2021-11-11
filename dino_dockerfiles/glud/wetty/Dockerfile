FROM node:0.10.38
LABEL maintainer "Sebastian Tabares <sytabaresa@gmail.com>" 

ADD . /app
WORKDIR /app
RUN npm install
RUN apt-get update
RUN apt-get install -y vim nano asciinema mosquitto-clients jq net-tools
RUN useradd -d /home/glud -m -s /bin/bash glud
RUN echo 'glud:nomelase' | chpasswd

EXPOSE 3000

ENTRYPOINT ["node"]
CMD ["app.js", "-p", "3000"]
