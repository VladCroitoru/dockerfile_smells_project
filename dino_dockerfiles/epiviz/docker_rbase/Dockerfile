FROM bioconductor/devel_core

RUN install2.r --error devtools

RUN installGithub.r epiviz/epivizr

COPY installPackage.r /usr/bin/installPackage.r
RUN chmod u+x /usr/bin/installPackage.r
