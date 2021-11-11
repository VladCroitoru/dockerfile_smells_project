# ------------------------------------------------------------- shellcheck-build

ARG SHELLCHECK_BUILDER_BASE_IMAGE="fleshgrinder/debian:stretch-build"
ARG SHELLCHECK_BASE_IMAGE="fleshgrinder/debian:stretch"

# hadolint ignore=DL3006
FROM ${SHELLCHECK_BUILDER_BASE_IMAGE} AS shellcheck-build

ARG SHELLCHECK_VERSION_REF="master"

WORKDIR /usr/src/shellcheck

RUN apt-install git ghc cabal-install \
 && git clone https://github.com/koalaman/shellcheck.git . \
 && git checkout ${SHELLCHECK_VERSION_REF} \
 && cabal update && cabal install

ENV PATH="$PATH:/root/.cabal/bin"

RUN mkdir -p  /package/bin /package/lib \
 && cp "$(command -v shellcheck)" /package/bin/ \
 && ldd "$(command -v shellcheck)" | grep "=> /" | awk '{print $3}' | xargs -I '{}' cp -v '{}' /package/lib/

# ------------------------------------------------------------------- shellcheck

# hadolint ignore=DL3006
FROM ${SHELLCHECK_BASE_IMAGE} AS shellcheck

COPY --from=shellcheck-build /package/bin/ /usr/local/bin/
COPY --from=shellcheck-build /package/lib/ /usr/local/lib/
COPY resources/docker/bin/shellcheckw /usr/local/bin/shellcheckw

RUN apt-install bash file \
 && ldconfig /usr/local/lib

ENTRYPOINT ["shellcheckw"]
