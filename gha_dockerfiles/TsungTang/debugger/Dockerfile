FROM node:12.20 as base


# set working directory
WORKDIR /

COPY package*.json /frontend/package.json
RUN npm install

FROM base as frontend
WORKDIR /frontend
COPY . /frontend/

EXPOSE 3000

CMD ["npm", "run", "dev"]
