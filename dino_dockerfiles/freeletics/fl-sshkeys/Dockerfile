FROM python:2.7-slim-stretch
LABEL maintainer="Freeletics GmbH <operations@freeletics.com>"

RUN pip install awscli==1.14.17
RUN apt update \
  && apt install -y \
    bash \
    gawk \
  && rm -rf /var/lib/apt/lists/*

RUN adduser --uid 500 --system --disabled-login core
WORKDIR /

ENV IAM_GROUPS=""
USER core
COPY keys.sh /keys.sh
CMD ["/keys.sh"]
