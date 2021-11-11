FROM williamyeh/ansible:alpine3

RUN apk --update add \
  curl \
  bash \
  git \
  && rm /var/cache/apk/*

# Download semaphore
ADD https://github.com/ansible-semaphore/semaphore/releases/download/v2.0.2/semaphore_linux_amd64 /usr/bin/semaphore
RUN chmod +x /usr/bin/semaphore

VOLUME /tmp/semaphore

EXPOSE 3000
