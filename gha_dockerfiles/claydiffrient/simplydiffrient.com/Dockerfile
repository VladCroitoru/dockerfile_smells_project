FROM node:17 as build
ENV APP_HOME /usr/src/app/
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
COPY package.json           ${APP_HOME}
COPY package-lock.json      ${APP_HOME}
RUN npm install
COPY . ${APP_HOME}
RUN npm run build

FROM alpine:latest
ARG CERT_DIRECTORY
EXPOSE 8080
COPY --from=build /usr/src/app/public /app/public
COPY CHECKS /app/CHECKS
RUN apk add --no-cache nginx
ADD nginx.conf /
ENTRYPOINT ["nginx", "-c",  "/nginx.conf"]
