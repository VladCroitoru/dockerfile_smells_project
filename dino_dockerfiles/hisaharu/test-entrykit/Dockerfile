FROM ubuntu:14.04.2
RUN : \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
 && :
RUN : \
 && curl -L https://github.com/progrium/entrykit/releases/download/v0.4.0/entrykit_0.4.0_Linux_x86_64.tgz | tar -xvz \
 && mv entrykit /bin/entrykit \
 && chmod +x /bin/entrykit \
 && entrykit --symlink \
 && :
COPY ./fuga.tmpl /fuga.tmpl
ENV \
  hoge=foo \
  :=:
ENTRYPOINT ["render", "/fuga", "--", "sleep", "60"]

