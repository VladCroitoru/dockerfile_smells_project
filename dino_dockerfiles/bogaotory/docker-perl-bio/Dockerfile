FROM perl:5.20
MAINTAINER Bo Gao (bogao@dcs.warwick.ac.uk)
LABEL Description="Image which includes some essential biology APIs"

ENV LIB_NCPAN_PERL /root/lib-perl

RUN mkdir $LIB_NCPAN_PERL

RUN cd $LIB_NCPAN_PERL \
 && git clone https://github.com/Ensembl/ensembl-git-tools.git \
 && echo 'export PATH="'$LIB_NCPAN_PERL'/ensembl-git-tools/bin:$PATH"' >> /root/.profile

WORKDIR $LIB_NCPAN_PERL

RUN . /root/.profile \
 && git ensembl --clone api \
 && echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensembl/modules:$PERL5LIB"' 			>> /root/.profile \
 && echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensembl-compara/modules:$PERL5LIB"' 	>> /root/.profile \
 && echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensembl-funcgen/modules:$PERL5LIB"' 	>> /root/.profile \
 && echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensembl-io/modules:$PERL5LIB"' 	>> /root/.profile \
 && echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensembl-variation/modules:$PERL5LIB"' 	>> /root/.profile

RUN git clone https://github.com/EnsemblGenomes/ensemblgenomes-api.git \
 && echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/ensemblgenomes-api/modules:$PERL5LIB"' >> /root/.profile

RUN git clone git://github.com/bioperl/bioperl-live.git \
 && git clone https://github.com/bioperl/Bio-EUtilities.git \
 && echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/bioperl-live:$PERL5LIB"' 		>> /root/.profile \
 && echo 'export PERL5LIB="'$LIB_NCPAN_PERL'/Bio-EUtilities/lib:$PERL5LIB"' >> /root/.profile

ENV PERL5LIB $LIB_NCPAN_PERL/ensembl/modules:$LIB_NCPAN_PERL/ensembl-compara/modules:$LIB_NCPAN_PERL/ensembl-funcgen/modules:$LIB_NCPAN_PERL/ensembl-io/modules:$LIB_NCPAN_PERL/ensembl-variation/modules:$LIB_NCPAN_PERL/bioperl-live:$LIB_NCPAN_PERL/Bio-EUtilities/lib

WORKDIR /root

CMD bash -l
