FROM node:14-alpine
WORKDIR /vindigo
ENV PRISMA_HIDE_UPDATE_MESSAGE=true

# Install dependencies
COPY package.json .
COPY packages/ packages/
RUN yarn install --production

# Build the source
COPY . .

# Trigger the default setup and generation
# of most distribution files.
RUN node vindigo init --defaults --skip-migrate
RUN rm ./data/config.toml

# Start the app platform
VOLUME ["/vindigo/data"]
ENTRYPOINT ["sh", "./bootstrap.sh"]
CMD ["node", "vindigo", "run"]