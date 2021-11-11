FROM sameersbn/gitlab-ci-runner:latest
MAINTAINER sameer@damagehead.com

RUN apt-get update && apt-get install -y curl

RUN curl -sL https://deb.nodesource.com/setup | bash -

RUN apt-get update && \
    apt-get install -y build-essential nodejs \
    git lftp p7zip-full && \
    rm -rf /var/lib/apt/lists/* # 20140918

ADD assets/ /app/
RUN chmod 755 /app/setup/install
RUN /app/setup/install
