FROM node:13-buster as build

RUN apt-get update && \
    apt-get install -y \
        libglu1 \
        libxi6 \
        libgconf-2-4 \
    && ldconfig \
    && npm i gatsby-cli -g
WORKDIR /app
ADD . ./
RUN npm ci
RUN gatsby build

FROM gatsbyjs/gatsby
COPY --from=build /app/public /pub
