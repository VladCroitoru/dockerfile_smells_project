FROM node:16-alpine as build
WORKDIR /app
RUN apk update && apk add yarn git curl build-base
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN rustup default stable && rustup toolchain install stable
COPY . .
ARG REACT_APP_GIT_TAG unknown
RUN yarn && yarn build

FROM nginx:latest as run
COPY artifacts/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/build /usr/share/nginx/html
