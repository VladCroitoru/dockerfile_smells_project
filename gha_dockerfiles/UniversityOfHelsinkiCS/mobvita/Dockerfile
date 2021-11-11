FROM node:10

# Set timezone to Europe/Helsinki
RUN echo "Europe/Helsinki" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

ARG BASE_PATH
ENV BASE_PATH=$BASE_PATH

ARG COMMIT_HASH
ENV COMMIT_HASH=$COMMIT_HASH

ARG REVITA_URL
ENV REVITA_URL=$REVITA_URL

ARG ENVIRONMENT
ENV ENVIRONMENT=$ENVIRONMENT

# Setup
WORKDIR /usr/src/app
COPY . .

RUN npm ci

RUN npm run build

EXPOSE 8000

CMD ["npm", "run", "start:prod"]
