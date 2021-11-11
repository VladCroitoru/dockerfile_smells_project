#
# Builder image for the TS pipeline
#
FROM node:14-buster AS tsbuilder
COPY package.json /var/www/aplus/package.json
COPY typescript /var/www/aplus/typescript/
WORKDIR /var/www/aplus/
RUN npm install
RUN npm run build


#
# Builder image for the Scala app
# based on https://github.com/hseeberger/scala-sbt
#
FROM adoptopenjdk:11-jdk-hotspot AS scalabuilder

# We need nodejs to run in a reasonable amount of time sbt-web
# see step `Optimizing JavaScript with RequireJS`
RUN apt-get update && apt-get install -y --no-install-recommends nodejs

# Env variables
ENV SBT_VERSION 1.5.1

# Install sbt
RUN \
  curl -L -o sbt-$SBT_VERSION.deb https://repo.scala-sbt.org/scalasbt/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get install -y --no-install-recommends sbt && \
  sbt sbtVersion -Dsbt.rootdir=true

ENV PLAY_APP_NAME aplus
ENV PLAY_APP_DIR /var/www/$PLAY_APP_NAME
RUN mkdir -p $PLAY_APP_DIR
COPY .git $PLAY_APP_DIR/.git/
COPY build.sbt $PLAY_APP_DIR/
COPY app $PLAY_APP_DIR/app/
COPY macros $PLAY_APP_DIR/macros/
COPY conf $PLAY_APP_DIR/conf/
COPY public $PLAY_APP_DIR/public/
COPY --from=tsbuilder /var/www/aplus/public/generated-js $PLAY_APP_DIR/public/generated-js/
COPY project/*.properties project/*.sbt project/*.scala $PLAY_APP_DIR/project/

WORKDIR $PLAY_APP_DIR
ENV HOME $PLAY_APP_DIR
RUN sbt clean stage


#
#
# Final Image
#
#
FROM adoptopenjdk:11-jre-hotspot

ENV PLAY_APP_NAME aplus
ENV PLAY_APP_DIR /var/www/$PLAY_APP_NAME
ENV HOME $PLAY_APP_DIR
WORKDIR $PLAY_APP_DIR

COPY --from=scalabuilder $PLAY_APP_DIR/target/universal/stage $PLAY_APP_DIR
COPY data $PLAY_APP_DIR/data/
RUN chmod 554 $PLAY_APP_DIR/bin/$PLAY_APP_NAME
RUN chmod 774 $PLAY_APP_DIR

EXPOSE 9000
CMD ["sh", "-c", "$PLAY_APP_DIR/bin/$PLAY_APP_NAME $OPTIONS"]
