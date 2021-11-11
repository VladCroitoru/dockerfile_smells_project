# FROM node:latest
# WORKDIR /usr/src/app
# COPY package.json ./
# RUN npm install
# COPY . .
# EXPOSE 3000
# CMD ["node", "run", "dev"]
FROM node:latest
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
ENTRYPOINT ["node", "src/index.js"]
