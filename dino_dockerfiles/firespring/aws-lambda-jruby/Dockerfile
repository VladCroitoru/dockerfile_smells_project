FROM debian:stretch
MAINTAINER Firespring "info.dev@firespring.com"

# Add add-apt-repository
RUN apt-get update \
    && apt-get install -y software-properties-common

RUN apt-get update \
    && apt-get install default-jdk curl tar unzip -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add JRuby
ARG JRUBY_VERSION=9.2.0.0
RUN mkdir /opt/jruby \
  && curl -fSL https://s3.amazonaws.com/jruby.org/downloads/${JRUBY_VERSION}/jruby-bin-${JRUBY_VERSION}.tar.gz -o /tmp/jruby.tar.gz \
  && tar -zx --strip-components=1 -f /tmp/jruby.tar.gz -C /opt/jruby \
  && rm /tmp/jruby.tar.gz
ENV PATH /opt/jruby/bin:$PATH

RUN mkdir -p /usr/src/app/lib/ /usr/src/app/src/main/resources/ /usr/src/code/
WORKDIR /usr/src/app

# Add JRuby to the project
RUN cp /opt/jruby/lib/jruby.jar /usr/src/app/lib/jruby.jar \
    && cp -r /opt/jruby/lib/ruby/stdlib /usr/src/app/src/main/resources/ \
    && touch /usr/src/app/src/main/resources/stdlib/.jrubydir

# Add bundler to the stdlib dir in order to make it available to Java/JRuby
RUN jruby -S gem install bundle --no-ri --no-rdoc \
    && cp -r /opt/jruby/lib/ruby/gems/shared/gems/bundler*/lib/* /usr/src/app/src/main/resources/stdlib/

## Copy in the gradle project
COPY build.gradle /usr/src/app/
COPY src /usr/src/app/src

# Do a gradlew build, which also fetches gradle for the container
ARG GRADLE_VERSION=5.4.1
RUN curl -O https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \
    && unzip gradle-${GRADLE_VERSION}-bin.zip \
    && rm -f gradle-${GRADLE_VERSION}-bin.zip \
    && ./gradle-${GRADLE_VERSION}/bin/gradle wrapper

# Do a build just to verify the bundled files compile correctly
RUN ./gradlew build && rm -rf ./build

# Set our entrypoint
COPY entrypoint.sh /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
