FROM perl:5.30.0
LABEL maintainer="dave@perlhacks.org"

EXPOSE 1701
CMD carton exec starman --port 1701 Succession/bin/app.psgi

RUN cpanm Carton Starman

COPY . /succession
RUN cd /succession && carton install --deployment
WORKDIR /succession
