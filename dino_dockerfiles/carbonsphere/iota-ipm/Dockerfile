############################################################
# If this docker container helps you in anyway 
# please consider making a donation to the following address
# IOTA: FBIDRYFZKSYNGQICJTPPYAFUKYGCEVLCKHPKAXHLBGXJ9ENVRYYIYEMVQHIK9GNXFVILHYAKKPVBQSNTCBCKVPDM9Z
# ETH: 0xb205a4560bbc9840b80d36245333401e65d4f05e
# BTC: 395vsb41m46voFyhrgYMh6TauWKmNqJAtm
# Thanks!
############################################################


FROM node:9.1.0

MAINTAINER CarbonSphere <CarbonSphere@gmail.com>

COPY /docker-entrypoint.sh /
RUN npm install -g iota-pm && chmod +x /docker-entrypoint.sh


ENV WEB_PORT 80
ENV API_PORT 14265

ENV API_HOST http://127.0.0.1:${API_PORT}

EXPOSE $WEB_PORT

ENTRYPOINT ["/docker-entrypoint.sh"]

