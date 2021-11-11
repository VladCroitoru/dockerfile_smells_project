FROM progrium/buildstep:latest
MAINTAINER Lauri Nevala <lauri@kontena.io>

ADD init.sh /init.sh
RUN rm -fr /app

ONBUILD ADD . /app
ONBUILD RUN /build/builder

ENTRYPOINT ["/init.sh"]