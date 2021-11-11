FROM progrium/cedarish:latest
MAINTAINER Ian Blenke <ian@blenke.com>

ADD ./runner /runner
ENTRYPOINT ["/runner/init"]

# add default port to expose (can be overridden)
ENV PORT 5000
EXPOSE 5000
