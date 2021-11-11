FROM debian:jessie
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -yq rng-tools haveged && apt-get clean
RUN echo 'HRNGDEVICE=/dev/urandom'>> /etc/default/rng-tools
ENTRYPOINT ["haveged"]
CMD ["-F", "-v 1"]
