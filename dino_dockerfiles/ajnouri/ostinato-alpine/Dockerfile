FROM alpine

#RUN cat > /etc/apk/repositories  << __EOF__ 
#http://dl-cdn.alpinelinux.org/alpine/v3.3/main 
#http://dl-cdn.alpinelinux.org/alpine/v3.3/community 
#http://nl.alpinelinux.org/alpine/edge/main/ 
#http://nl.alpinelinux.org/alpine/edge/testing/ 
#__EOF__

RUN apk update && apk add wget

RUN wget http://nl.alpinelinux.org/alpine/edge/testing/x86_64/ostinato-0.7.1-r0.apk
RUN wget http://nl.alpinelinux.org/alpine/edge/testing/x86_64/ostinato-drone-0.7.1-r0.apk
RUN wget http://nl.alpinelinux.org/alpine/edge/testing/x86_64/ostinato-gui-0.7.1-r0.apk
RUN apk add ostinato-0.7.1-r0.apk
RUN apk add ostinato-drone-0.7.1-r0.apk
RUN apk add ostinato-gui-0.7.1-r0.apk
RUN apk add font-adobe-100dpi

RUN rm -rf /var/cache/apk/*

CMD ostinato
