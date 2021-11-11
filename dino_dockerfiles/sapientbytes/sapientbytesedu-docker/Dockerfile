FROM sapientbytes/sapientbytes-maven-docker

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install -y \
    apt-utils \
    curl \
    unzip

ENV M2_HOME "/opt/apache-maven-3.5.3"
ENV PATH "$PATH:$M2_HOME/bin"

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

RUN [ "cross-build-end" ]
