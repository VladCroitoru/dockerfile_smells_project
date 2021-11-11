FROM node:14

LABEL version="1.0"
LABEL maintainer = ["jean.molino@zallpy.com"]

WORKDIR /app

COPY ["package.json", "yarn.lock", "./"]

RUN npm install 

COPY . .

EXPOSE 3000

CMD ["npm", "start"]