FROM openjdk:8u121

RUN mkdir /static/public -p

COPY ./app/static/public /static/public
COPY ./docker/entrypoint /entrypoint

ADD ./app/build/distributions/app-boot.tar /

ARG SPRING_PROFILES_ACTIVE
ENV SPRING_PROFILES_ACTIVE $SPRING_PROFILES_ACTIVE

# This path is needed for the eventual configuration
RUN mkdir -p /etc/hint

ENTRYPOINT ["/entrypoint"]
