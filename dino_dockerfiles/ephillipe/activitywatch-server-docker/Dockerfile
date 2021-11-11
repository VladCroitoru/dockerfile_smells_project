FROM debian:stretch

ENV VERSION=0.7.1

# Requirements
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y dumb-init curl unzip \    
    && apt-get autoremove -y \
    && apt-get clean all

WORKDIR /activitywatch
ADD aw-server.ini /activitywatch/.config/activitywatch/aw-server/aw-server.ini
# Add aw user so we aren't running as root.
RUN useradd --home-dir /activitywatch --shell /bin/bash aw
RUN chown -R aw:aw /activitywatch
USER aw

# Installation
RUN curl -L -o /tmp/activitywatch.zip https://github.com/ActivityWatch/activitywatch/releases/download/v${VERSION}/activitywatch-v${VERSION}-linux-$(uname -m).zip \
    && unzip /tmp/activitywatch.zip -d / \
    && chmod -x /activitywatch/*.so* \
    && rm /tmp/activitywatch.zip

ENTRYPOINT ["/usr/bin/dumb-init","--"]
CMD ["/activitywatch/aw-server"]

EXPOSE 80
