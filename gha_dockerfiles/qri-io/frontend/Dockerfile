FROM node:14.8-alpine as build

ARG api_base_url
ARG ws_base_url
ARG app_port

ENV REACT_APP_API_BASE_URL=$api_base_url
ENV REACT_APP_WS_BASE_URL=$ws_base_url
ENV PORT=$app_port

# create app directory
WORKDIR /app

RUN echo "fs.inotify.max_user_watches=524288" >> /etc/sysctl.conf

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# copy local source to /app working directory
# this is affected by .dockerignore
COPY . ./
# run installation
RUN yarn install
RUN yarn build

# distribution image, must be the same architecture & OS as build
# or else node-sass gets angry
FROM node:14.8-alpine
COPY --from=build /app /
EXPOSE 8080
CMD ["yarn", "serve"]
