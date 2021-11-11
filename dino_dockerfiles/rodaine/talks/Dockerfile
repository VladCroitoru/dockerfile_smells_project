FROM scratch
MAINTAINER Chris Roche <docker@rodaine.com>

EXPOSE 6060

COPY bin/present    /present
COPY vendor/present /static
COPY talks          /talks
COPY tmp            /tmp

WORKDIR /talks
ENTRYPOINT ["/present"]
CMD ["-base=/static", "-play=false", "-http=0.0.0.0:6060"]
