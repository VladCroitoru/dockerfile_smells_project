FROM parity/parity:v1.10.7

MAINTAINER Mateusz Probachta <mateusz.probachta@gmail.com>

EXPOSE 8545
EXPOSE 8546
EXPOSE 8180
EXPOSE 30303

COPY . /eth-env
WORKDIR /eth-env
RUN mkdir -p /ipc

ENTRYPOINT []

CMD ./run-parity.sh
