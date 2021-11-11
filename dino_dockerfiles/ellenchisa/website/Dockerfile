FROM node:alpine

WORKDIR /app
COPY ./package.json .
COPY ./package-lock.json .
RUN npm ci

COPY . .
RUN npm run build

CMD ["npm", "run", "serve", "--", "-p 8000", "--host=0.0.0.0"]