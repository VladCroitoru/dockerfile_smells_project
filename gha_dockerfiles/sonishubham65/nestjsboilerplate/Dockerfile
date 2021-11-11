FROM node:12-buster
WORKDIR /app
COPY . /app
RUN npm install
ENV NODE_ENV=test 
RUN npm run db:migrate
RUN npm run db:seed
RUN npm run test
RUN npm run test:e2e
ENV NODE_ENV=dev
RUN npm run db:migrate
RUN npm run db:seed
EXPOSE 3000
CMD [ "npm", "start" ]