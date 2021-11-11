FROM scratch
MAINTAINER Wander Nauta

ENV ROOT="/data/" IP="0.0.0.0" UID="0" GID="0"
EXPOSE 53
COPY ./bin/tinydns /bin/tinydns
CMD ["/bin/tinydns"]
