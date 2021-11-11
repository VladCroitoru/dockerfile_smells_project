FROM buildkite/puppeteer:latest
RUN apt-get update && apt-get install -y procps
ENV PUPPETEER_EXECUTABLE_PATH="/usr/bin/google-chrome-stable"
RUN mkdir /app
WORKDIR /app
COPY . .
RUN yarn install
