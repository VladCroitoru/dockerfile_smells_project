FROM davislaboratory/docker-rstudio-server
MAINTAINER soroorh <hediyehzadeh.s@wehi.edu.au>
RUN git clone https://soroorh@bitbucket.org/soroorh/mforoutan_tgfb_2017_tumour.git 
RUN ln -s /mforoutan_tgfb_2017_tumour/output /home/davislab/output
RUN ln -s /mforoutan_tgfb_2017_tumour/scripts /home/davislab/scripts
RUN ln -s /mforoutan_tgfb_2017_tumour/data /home/davislab/data
RUN chown -R davislab:davislab /home/davislab/data/TCGA/panCancer
RUN chmod 700 /home/davislab/data/TCGA/panCancer
RUN chown -R davislab:davislab /home/davislab/output/figures
RUN chmod 700 /home/davislab/output/figures
RUN chown -R davislab:davislab /home/davislab/output/results
RUN chmod 700 /home/davislab/output/results
RUN chown -R davislab:davislab /home/davislab/output/results/supplementary
RUN chmod 700 /home/davislab/output/results/supplementary
RUN (Rscript -e 'install.packages(c("dplyr","hexbin","colorRamps","survival","XML","ggplot2","matrixStats"), repos="http://cran.rstudio.com/")')
RUN (Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(c("limma","GSEABase","GSVA", "sva","org.Hs.eg.db"))')  
WORKDIR /mforoutan_tgfb_2017_tumour
RUN mv generate_all_experiments.R /home/davislab 
