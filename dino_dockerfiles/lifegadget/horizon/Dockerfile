# REQUIREMENTS
#
# If DB_HOST and DB_PORT environment variables are pushed into the container at runtime
# then they will override the defaults of http://localhost:29015
#
# Your Horizon app should be mounted to "/usr/app"
# and if you're serving static content mount to "/static"
FROM mhart/alpine-node-auto:6.2.2

ENV DB_HOST localhost
ENV DB_PORT 29015

ENV HZ_DEV ""
ENV SERVE_PORT 8181
ENV SECURE yes
ENV PERMISSIONS yes
ENV AUTO_CREATE_COLLECTION ""
ENV AUTO_CREATE_INDEX ""
ENV HZ_SERVE_STATIC /static

# Authorization is not set but these values can be passed in
# and will be picked up by the Horizon Server, the ENV variables
# are (each has an 'id' and 'secret' key):
# ENV HZ_AUTH_FACEBOOK
# ENV HZ_AUTH_GOOGLE
# ENV HZ_AUTH_TWITTER
# ENV HZ_AUTH_GITHUB
# ENV HZ_AUTH_TWITCH
# Across all Auth services you can set:
ENV HZ_ALLOW_ANONYMOUS false
ENV HZ_ALLOW_UNAUTHENTICATED false
ENV HZ_AUTH_REDIRECT /static/auth
ENV HZ_ACCESS_CONTROL_ALLOW_ORIGIN *
# note: because above are set they will override TOML config file
# but operator can override these settings with use of explicitly
# set ENV variables

RUN mkdir -p /certs /static /static/auth \
 && apk update \
 && apk add git \
 && npm install -g horizon

EXPOSE $SERVE_PORT
WORKDIR /horizon
VOLUME ["/horizon", "/certs", "/static"]
CMD ["hz", "serve", $HZ_DEV, $AUTO_CREATE_COLLECTION, $AUTO_CREATE_INDEX, "--connect $DB_HOST:$DB_PORT"]
