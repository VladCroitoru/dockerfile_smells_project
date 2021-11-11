FROM progrium/cedarish
MAINTAINER Music Glue "devteam@musicglue.com"

RUN gem install slug-compiler --no-ri --no-rdoc
ADD ./scripts/ /compiler
ENTRYPOINT ["/compiler/start"]
