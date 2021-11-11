# Kallisto
# VERSION               0.42.3
#### # Kallisto - kallisto is a program for quantifying abundances of transcripts from RNA-Seq data # Nicolas L Bray, Harold Pimentel, Páll Melsted and Lior Pachter, Near-optimal probabilistic RNA-seq quantification # Nature Biotechnology 34, 525–527 (2016), doi:10.1038/nbt.3519 ####
#

FROM      combinelab/salmon:0.8.1
MAINTAINER Kapeel Chougule

LABEL Description="This image is used for running Salmon RNA seq qauntification tool "
RUN apt-get update && apt-get install -y build-essential

ADD Salmon_align.pl /usr/bin/
RUN [ "chmod", "+x",  "/usr/bin/Salmon_align.pl" ]
ENTRYPOINT ["Salmon_align.pl"]
