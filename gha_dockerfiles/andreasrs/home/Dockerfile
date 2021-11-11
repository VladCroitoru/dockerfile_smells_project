FROM node:16-alpine

RUN mkdir -p /src/app
WORKDIR /src/app
COPY package.json package-lock.json /src/app/
RUN npm install

COPY . /src/app
ENV NODE_ENV production
RUN npm run build

CMD ["npm", "start"]
EXPOSE 8080
