# Freeze at Node version 6.?.?
FROM node:6

# Create app environment.
ENV NODE_ENV production
EXPOSE 4444
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install Dockerize
ENV DOCKERIZE_VERSION 0.2.0
ADD https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz /tmp/dockerize.tar.gz
RUN tar -C /usr/local/bin -xzvf /tmp/dockerize.tar.gz \
    && rm -f /tmp/dockerize.tar.gz

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install --production

# Bundle app source
COPY . /usr/src/app

# Build static assets
RUN npm run build

CMD ["dockerize", "-template", "assets/config.json.tmpl:config.json", "npm", "start"]
