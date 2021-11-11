FROM node:0.10

RUN groupadd -r app \
&&  useradd -r -g app app

COPY . /source
WORKDIR /source

RUN curl -sL https://install.meteor.com | sed s/--progress-bar/-sL/g | /bin/sh \
 && meteor npm install \
 && meteor build --directory /app \
 && cd /app/bundle/programs/server \
 && npm install \
 && chown -R app:app /app

USER app

WORKDIR /app/bundle

# needs a mongoinstance - defaults to container linking with alias 'db'
ENV MONGO_URL=mongodb://db:27017/meteor \
    HOME=/tmp \
    PORT=3000 \
    ROOT_URL=http://localhost:3000

EXPOSE 3000

CMD ["node", "main.js"]
