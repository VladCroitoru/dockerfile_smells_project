FROM node:12
WORKDIR /usr/src/service
COPY . .
RUN npm install
RUN npm run build
EXPOSE 8080
CMD ["npm", "run", "start"]
