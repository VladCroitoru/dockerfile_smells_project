FROM node:boron-alpine

EXPOSE 3000

RUN mkdir -p /app/code
WORKDIR /app/code

# node-sass requires python
RUN apk add --no-cache  --update \
    python \
    python-dev \
    build-base

# Install node deps
ADD package.json package.json
RUN npm install

# Install Gulp tool
RUN npm install -g gulp-cli

# Add code
ADD src/ /app/code/src/
ADD frontend/ /app/code/frontend/
ADD gulpfile.js package.json app.js start.sh things.json logo.png /app/code/

# Build the app
RUN gulp default

# Start the app
CMD [ "/app/code/start.sh" ]
