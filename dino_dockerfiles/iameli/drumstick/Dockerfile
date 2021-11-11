FROM ubuntu:xenial

WORKDIR /build

ADD packages.txt /build/packages.txt
RUN apt-get update && cat packages.txt | xargs apt-get install -y

ADD get-node.sh /build/get-node.sh
RUN /build/get-node.sh

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
  apt-get update && apt-get install -y yarn

RUN npm install -g babel-cli webpack grunt-cli nodemon jest-cli

RUN pip install awscli

ADD init-env.fish /build/init-env.fish

RUN chmod 755 /build/init-env.fish
RUN fish /build/init-env.fish

ADD entrypoint.fish /build/entrypoint.fish
RUN chmod 755 /build/entrypoint.fish

ENV DRUMSTICK_DOCKER_VERSION 1.12.5

RUN curl -L -o /build/docker.tgz https://get.docker.com/builds/Linux/x86_64/docker-$DRUMSTICK_DOCKER_VERSION.tgz && \
  (cd /build && tar xzvf /build/docker.tgz) && \
  mv /build/docker/docker /usr/bin/docker && \
  rm -rf /build/docker /build/docker.tgz

# Boot up... and do nothing at all.
CMD /build/entrypoint.fish
