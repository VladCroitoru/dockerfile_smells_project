FROM dhspence/docker-baseimage:latest
MAINTAINER David H. Spencer <dspencer@wustl.edu>

LABEL \
  description="Haloplex QC scripts"

#COPY CalculateCoverageQC.071417.sh /usr/local/bin/
#COPY CoveragePlots.R /usr/local/bin/

#RUN ln -s /usr/bin/Rscript /usr/local/bin/

RUN ["cpanm", "Statistics::Basic" ]
RUN ["cpanm", "JSON" ]

