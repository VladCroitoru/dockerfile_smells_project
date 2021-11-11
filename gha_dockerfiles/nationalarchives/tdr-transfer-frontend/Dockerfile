FROM openjdk:15-alpine
#For alpine versions need to create a group before adding a user to the image
RUN addgroup --system frontendgroup && adduser --system frontenduser -G frontendgroup
WORKDIR play
COPY target/universal/tdr-transfer-frontend*.zip .
RUN apk update && apk upgrade p11-kit && apk add bash unzip && unzip -qq tdr-transfer-frontend-*.zip
RUN chown -R frontenduser /play

USER frontenduser
CMD  tdr-transfer-frontend-*/bin/tdr-transfer-frontend \
                        -Dplay.http.secret.key=$PLAY_SECRET_KEY \
                        -Dconfig.resource=application.$ENVIRONMENT.conf \
                        -Dplay.cache.redis.host=$REDIS_HOST \
                        -Dauth.secret=$AUTH_SECRET
