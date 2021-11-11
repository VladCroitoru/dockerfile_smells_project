FROM node:6.9
WORKDIR /nodejs_apps/profiler_cabinet
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 8888
CMD [ "npm", "start" ]