FROM node:8.6

# First install dependencies
COPY ./package.json ./app/
WORKDIR /app/
ENV NODE_ENV production

ENV MT_TITLE mailtrain
ENV MT_LANGUAGE en
ENV MT_LOG_LEVEL verbose

ENV MT_PORT 3000
ENV MT_HOST_INTERFACE 0.0.0.0
ENV MT_SECRET a cat
ENV MT_LOGGER dev
ENV MT_USE_PROXY false
ENV MT_MAX_POST 2MB

ENV MYSQL_HOST localhost
ENV MYSQL_USER mysql
ENV MYSQL_PASSWORD password
ENV MYSQL_DB database
ENV MYSQL_PORT 3306

ENV USE_REDIS true
ENV REDIS_HOST localhost
ENV REDIS_PORT 6379


RUN npm install --no-progress --production && npm install --no-progress passport-ldapjs passport-ldapauth

# Later, copy the app files. That improves development speed as buiding the Docker image will not have 
# to download and install all the NPM dependencies every time there's a change in the source code
COPY . /app
EXPOSE 3000
ENTRYPOINT ["bash", "/app/docker-entrypoint.sh"]
CMD ["node", "index.js"]
