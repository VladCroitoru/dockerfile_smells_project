FROM huggla/tomcat-alpine

USER root

ENV REV_param_CATALINA_OPTS="-Xms128m -Xmx756M -XX:SoftRefLRUPolicyMSPerMB=36000" \
    JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

RUN apk add --no-cache --virtual .build-deps openjdk$JAVA_MAJOR \
 && downloadDir="$(mktemp -d)" \
 && wget http://data.boundlessgeo.com/suite/jai/jai-1_1_3-lib-linux-amd64-jdk.bin -O "$downloadDir/jai-1_1_3-lib-linux-amd64-jdk.bin" \
 && cd "$JAVA_HOME" \
 && echo "yes" | sh "$downloadDir/jai-1_1_3-lib-linux-amd64-jdk.bin" \
 && wget http://data.opengeo.org/suite/jai/jai_imageio-1_1-lib-linux-amd64-jdk.bin -O "$downloadDir/jai_imageio-1_1-lib-linux-amd64-jdk.bin" \
 && echo "yes" | sh "$downloadDir/jai_imageio-1_1-lib-linux-amd64-jdk.bin" \
 && rm -rf "$downloadDir" \
 && apk del .build-deps

ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk/jre"

USER sudoer
