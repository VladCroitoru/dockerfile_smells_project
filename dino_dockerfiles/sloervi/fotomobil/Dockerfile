# Dockerfile fotomobil
FROM sloervi/ubuntu-perl-phatch:v1
MAINTAINER sloervi McMurphy <docker@sloervi.de>

LABEL Description="Create Docker Image for copying your Photos in a size suitable for your mobile device" Vendor="sloervi McMurphy" Version="1"

# Get some Python Packets
RUN apt-get install python python-wxgtk3.0 python-imaging findutils python-pyexiv2

# Get my scripts
RUN cd /usr/local/bin && git clone https://github.com/sloervi/fotomobil.git fotomobil

# Create User and group
RUN groupadd -r fotomobil && useradd -r -g fotomobil fotomobil
RUN chown -R fotomobil /usr/local/bin/fotomobil
RUN chmod u+x /usr/local/bin/fotomobil/fotomobil.sh
RUN chmod u+x /usr/local/bin/fotomobil/fotomobil.pl

VOLUME /indir
VOLUME /outdir

WORKDIR /indir

ENTRYPOINT /usr/local/bin/fotomobil/fotomobil.sh
