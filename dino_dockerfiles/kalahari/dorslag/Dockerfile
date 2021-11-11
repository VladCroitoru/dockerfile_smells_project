FROM node:0.12
RUN useradd -d /opt/dorslag -m -r -U dorslag
USER dorslag
WORKDIR /opt/dorslag
COPY package.json server.js ./
RUN npm install
EXPOSE 8080
CMD ["/usr/local/bin/node", "server.js"]
