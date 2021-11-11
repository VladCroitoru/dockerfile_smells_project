FROM jvwong/pc_guide_bioc

MAINTAINER Pathway Commons <https://groups.google.com/forum/#!forum/pathway-commons-help/>

# Install the required packages from GitHub
RUN R -e 'devtools::install_github("jvwong/emRNASeq");'

# Apache ports
EXPOSE 80
EXPOSE 443
EXPOSE 8004

# Define default command.
CMD service opencpu restart && tail -F /var/log/opencpu/apache_access.log
