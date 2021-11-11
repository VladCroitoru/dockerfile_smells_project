## Based on rocker / hadleyverse maintained by Carl Boettiger and Dirk Eddelbuettel
FROM rocker/hadleyverse

MAINTAINER "Daniel Gatti" dan.gatti@jax.org

# install additional BioC scripts
RUN install2.r --error qtl
# DOQTL and dependencies.
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(c("AnnotationHub", "DOQTL", "VariantAnnotation", "limma", "DESeq2", "edgeR"), ask=FALSE)'
# Chesler haplotype probabilities.
RUN mkdir -p /data
RUN wget --directory-prefix=/data ftp://ftp.jax.org/dgatti/logan_haploprobs.Rdata
# Chesler phenotypes.
RUN wget --directory-prefix=/data ftp://ftp.jax.org/dgatti/logan_phenotypes.Rdata
# Chesler hippocampus experssion data.
RUN wget --directory-prefix=/data ftp://ftp.jax.org/dgatti/chesler_hippocampus_expr.Rdata
RUN chmod --recursive 755 /data
# Chesler tutorial
RUN wget --directory-prefix=/data ftp://ftp.jax.org/dgatti/addiction_DOQTL_tutorial.html
RUN wget --directory-prefix=/data ftp://ftp.jax.org/dgatti/addiction_DOQTL_tutorial.Rmd
RUN wget --directory-prefix=/data ftp://ftp.jax.org/dgatti/addiction_DOQTL_tutorial.R
RUN wget --directory-prefix=/data ftp://ftp.jax.org/dgatti/DO.impute.founders.png
RUN wget --directory-prefix=/data ftp://ftp.jax.org/dgatti/haploprobs3D.png
# Load the AnnotationHub cache.
RUN Rscript -e 'library("AnnotationHub"); hub = AnnotationHub()'
RUN ln -s /data ~/data
# Data for differential expression analysis
RUN mkdir -p /deseq
RUN wget --directory-prefix=/deseq http://raw.githubusercontent.com/simecek/AddictionCourse2015/master/data/Hippocampus_Exp_for_DE_analysis.txt
RUN wget --directory-prefix=/deseq http://raw.githubusercontent.com/simecek/AddictionCourse2015/master/data/Hippocampus_Exp_Design_for_DE_analysis.txt
RUN chmod --recursive 755 /deseq
