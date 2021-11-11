FROM alpine as build-env
RUN apk add --no-cache build-base make sdl2-dev sdl2_image-dev gtk+3.0-dev

WORKDIR /app

CMD make