FROM thothbot/alpine-sbt
MAINTAINER Alex Usachev <thothbot@gmail.com>

RUN echo $'name := """java""" \n\
version := "1.0-SNAPSHOT" \n\
scalaVersion := "2.11.8" \n\
libraryDependencies ++= { \n\
    val jacksonVersion="2.7.8" \n\
    Seq( \n\
      "io.baratine" % "baratine" % "1.0.1", \n\
      "org.postgresql" % "postgresql" % "9.4.1212", \n\
      "redis.clients" % "jedis" % "2.9.0", \n\
      "biz.source_code" % "base64coder" % "2010-12-19", \n\
      "org.apache.commons" % "commons-lang3" % "3.5", \n\
      "commons-io" % "commons-io" % "2.5", \n\
      "com.google.guava" % "guava" % "19.0", \n\
      "com.fasterxml.jackson.core"     % "jackson-core" % jacksonVersion, \n\
      "com.fasterxml.jackson.core"     % "jackson-databind" % jacksonVersion, \n\
      "com.fasterxml.jackson.core"     % "jackson-annotations" % jacksonVersion, \n\
      "com.fasterxml.jackson.datatype" % "jackson-datatype-jdk8" % jacksonVersion, \n\
      "com.fasterxml.jackson.datatype" % "jackson-datatype-jsr310" % jacksonVersion \n\
    ) \n\
}' > /app/build.sbt && \

mkdir /app/project && \

echo $'addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "0.14.4")' > /app/project/plugins.sbt && \
echo $'sbt.version=0.13.15' > /app/project/build.properties && \

cd /app && sbt package && \

rm -fr /app/*
