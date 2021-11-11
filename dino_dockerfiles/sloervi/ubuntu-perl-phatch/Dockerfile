# Dockerfile ubuntu-perl-phatch
FROM acdaic4v/ubuntu-perl-redis:v1
MAINTAINER sloervi McMurphy <docker@sloervi.de>
# Pakete nachinstallieren
RUN apt-get update && apt-get install -y phatch git libimage-exiftool-perl

# Perl Modules 
RUN cpanm Image::ExifTool

# CPAN- Directory: CLean Up
RUN rm -rf .cpanm

