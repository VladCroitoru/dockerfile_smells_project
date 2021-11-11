FROM node:10-buster as build

WORKDIR /app/

# Copy project dependencies
COPY package.json /app/
COPY yarn.lock /app/

# Install project dependencies
RUN yarn install --frozen-lockfile --production=true

# Copy project files
COPY . /app/

# Build project
RUN yarn build


FROM nginx:1.17.7

LABEL maintainer="Penn Labs"

COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build /app/build/ /usr/share/nginx/html
