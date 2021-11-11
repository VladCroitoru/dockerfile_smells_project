FROM node:onbuild
MAINTAINER ninthwalker
# Forked for unraid usage
# Original Creator: Benjamin Jorand <benjamin.jorand@gmail.com>

EXPOSE 7879

COPY . /slack-invite
WORKDIR /slack-invite
RUN npm install
CMD ./bin/www
