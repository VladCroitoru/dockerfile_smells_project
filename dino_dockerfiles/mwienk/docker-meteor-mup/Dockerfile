FROM node
MAINTAINER Mark Wienk <mark@wienkit.nl>

# exporting language settings for mongodb, which gets confused by missing locale variables or some such.
ENV LC_ALL C.UTF-8
ENV LANG C
ENV METEOR_ALLOW_SUPERUSER true
RUN curl https://install.meteor.com | /bin/sh
RUN node -v
RUN npm install -g mup
RUN npm install -g eslint eslint-plugin-class-property eslint-plugin-react
