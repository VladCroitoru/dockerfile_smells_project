FROM ubuntu:17.04

ENV DMD_STABLE_VERSION 2.076.1

# Install dependencies:
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends build-essential ca-certificates curl git; \
	curl -fsS https://dlang.org/install.sh | bash -s dmd-${DMD_STABLE_VERSION}; \
	mkdir /dlang-build

WORKDIR /dlang-build
ADD build_and_run.d /dlang-build

RUN . ~/dlang/dmd-${DMD_STABLE_VERSION}/activate; \
    dmd -g -debug build_and_run.d; \
    chmod +x build_and_run

ENTRYPOINT ["/dlang-build/build_and_run"]
CMD ["--help"]
