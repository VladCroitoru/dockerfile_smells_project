FROM node:15-slim

RUN apt-get update \
    && mkdir -p /usr/share/man/man1 \
    && mkdir -p /usr/share/man/man7 \
    && apt-get install -y --no-install-recommends postgresql-client libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

WORKDIR /app

COPY ["package.json", "yarn.lock*", "./"]

RUN yarn

COPY . .

EXPOSE 3000

CMD [ "yarn", "start" ]