FROM progrium/buildstep:latest

MAINTAINER bobtfish@bobtfish.net

RUN mkdir /app;sed -i -e's/raw.github.com/raw.githubusercontent.com/' /build/buildpacks/heroku-buildpack-perl/bin/compile 
ADD /app.psgi /app/app.psgi
ADD /cpanfile /app/cpanfile
RUN /build/builder
USER nobody
EXPOSE 5000
CMD ["/bin/bash", "-c", "/start web"]

