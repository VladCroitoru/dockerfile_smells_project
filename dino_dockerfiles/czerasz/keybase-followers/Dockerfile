FROM node:8.5.0-alpine

# Add files which describe module dependencies
COPY ./package.json ./yarn.lock /usr/app/
# Install node modules
RUN cd /usr/app/ && yarn install --production=true && rm ./package.json ./yarn.lock
# Add main script
COPY ./src/* /usr/app/

ENTRYPOINT ["node", "/usr/app/keybase-get-followers.js"]
CMD ["--help"]
