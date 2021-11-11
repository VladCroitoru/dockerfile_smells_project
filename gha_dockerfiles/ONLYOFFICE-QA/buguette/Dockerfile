FROM node:16.12.0-alpine AS build

RUN apk update && \
    apk upgrade && \
    apk add --no-cache git
ENV NODE_OPTIONS=--max-old-space-size=1024
WORKDIR /buguette
COPY . .
RUN npm install
RUN npm run build

FROM nginx:1.21.3-alpine AS serve
COPY --from=build /buguette/dist/ /buguette/dist/
