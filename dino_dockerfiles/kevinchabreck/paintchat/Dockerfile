FROM 1science/sbt:0.13.8-oracle-jre-8
MAINTAINER Kevin Chabreck

# PaintChat image based on Oracle Java 8 and SBT 0.13.9

# get required sbt version
COPY project/build.properties project/build.properties
RUN sbt update

# build compiler-interface for scala 12.4
RUN echo 'scalaVersion := "2.12.4"' > build.sbt && \
    mkdir -p src/main/scala && \
    touch src/main/scala/tmp.scala && \
    sbt compile && \
    rm -rf src build.sbt

# download dependencies
COPY build.sbt build.sbt
RUN sbt compile

# build project once without config file
COPY src/main/resources/www/ src/main/resources/www/
COPY src/main/scala/ src/main/scala/
RUN sbt compile

# rebuild with config
COPY src/main/resources/application.conf src/main/resources/application.conf
RUN sbt compile

# run PaintChat on entry
CMD ["sbt", "run"]
