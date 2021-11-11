FROM groovy:jdk15 AS base

USER root

RUN apt-get update \
	&& apt-get install -y \
		maven \
	&& rm -rf /var/lib/apt/lists/*

FROM base AS build

WORKDIR /app
ADD . .
# RUN mvn clean compile
# RUN mvn clean test

# FROM base
