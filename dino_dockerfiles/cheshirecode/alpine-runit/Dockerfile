FROM alpine

# base
RUN apk add --no-cache openntpd inotify-tools runit curl && \
  sh -c "nohup ntpd -d -f /etc/ntpd.conf -s > /dev/null 2>&1 &"

CMD tail -f /dev/null