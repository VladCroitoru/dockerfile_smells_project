FROM nginx:alpine

# remove trash
RUN rm -f /etc/nginx/fastcgi* /etc/nginx/koi* /etc/nginx/win* /etc/nginx/*.default /etc/nginx/*_params /etc/conf.d/*.conf 

RUN apk update && apk add -u python3 py3-requests openssl curl mc git && \
    mkdir /persist && \
    curl -L -o /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.1.1/dumb-init_1.1.1_amd64 && \
    chmod 755 /usr/bin/dumb-init && \
    cd && git clone https://github.com/Neilpang/acme.sh.git acmegit && \
    cd acmegit && sh acme.sh \
	--install \
	--certhome /persist/certs \
	--accountkey /persist/account.key && \
    apk del git && \
    rm -Rf /root/acmegit && rm -Rf /var/cache/apk/*

COPY keeper.py /bin/nginx-keeper
RUN chmod 755 /bin/nginx-keeper

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["nginx-keeper"]
