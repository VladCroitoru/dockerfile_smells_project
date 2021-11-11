FROM alpine:edge
RUN apk add --update alpine-sdk linux-headers bash perl-dev libffi-dev openssl-dev python3-dev vim
WORKDIR /build

# ETH / XMR
RUN git clone https://github.com/maandree/libkeccak.git && \
	cd libkeccak && \
	make install
RUN git clone https://github.com/maandree/sha3sum.git && \
	cd sha3sum && \
	make keccak-256sum

# IOTA
RUN pip3 install pyota base58

RUN addgroup -S app && adduser -S -G app app
USER app
WORKDIR /home/app

RUN cp /build/sha3sum/keccak-256sum .
COPY . .

ENTRYPOINT ["/home/app/entrypoint.sh"]
