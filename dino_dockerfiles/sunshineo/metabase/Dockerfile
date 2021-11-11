# NOTE: this Dockerfile builds Metabase from source. We recommend deploying the pre-built
# images hosted on Docker Hub https://hub.docker.com/r/metabase/metabase/ which use the
# Dockerfile located at ./bin/docker/Dockerfile

FROM openjdk:8-jre

WORKDIR /app/source

# expose our default runtime port
EXPOSE 3000

ENV JAVA_HOME=/usr/lib/jvm/default-jvm
ENV PATH /usr/local/bin:$PATH
ENV LEIN_ROOT 1

ENV FC_LANG en-US
ENV LC_CTYPE en_US.UTF-8

# install core build tools
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python
RUN apt-get install -y g++
RUN apt-get install -y ttf-dejavu
RUN apt-get install -y fontconfig
#RUN ln -sf "${JAVA_HOME}/bin/"* "/usr/bin/"

# install lein
ADD https://raw.github.com/technomancy/leiningen/stable/bin/lein /usr/local/bin/lein
RUN chmod 744 /usr/local/bin/lein

# build the app
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g yarn

# add the application source to the image
ADD . /app/source
RUN bin/build

# build and then run it
ENTRYPOINT ["./bin/start"]
