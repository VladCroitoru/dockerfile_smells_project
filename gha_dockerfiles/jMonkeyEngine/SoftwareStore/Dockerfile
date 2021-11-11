FROM azul/zulu-openjdk:8

RUN apt update -y && apt upgrade -y && apt dist-upgrade -y

RUN apt install -y curl unzip && apt clean


RUN groupadd --gid 1000 nonroot 
RUN useradd --uid 1000 -r --gid 1000 nonroot 

COPY www /app_build/www
COPY build-docker.sh /app_build
COPY build.sh /app_build
COPY src /app_build/src
COPY build.gradle /app_build
COPY settings.gradle /app_build

# Install gradle
RUN curl https://downloads.gradle-dn.com/distributions/gradle-6.7-bin.zip -o /tmp/gradle.zip
RUN if [ "`sha256sum /tmp/gradle.zip | cut -d' ' -f1`" != "8ad57759019a9233dc7dc4d1a530cefe109dc122000d57f7e623f8cf4ba9dfc4" ];\
    then \
        echo "Error. This version of gradle is corrupted."; \
        exit 1;\
    fi && \
    mkdir -p /tmp/gradle && \
    unzip -q -d /tmp/gradle /tmp/gradle.zip &&\
    cp -Rf /tmp/gradle/gradle-*/bin/* /bin/ &&\
    cp -Rf /tmp/gradle/gradle-*/lib/* /lib/ &&\
    rm -Rf /tmp/gradle && rm -f /tmp/gradle.zip && \
    echo "Installed gradle `gradle -v`"

# Build
RUN cd /app_build &&\
    ./build.sh  && \
    mv dist /app && \
    cd / && \
    rm -Rf /app_build

RUN  chown 1000:1000 /app
USER nonroot
WORKDIR /app
ENTRYPOINT [ "java","-Djava.io.tmpdir=/tmp/apptmp","-jar","SoftwareStore.jar" ]

# Writable volumes
VOLUME /app/www/images/database
VOLUME /app/config

# tmpfs
VOLUME /app/sitemap

# tmpfs
VOLUME /tmp/apptmp
