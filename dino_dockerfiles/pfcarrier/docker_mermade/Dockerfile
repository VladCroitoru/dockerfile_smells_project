FROM debian:stretch

RUN apt-get update && \
    apt-get install -y \
      vim \
      curl \
      perl \
      perl-modules \
      ghostscript \
      libimage-magick-perl \
      sqlite3 \
      libdbd-sqlite3-perl \
      less \
      gcc \
      make

# github repo of the mermade project https://github.com/KorfLab/Mermade
RUN mkdir /mermade && \
    curl -sSL \
    http://korflab.ucdavis.edu/Datasets/BindNSeq/mermade_v1.03.tar.gz \
      | tar -xz -C /mermade --strip 1 && \
    chmod +x /mermade/reporter.pl

# Fix typo that prevent execution on linux/macos
RUN sed -i /mermade/kmer_counter.pl -e 's/Perl/perl/' && \
    sed -i /mermade/kmer_counter.pl -e 's/k:a/k:m:a/' && \
    sed -i /mermade/db_creator.pl -e 's/ls \([^\`]*\)/find \1 -type f/' && \
    sed -i /mermade/db_creator.pl -e 's/\*//'

# Recompile motifamatic for a linux target
RUN cd /mermade && \
    make

RUN mkdir /work

WORKDIR /work
ENV MERMADE=/mermade
ENV PATH=${PATH}:${MERMADE}:${MERMADE}/weblogo
ENV PERL5LIB="${MERMADE}:${PERL5LIB}"

CMD ["/bin/bash"]
