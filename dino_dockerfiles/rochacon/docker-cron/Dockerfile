FROM golang:1.4-onbuild
ONBUILD COPY jobs/ /docker-jobs
ENTRYPOINT ["/go/bin/docker-cron"]
CMD ["-jobs", "/docker-jobs"]
