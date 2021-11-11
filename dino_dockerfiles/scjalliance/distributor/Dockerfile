FROM debian

RUN mkdir /git
WORKDIR /git

RUN apt-get update \
    && apt-get install -y \
       git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 9418

ENTRYPOINT ["git"]
CMD ["daemon", "--export-all", "--base-path=/git", "--listen=0.0.0.0", "--port=9418"]
