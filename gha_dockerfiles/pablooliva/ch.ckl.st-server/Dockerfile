FROM node:10-alpine
WORKDIR /app
COPY . /app
RUN npm ci
EXPOSE 80
CMD ["npm", "run", "prod"]
