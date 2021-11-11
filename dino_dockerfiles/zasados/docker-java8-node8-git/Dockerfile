FROM openjdk:8-jre

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update -y && \
    apt-get -y install \
    nodejs \
    git && \
    rm -rf /var/lib/apt/lists/*