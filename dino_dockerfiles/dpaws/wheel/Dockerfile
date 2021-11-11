FROM alpine
MAINTAINER Justin Menga <justin.menga@gmail>

RUN apk add --update --no-cache bash python python-dev openssl-dev libffi-dev musl-dev git gcc py-pip
RUN pip install wheel

# Packages volume
VOLUME /packages

# Build wheels for packages
ENTRYPOINT ["pip", "wheel", "-w", "/packages", "-r", "/packages/requirements.txt"]