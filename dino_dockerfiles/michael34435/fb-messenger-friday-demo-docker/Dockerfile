FROM node
MAINTAINER michael34435

RUN apt-get update
RUN apt-get install git
RUN git clone https://github.com/michael34435/fb-messenger-friDay-demo.git
WORKDIR "fb-messenger-friDay-demo"
RUN npm i
EXPOSE 80
CMD ["node", "demo.js"]
