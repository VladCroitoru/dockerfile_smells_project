FROM node:14.16.0-alpine
WORKDIR ./FamiliaNETFront
COPY package.json .
RUN npm install
COPY . .
EXPOSE 4200 49153
CMD npm run start
