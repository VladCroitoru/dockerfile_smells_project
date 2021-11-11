FROM node:14 AS builder

WORKDIR /app

COPY ./package.json ./

RUN npm install

COPY ./ ./

# RUN npm run build

###

# FROM node:14-alpine

# WORKDIR /app

# COPY --from=builder /app ./

EXPOSE 8000

# CMD ["npm", "run", "start:prod"]

CMD ["npm", "run", "start:dev"]
