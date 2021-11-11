FROM node:16 AS build-env
COPY package*.json /app/
WORKDIR /app

RUN npm ci --only=production --unsafe-perm

FROM gcr.io/distroless/nodejs:16
COPY --from=build-env /app /app
COPY . /app
WORKDIR /app
CMD ["bin/www"]
