FROM rocker/rstudio

MAINTAINER Christian Brenninkmeijer <Christian.Brenninkmeijer@manchester.ac.uk>

# See https://cran.r-project.org/bin/linux/ubuntu/README
RUN echo "deb http://mirrors.ebi.ac.uk/CRAN/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list

#Install curl, R, and R packages
RUN apt-get update  && apt-get install -y --force-yes \
    curl 
    
RUN \   
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/ade4_1.7-2.tar.gz > ade4_1.7-2.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/RColorBrewer_1.1-2.tar.gz > RColorBrewer_1.1-2.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/gtools_3.5.0.tar.gz > gtools_3.5.0.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/gdata_2.17.0.tar.gz > gdata_2.17.0.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/bitops_1.0-6.tar.gz > bitops_1.0-6.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/caTools_1.17.1.tar.gz > caTools_1.17.1.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/KernSmooth_2.23-15.tar.gz > KernSmooth_2.23-15.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/gplots_2.17.0.tar.gz > gplots_2.17.0.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/scatterplot3d_0.3-36.tar.gz > scatterplot3d_0.3-36.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/made4_1.42.0.tar.gz > made4_1.42.0.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/impute_1.42.0.tar.gz > impute_1.42.0.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/highr_0.5.1.tar.gz > highr_0.5.1.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/repr_0.4.tar.gz > repr_0.4.tar.gz 

RUN ls -al

RUN R CMD INSTALL \ 
        ade4_1.7-2.tar.gz \
        RColorBrewer_1.1-2.tar.gz \
        gtools_3.5.0.tar.gz \
        gdata_2.17.0.tar.gz \
        bitops_1.0-6.tar.gz \ 
        caTools_1.17.1.tar.gz \
        KernSmooth_2.23-15.tar.gz \
        gplots_2.17.0.tar.gz \
        scatterplot3d_0.3-36.tar.gz \
        made4_1.42.0.tar.gz \
        impute_1.42.0.tar.gz \
        highr_0.5.1.tar.gz \
        repr_0.4.tar.gz 

RUN \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/getopt_1.20.0.tar.gz > getopt_1.20.0.tar.gz && \
    curl https://raw.githubusercontent.com/Christian-B/galaxy_shedtools/master/r_extended/optparse_1.3.2.tar.gz > optparse_1.3.2.tar.gz && \
    ls -al

RUN R CMD INSTALL \ 
        getopt_1.20.0.tar.gz \
        optparse_1.3.2.tar.gz 



