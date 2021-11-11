FROM node:14.15.4-buster

WORKDIR /app
COPY . /app/
RUN npm install
RUN npm run build

ENV ENV_EXAMPLE 'replaceme'

CMD ["npm", "start"]
