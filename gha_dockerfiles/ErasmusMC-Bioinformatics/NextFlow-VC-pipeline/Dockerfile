FROM mambaorg/micromamba:latest
USER root
COPY env.yaml /root/env.yaml
RUN apt clean && apt update && apt upgrade -y
RUN apt install -y procps zip perl-modules libgd-dev cpanminus \
    r-base circos parallel libmagick++-dev libclone-perl \
    libconfig-general-perl libfont-ttf-perl libgd-perl libsvg-perl \
    libregexp-common-perl libtext-format-perl libtext-soundex-perl \
    libstatistics-basic-perl liblist-moreutils-perl libmath-bezier-perl \
    libmath-round-perl libparams-validate-perl libreadonly-perl libset-intspan-perl
RUN apt clean && apt purge
RUN cpanm install GD::Polyline
RUN cpanm install Math::VecStat
RUN micromamba install -y -n base -f /root/env.yaml &&\
    micromamba clean --all --yes
RUN jar xf /opt/conda/share/hmftools-purple-*/purple.jar circos/
RUN cp circos/gaps.38.txt circos/gaps.txt &&\
    mv circos/circos.template circos/circos.conf &&\
    mv circos/input.template circos/input.conf &&\
    mv circos/* /opt/conda/pkgs/circos-*/etc/. &&\
    rm -r circos

ENV export LC_ALL=C
ENV TERM=xterm

LABEL Author "Dennis Dollee"
#locale-gen en_US.UTF-8
