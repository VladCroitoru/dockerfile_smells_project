FROM alpine:latest
CMD ip route | grep '^default' | awk '{ print $3 ; exit }'
