# use the base image to build with because we need to ensure that the library is built for the correct version
FROM parity/parity@sha256:4a33438fe4cbd73a6ad37874becf3215c77ac3d7a567992ebd3ee4142fabdb5a as faketime
USER root
RUN apt-get --yes update && apt-get install --yes git make gcc ca-certificates
RUN git clone https://github.com/wolfcw/libfaketime /libfaketime
WORKDIR /libfaketime
RUN make && make install

# v2.7.2-stable
FROM parity/parity@sha256:4a33438fe4cbd73a6ad37874becf3215c77ac3d7a567992ebd3ee4142fabdb5a

WORKDIR /
COPY --from=faketime /usr/local/lib/faketime/libfaketimeMT.so.1 /lib/faketime.so
COPY dev-key.json /home/parity/keys/DevChain/dev-key.json
COPY chain-spec.json /home/parity/chain-spec.json
COPY config.toml /home/parity/config.toml
RUN echo "" > /home/parity/password

ENV LD_PRELOAD="/lib/faketime.so"

ENTRYPOINT [ "/bin/parity", "--config", "/home/parity/config.toml" ]

# docker image build --tag keydonix/parity-instantseal .
# docker container run --rm -it -p 8000:8000 -p 8001:8001 -p 8545:8545 -p 8180:8180 --name parity-instant-seal keydonix/parity-instantseal
