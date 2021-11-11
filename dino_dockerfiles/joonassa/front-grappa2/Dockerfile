FROM node:8.0.0

# Setup
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

RUN npm i

RUN npm run build
RUN npm install -g serve

EXPOSE 5000

CMD ["serve", "-s", "build"]
