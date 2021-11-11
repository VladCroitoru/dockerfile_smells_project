FROM node:latest

WORKDIR /app

COPY . /app

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

ENV SECURITY=public

EXPOSE 4000

CMD [ "npm", "run", "serve" ]
