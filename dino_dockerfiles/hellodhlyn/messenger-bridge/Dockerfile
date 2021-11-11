FROM node:carbon

# Non-root user `app`
RUN useradd --create-home -s /bin/bash app
WORKDIR /home/app

# Install dependencies and build
COPY package.json .
RUN yarn --production

COPY . .
RUN yarn build

# Change to user `app`
RUN chown -R app:app /home/app
USER app

CMD [ "yarn", "start" ]
