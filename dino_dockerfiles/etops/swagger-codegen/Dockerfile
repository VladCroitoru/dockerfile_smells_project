FROM jimschubert/8-jdk-alpine-mvn:1.0

RUN apk add --no-cache gnupg curl tar xz nodejs bash

# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  ; do \
    gpg -q --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

ENV NPM_CONFIG_LOGLEVEL info

RUN mkdir -p /tools   
WORKDIR /tools
VOLUME  /src
VOLUME  /root/.m2/repository

ENV GEN_DIR /opt/swagger-codegen
WORKDIR ${GEN_DIR}
VOLUME  ${MAVEN_HOME}/.m2/repository

# Required from a licensing standpoint
COPY ./LICENSE ${GEN_DIR}

COPY ./google_checkstyle.xml ${GEN_DIR}

COPY gulpfile.js /tools/gulpfile.js
COPY package.json /tools/package.json

COPY ./modules/swagger-codegen-maven-plugin ${GEN_DIR}/modules/swagger-codegen-maven-plugin
COPY ./modules/swagger-codegen-cli ${GEN_DIR}/modules/swagger-codegen-cli
COPY ./modules/swagger-codegen ${GEN_DIR}/modules/swagger-codegen
COPY ./modules/swagger-generator ${GEN_DIR}/modules/swagger-generator
COPY ./pom.xml ${GEN_DIR}

# Pre-compile swagger-codegen-cli
RUN mvn -am -pl "modules/swagger-codegen-cli" package

# This exists at the end of the file to benefit from cached layers when modifying docker-entrypoint.sh.
COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["help"]
