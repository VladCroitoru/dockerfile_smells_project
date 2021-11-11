FROM alpine
LABEL maintainer="rubengomez78@gmail.com"
RUN apk add --no-cache \
    git=2.15.0-r1 \
    openssh \
  && rm -rf /var/cache/apk
ENTRYPOINT ["git"]
VOLUME /root/
CMD ["help"]
