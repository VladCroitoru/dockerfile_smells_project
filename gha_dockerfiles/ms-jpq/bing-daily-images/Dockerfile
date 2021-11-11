FROM python:alpine


COPY ./bing /bing
VOLUME /data

ENTRYPOINT ["/bing/daemon.sh"]
CMD ["--out", "/data", "--days", "14"]
