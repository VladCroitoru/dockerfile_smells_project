FROM alpine:3.8
MAINTAINER Ben Bridegs <07bridesb@gmail.com>

# When this Dockerfile was last refreshed (year/month/day)
ENV REFRESHED_AT 2018-03-01
ENV OAUTH2_PROXY_VERSION 2.2

# Checkout bitly's latest google-auth-proxy code from Github
RUN apk add --no-cache curl wget
RUN curl -s -L https://github.com/bitly/oauth2_proxy/releases/latest | egrep -o '/bitly/oauth2_proxy/releases/download/v[0-9]\.[0-9]/oauth2_proxy-[0-9]\.[0-9]\.[0-9]\.linux-amd64.go[0-9]\.[0-9]\.[0-9]\.tar.gz' | wget --base=http://github.com/ -i - -O /tmp/oauth2_proxy.tar.gz
RUN tar -xf /tmp/oauth2_proxy.tar.gz -C ./bin --strip-components=1 && rm /tmp/*.tar.gz

# Get startup script
ADD https://raw.githubusercontent.com/cheesemarathon/OAuth2-Proxy/master/startup.sh /
RUN chmod +x /startup.sh

# Install CA certificates
RUN apk add --no-cache ca-certificates

# Expose the ports we need and setup the ENTRYPOINT w/ the default argument
# to be pass in.
EXPOSE 8080 4180
ENTRYPOINT sh /startup.sh
