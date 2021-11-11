FROM codesimple/elm:0.19
FROM node

# NOTE: you actually do need unsafe perm to install elm packages with npm
RUN npm install --unsafe-perm -g elm-test

# NOTE: we need to set HOME, because elm uses $HOME/.elm to save packages.
#       if this doesn't persist between runs, you get CORRUPT BINARY errors.
ENV HOME /mnt

WORKDIR /mnt
VOLUME /mnt
# NOTE: docker-compose mounts code in /mnt
COPY . /mnt

CMD ["yarn", "build-prod"]

FROM nginx
WORKDIR /mnt/dist
EXPOSE 8000 80