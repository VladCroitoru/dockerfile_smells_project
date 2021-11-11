FROM node:12.16.1-alpine3.11 AS builder

LABEL maintainer="HackMerced"
LABEL maintainer.email="general@hackmerced.com"
LABEL version="2.0.0"

WORKDIR /app
COPY . .

RUN npm install react-scripts -g --silent
RUN yarn install --silent --ignore-scripts --check-files
RUN yarn build --silent

# Serve built react app
FROM node:12.16.1-alpine3.11

RUN yarn global add serve

WORKDIR /app
COPY --from=builder /app/build .

CMD ["serve", "-p", "3000", "-s", "."]doc
