FROM frolvlad/alpine-glibc
WORKDIR /opt/dropbox
RUN apk update && apk add --no-cache ca-certificates wget openssl
RUN wget -O dropbox.tar.gz "https://www.dropbox.com/download/?plat=lnx.x86_64" && tar -xvzf dropbox.tar.gz && rm dropbox.tar.gz
COPY dropbox-link.sh .
RUN chmod +x dropbox-link.sh
CMD ["/opt/dropbox/dropbox-link.sh"]