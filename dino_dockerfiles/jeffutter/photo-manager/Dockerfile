FROM node:12.16.2-stretch as ui
RUN mkdir -p /src
WORKDIR /src

RUN apt-get update && apt-get install -y brotli

ADD package.json /src
ADD yarn.lock /src

RUN yarn install

ADD webpack.config.js /src
ADD bsconfig.json /src/bsconfig.json
ADD graphql_schema.json /src/graphql_schema.json
ADD src/ /src/src
ADD __tests__/ /src/__tests__
ADD public/ /src/public

RUN mkdir -p apps/photo_management_api_web/priv/static/
RUN yarn run webpack:production

FROM elixir:1.6-alpine as build
RUN mkdir -p /src
WORKDIR /src

RUN apk add -U git make gcc musl-dev \
    && mix local.hex --force \
    && mix local.rebar --force

ADD mix.exs /src/
ADD mix.lock /src/
ADD apps/images_resource/mix.exs /src/apps/images_resource/
ADD apps/photo_management_api/mix.exs /src/apps/photo_management_api/
ADD apps/photo_management_api_web/mix.exs /src/apps/photo_management_api_web/

RUN mix deps.get

ADD config /src/config
ADD apps /src/apps
ADD rel /src/rel

COPY --from=ui /src/apps/photo_management_api_web/priv/static/ apps/photo_management_api_web/priv/static/

ENV MIX_ENV prod
RUN mix compile
RUN mix release --env=prod

FROM jeffutter/python-opencv-alpine
RUN apk add -U --upgrade apk-tools \
    && apk add -U --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main libde265 libcrypto1.1 \
    && apk add -U bash imagemagick ncurses-libs libcrypto1.0 bc \
    && rm -rf /var/cache/apk/*
ADD https://raw.githubusercontent.com/wavexx/facedetect/master/facedetect /usr/local/bin/
ADD bin/face_crop /usr/local/bin
RUN chmod 755 /usr/local/bin/facedetect \
    && chmod 755 /usr/local/bin/face_crop
COPY --from=build /src/_build/prod/rel/photo_management /photo_management
ENTRYPOINT ["/photo_management/bin/photo_management"]
