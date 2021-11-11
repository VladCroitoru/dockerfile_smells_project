FROM            docker.io/livelace/gentoo:latest

ENV             GIRIE_BIN="/usr/local/bin/girie"

COPY            "work/girie" $GIRIE_BIN

USER            "user"

WORKDIR         "/home/user"

CMD             ["/usr/local/bin/girie"]
