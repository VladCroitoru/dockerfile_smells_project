FROM node:14.15.1-alpine
EXPOSE 3000
ENV HOST 0.0.0.0

WORKDIR /app
COPY ./package.json ./
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]