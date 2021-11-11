FROM alpine:latest

# Prepare to fetch the latest binary from GitHub
RUN apk update && apk add --no-cache curl tzdata openssl ca-certificates && update-ca-certificates

# Configure the timezone
RUN cp /usr/share/zoneinfo/${TIMEZONE:-Europe/London} /etc/localtime

# Grab the latest linux binary
RUN curl -o /bin/xur-notify -Ls $(curl -s https://api.github.com/repos/cmacrae/xur-notify/releases | fgrep browser_download_url | fgrep linux | cut -d '"' -f 4 | head -n 1) && chmod +x /bin/xur-notify

# Write a crontab to run xur-notify at 10:01AM UTC on Friday
RUN echo -e "1\t10\t*\t*\t5\t/bin/xur-notify &> /dev/stdout" > /etc/crontabs/root
ENTRYPOINT ["/usr/sbin/crond"]
CMD ["-f"]
