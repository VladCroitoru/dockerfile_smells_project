FROM node
MAINTAINER wyvernnot <wyvernnot@gmail.com>
COPY . .
RUN npm install
ENV ab-docker_PORT=80
ENV ab-docker_ADMIN_PORT=3000
ENV ab-docker_MODE=proxy
EXPOSE 80
EXPOSE 3000
CMD ["node","server.js"]