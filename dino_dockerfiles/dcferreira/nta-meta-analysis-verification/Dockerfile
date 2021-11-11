FROM python:alpine
LABEL maintainer="dcferreira"

RUN apk --update add git openssh bash && \
    rm -rf /var/lib/apt/lists/* /var/cache/apk/*
RUN pip install simplejson six requests jsonschema

RUN git clone https://github.com/CN-TU/nta-meta-analysis-specification /ntarc-spec
RUN echo "#!/bin/sh" > entrypoint.sh && \
    echo "cd ntarc-verification; if [ \"\$1\" == \"all\" ]; then ./verify_all.sh \$2 /ntarc-spec; else ./verify.sh \$1 /ntarc-spec; fi" >> entrypoint.sh && \
    chmod +x entrypoint.sh

RUN mkdir /ntarc-verification && (cd /ntarc-verification && git init)
ADD verify.sh /ntarc-verification/verify.sh
ADD verify_all.sh /ntarc-verification/verify_all.sh

ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
