FROM node:14-alpine

# Set a working directory
WORKDIR /usr/src/app

# Copy application files
COPY ./build .

# Install Node.js dependencies
RUN yarn install --production --no-progress

# Run the container under "node" user by default
USER node

# Set NODE_ENV env variable to "production" for faster expressjs
ENV NODE_ENV production

CMD [ "node", "server.js" ]
