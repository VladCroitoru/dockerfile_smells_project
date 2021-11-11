FROM perl:5.24.2
LABEL "maintainer=github.com/rbtr"
WORKDIR /
RUN apt-get update \
  && apt-get install -y unzip \
  && cpan File::Copy::Recursive File::Glob LWP::Simple TVDB::API Getopt::Long Switch WWW::TheMovieDB JSON::Parse XML::Simple
RUN curl -O https://pilotfiber.dl.sourceforge.net/project/sorttv/SortTV1.37.zip \
  && unzip SortTV1.37.zip
ENTRYPOINT perl /sorttv/sorttv.pl
