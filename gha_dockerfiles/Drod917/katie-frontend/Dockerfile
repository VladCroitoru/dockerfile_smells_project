FROM node:14
WORKDIR /app

EXPOSE 9000 8000 9929 9230
ENV HOST=0.0.0.0

# COPY the package.json file, update any deps and install them
COPY package.json .
COPY gatsby-config.js .
COPY gatsby-node.js .

RUN apt-get install -y python
RUN npm update --legacy-peer-deps
RUN npm install

# copy the whole source folder(the dir is relative to the Dockerfile)
COPY . .
RUN npm run build

CMD [ "npm", "run", "serve"]