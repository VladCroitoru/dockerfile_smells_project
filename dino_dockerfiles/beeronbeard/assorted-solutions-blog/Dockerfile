FROM node:12-alpine as generator

WORKDIR /usr/generator

COPY . .

RUN npm ci && \
    npm run build

###################################
# Host image
###################################
FROM nginx:alpine

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/BeerOnBeard/assorted-solutions-blog.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1"

COPY --from=generator /usr/generator/public /usr/share/nginx/html
