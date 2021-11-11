FROM golang

RUN go version

############# INITIAL SETUP/INSTALLATION #############
# non-root user
#RUN useradd -m -u 8877 wikispeech

# setup apt
RUN apt-get update -y && apt-get upgrade -y && apt-get install apt-utils -y

# debugging tools
# RUN apt-get install -y libnet-ifconfig-wrapper-perl/stable curl wget emacs

# RELEASE variable (to be set by build args)
ARG RELEASE="undefined"

LABEL "se.stts.vendor"="STTS - Speech technology services - http://stts.se"
LABEL "se.stts.release"=$RELEASE


############# COMPONENT SPECIFIC DEPENDENCIES #############
RUN apt-get install -y sqlite3 gcc build-essential
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8


############# PRONLEX #############
ENV BASEDIR /wikispeech/pronlex
RUN mkdir -p $BASEDIR/bin
ENV PRONLEXPATH=$BASEDIR/git

# local copy of https://github.com/stts-se/pronlex.git
COPY . $PRONLEXPATH

WORKDIR $PRONLEXPATH
RUN cd $PRONLEXPATH/lexserver && go get && go install
RUN cd $PRONLEXPATH/cmd/lexio/createEmptyDB && go get && go install
RUN cd $PRONLEXPATH/cmd/lexio/importLex && go get && go install
RUN cd $PRONLEXPATH/cmd/lexio/importSql && go get && go install

WORKDIR $BASEDIR

RUN ln -s $PRONLEXPATH/docker/setup $BASEDIR/bin/setup
RUN ln -s $PRONLEXPATH/docker/import_all $BASEDIR/bin/import_all
RUN chmod +x $BASEDIR/bin/*

ENV APPDIR $BASEDIR/appdir


############# POST INSTALL #############
WORKDIR $BASEDIR

# BUILD INFO
ENV BUILD_INFO_FILE $BASEDIR/build_info.txt
RUN echo "Application name: pronlex" >> $BUILD_INFO_FILE
RUN echo -n "Build timestamp: " >> $BUILD_INFO_FILE
RUN date --utc "+%Y-%m-%d %H:%M:%S %Z" >> $BUILD_INFO_FILE
RUN echo "Built by: docker" >> $BUILD_INFO_FILE
RUN echo "Release: $RELEASE" >> $BUILD_INFO_FILE
RUN cat $BUILD_INFO_FILE


############# RUNTIME SETTINGS #############
WORKDIR $BASEDIR
#RUN chown -R wikispeech.wikispeech /wikispeech
#USER wikispeech
EXPOSE 8787

CMD ($BASEDIR/bin/setup $APPDIR && lexserver -test -ss_files $APPDIR/symbol_sets -db_files $APPDIR/db_files -static  $PRONLEXPATH/lexserver/static && lexserver -ss_files $APPDIR/symbol_sets -db_files $APPDIR/db_files -static  $PRONLEXPATH/lexserver/static 8787)

