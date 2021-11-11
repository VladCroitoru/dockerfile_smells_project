FROM node:latest
WORKDIR /usr/app
COPY package.json .
RUN npm install\
&& npm install typescript -g
COPY . .
RUN tsc src/server.ts

# workaround to add appd profile in root file of applcation i.e. server.js
RUN chmod +x add-config.sh
RUN ./add-config.sh
WORKDIR /usr/app
EXPOSE 5000

CMD ["node", "src/server.js"]