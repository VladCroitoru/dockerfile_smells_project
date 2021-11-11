FROM node:VERSION

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y --no-install-recommends \
    rsync

EXPOSE 8080

ENV NODE_ENV production

CMD sh -c 'cd /usr/src/app && npm start'
