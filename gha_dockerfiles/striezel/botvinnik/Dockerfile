# Note: This file contains four environment variables near the end. Change
# (#1)  these to match your settings or you will not be able to connect the bot
#       to a Matrix homeserver.

# Note: This Dockerfile uses multi-stage builds. Therefore, the required Docker
# (#2)  version is 17.05 or (preferably) a later version on the client and
#       server side of Docker.

# build stage
FROM debian:10-slim AS builder
LABEL maintainer="Dirk Stolle <striezel-dev@web.de>"
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y catch cmake g++ git libcurl4-gnutls-dev libsqlite3-dev pkg-config
RUN mkdir -p /opt/bvn
COPY ./ /opt/bvn
WORKDIR /opt/bvn
RUN mkdir build && cd build && cmake .. && make -j4 && ctest

# runtime stage
FROM debian:10-slim AS runner
LABEL maintainer="Dirk Stolle <striezel-dev@web.de>"
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends --no-install-suggests \
    ca-certificates libcurl3-gnutls libsqlite3-0 fortune-mod fortunes-min
# You may want to add more or other fortune packages here. See
# <https://packages.debian.org/en/buster/fortune-cookie-db> for more packages.
COPY --from=builder /opt/bvn/build/src/botvinnik/botvinnik /usr/local/bin/botvinnik
# Create new user that will be used to run the program.
RUN useradd --create-home bot
USER bot
WORKDIR /home/bot
# Test that executable is reachable via PATH variable.
RUN botvinnik --version
RUN mkdir -p /home/bot/.bvn

# Note: Change these four variables to match your setup!
ENV HOMESERVER=https://matrix.org/
ENV BOT_USER=@alice-and-bob:charlie.tld
ENV BOT_PASSWORD=secret
ENV BOT_STOP_USER=@charlie:charlie.tld
# Generate configuration file.
RUN echo "matrix.homeserver=$HOMESERVER" > /home/bot/.bvn/bvn.conf && \
    echo "matrix.userid=$BOT_USER" >> /home/bot/.bvn/bvn.conf && \
    echo "matrix.password=$BOT_PASSWORD" >> /home/bot/.bvn/bvn.conf && \
    echo "bot.stop.allowed.userid=$BOT_STOP_USER" >> /home/bot/.bvn/bvn.conf

CMD botvinnik
