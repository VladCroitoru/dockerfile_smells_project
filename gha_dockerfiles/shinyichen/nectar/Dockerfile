FROM node:14.16.1-buster-slim

ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
# Cypress dependencies: https://docs.cypress.io/guides/continuous-integration/introduction#Dependencies
RUN apt-get update && \
    apt-get install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb -y

WORKDIR /app

# Copy application files (excluding unnecessary things such as node_modules)
COPY *.js /app/
COPY *.ts /app/
COPY *.json /app/
COPY .env* /app/
COPY yarn.lock /app/
COPY cypress/ /app/cypress/
COPY src/ /app/src/
COPY server/ /app/server/

# Install all required dependencies (prod & dev)
RUN yarn install --pure-lockfile

# Next.js collects completely anonymous telemetry data about general usage.
# Learn more here: https://nextjs.org/telemetry
# Uncomment the following line in case you want to disable telemetry.
ENV NEXT_TELEMETRY_DISABLED=1

ENV API_HOST=http://devapi.adsabs.harvard.edu/v1
ENV COOKIE_SECRET=G7Kfbufs9QkrnLRFPPGnciaLY3JLH3r9BL6nAKNdRPEzLAA5wcpmT6gF8hMVjY9n

# Port where express will listen
ENV PORT=8000

# Build production
RUN yarn build

# The next/image component's default loader uses squoosh because it is quick to install 
# and suitable for a development environment. For a production environment using next 
# start, it is strongly recommended you install sharp by running yarn add sharp in your 
# project directory.
# Source: https://nextjs.org/docs/messages/sharp-missing-in-production
RUN yarn add sharp@0.29.0

EXPOSE $PORT

CMD [ "yarn", "start" ]
