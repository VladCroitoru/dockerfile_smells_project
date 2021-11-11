#Note that for the upload command to work, the AWS access key and the AWS
# secret key must be args in the docker run command as environment vaiables, 
# along with the WB release and species with bioproject, as below.
# Example invocation:

#     docker build --no-cache -f Dockerfile -t test-protein . 
#     docker run --rm  \
#                -e "WB_RELEASE=280" \
#                -e "WB_SPECIES=c_nigoni_PRJNA384657" \
#                -e "AWS_ACCESS_KEY=<access_key>" \
#                -e "AWS_SECRET_KEY=<secret key>" \
#                 test-protein

# The script "single_species_build.sh" is currently hard coded to do the
# processing and assumes that the target S3 bucket is the one used for AGR's
# main JBrowse instance, agrjbrowse, and the path is /mod-jbrowses/test (but
# this will change with the next WB release),  

FROM gmod/jbrowse-gff-base:latest 

LABEL maintainer="scott@scottcain.net"


#RUN git clone --single-branch --branch main https://github.com/WormBase/website-jbrowse-protein.git
RUN git clone --single-branch --branch main https://github.com/WormBase/website-jbrowse-protein.git
RUN git clone --single-branch --branch protein-283 https://github.com/WormBase/website-genome-browsers.git
RUN git clone --single-branch --branch master https://github.com/alliance-genome/agr_jbrowse_config.git

RUN cp  /website-jbrowse-protein/single_species_build.sh / && \
    cp  /website-jbrowse-protein/parallel.sh / && \
    cp  /website-genome-browsers/protein_schematic/bin/log4perl.conf / && \
    mkdir -p /jbrowse/data/ && \
    cp -r /website-genome-browsers/protein_schematic/jbrowse/data /jbrowse/data


VOLUME /data
#ENTRYPOINT ["/bin/sh", "/docker-wrapper.sh"]

#CMD ["/bin/bash", "/single_species_build.sh"]
CMD ["/bin/bash", "/parallel.sh"]
