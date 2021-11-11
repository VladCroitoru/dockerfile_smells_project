FROM openjdk:8-jre-slim

WORKDIR /app
RUN apt-get update \
      && apt-get -y --no-install-recommends install curl \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/*

ARG VERSION="0.9.16"
RUN curl -o /bin/digdag --create-dirs -L "https://dl.digdag.io/digdag-${VERSION}" && chmod u+x /bin/digdag

ENTRYPOINT ["java", "-jar", "/bin/digdag"]
