FROM postgres:14-alpine
ENV ALPINE_MIRROR "http://dl-cdn.alpinelinux.org/alpine"
RUN echo "${ALPINE_MIRROR}/edge/main" >> /etc/apk/repositories
RUN apk add --no-cache nodejs-current  --repository="http://dl-cdn.alpinelinux.org/alpine/edge/community"
ENV NODE_ENV=production
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN apk update
RUN apk add --update npm
RUN npm install
COPY . .
EXPOSE 3000
RUN chown postgres:postgres /run/postgresql/
RUN cd
RUN chmod 0700 /var/lib/postgresql/data
RUN su -c 'initdb -D /var/lib/postgresql/data' postgres
RUN echo "host all all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf
RUN echo "listen_addresses='*'" >> /var/lib/postgresql/data/postgresql.conf
# RUN su -c 'pg_ctl start -D /var/lib/postgresql/data' postgres
# RUN su -c 'psql -U postgres < db/schema.sql' postgres
# RUN su -c 'pg_ctl stop -D /var/lib/postgresql/data' postgres
# CMD ["npm", "start"]
CMD ["/bin/sh"]