FROM quay.io/evryfs/base-ubuntu:focal-20211006
LABEL maintainer "fsdevops@evry.com"
RUN curl -L https://github.com/google/mtail/releases/download/v3.0.0-rc36/mtail_v3.0.0-rc36_linux_amd64 -o /usr/local/bin/mtail && chmod a+x /usr/local/bin/mtail
COPY progs /progs
EXPOSE 3903
CMD ["mtail", "-logtostderr", "-logs", "/_diag/*", "-progs", "/progs"]
