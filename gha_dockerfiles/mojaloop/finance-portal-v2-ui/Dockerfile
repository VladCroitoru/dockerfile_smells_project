FROM node:10.13-alpine
# First part, build the app
WORKDIR /app
COPY package.json /app/
COPY yarn.lock /app/
RUN yarn install

COPY ./ /app/

# Adds the package version and commit hash
ARG REACT_APP_VERSION
ENV REACT_APP_VERSION=$REACT_APP_VERSION

ARG REACT_APP_COMMIT
ENV REACT_APP_COMMIT=$REACT_APP_COMMIT

RUN yarn run build

EXPOSE 8080

ENTRYPOINT [ "yarn", "serve:prod" ]