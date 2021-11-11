FROM alpine:3.2
MAINTAINER admin@tropicloud.net

ADD wps /wps
RUN /wps/wps.sh build

ENV WP_ENV=development \
    WP_SSL=false \
    WP_REPO=https://github.com/roots/bedrock.git

EXPOSE 80 443
ENTRYPOINT ["wps"]
CMD ["start"]
