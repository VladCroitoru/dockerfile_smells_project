FROM alpine:3.4 

MAINTAINER Daniel Gusmão <dangusmao@hotmail.com>

# Install base packages
RUN apk update && apk upgrade \
 && apk add ca-certificates && update-ca-certificates \
 && apk add --update wget python tzdata

# Change TimeZone # ROOT
   ENV TZ=America/Bahia

# Clean APK cache
   RUN rm -rf /var/cache/apk/*

# # Download SpeedTest !
RUN wget -O /usr/local/bin/speedtest https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py && chmod +x /usr/local/bin/speedtest

ENTRYPOINT ["python","/usr/local/bin/speedtest"]
