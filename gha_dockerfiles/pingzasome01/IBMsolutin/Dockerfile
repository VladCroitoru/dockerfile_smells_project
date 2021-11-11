FROM node:12.18.1-alpine
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json 
COPY src /app/src
RUN npm install
RUN npm install @vue/cli -g
EXPOSE 8080
CMD ["npm", "run", "serve"]