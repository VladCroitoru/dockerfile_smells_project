ARG             IMAGE_TAG

FROM            harbor-core.k8s-2.livelace.ru/dev/clmixer:${IMAGE_TAG}

ENV             CLMIXER_BIN="/usr/local/bin/clmixer"

# copy application.
COPY            "work/clmixer" "$CLMIXER_BIN"

USER            "user"

WORKDIR         "/home/user"

CMD             ["/usr/local/bin/clmixer"]
