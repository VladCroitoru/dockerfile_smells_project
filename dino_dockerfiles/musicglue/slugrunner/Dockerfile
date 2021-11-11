FROM progrium/cedarish
MAINTAINER Music Glue "devteam@musicglue.com"

RUN useradd -d /app -m app
ADD ./runner/ /runner
ENTRYPOINT ["/runner/appuserexec"]
