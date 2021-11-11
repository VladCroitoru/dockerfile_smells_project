FROM alpine:latest

LABEL maintainer="Tiago Rodrigues <mail@tig.pt>"

##################
#  Install curl  #
##################

RUN apk add --no-cache curl

######################
#    Run crond       #
# -f for Foreground  #
######################

CMD ["/usr/sbin/crond", "-f"]
