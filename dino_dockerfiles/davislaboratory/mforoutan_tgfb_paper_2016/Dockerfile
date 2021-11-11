# Please note that this Dockerfile corresponds to the davislaboratory/mforoutan_tgfb_paper_2016
# image, which is the initial version of the study. There are two images for the new version of the study.
# Please see https://github.com/DavisLaboratory/mforoutan_tgfb_paper_2016 for more information.

FROM davislaboratory/docker-rstudio-server
MAINTAINER soroorh <hediyehzadeh.s@wehi.edu.au>
RUN git clone https://soroorh@bitbucket.org/soroorh/mforoutan_tgfb_paper_2016.git 
RUN ln -s /mforoutan_tgfb_paper_2016/output /home/davislab/output
RUN ln -s /mforoutan_tgfb_paper_2016/scripts /home/davislab/scripts
RUN ln -s /mforoutan_tgfb_paper_2016/data /home/davislab/data
RUN chown -R davislab:davislab /home/davislab/output/figures
RUN chmod 700 /home/davislab/output/figures
RUN chown -R davislab:davislab /home/davislab/output/results
RUN chmod 700 /home/davislab/output/results
RUN chown -R davislab:davislab /home/davislab/data/comparative_analysis/probe_gene_mapping/out_10data_check
RUN chmod 700 /home/davislab/data/comparative_analysis/probe_gene_mapping/out_10data_check
RUN git clone https://soroorh@bitbucket.org/soroorh/mforoutan_paper_rdata.git 
RUN mv /mforoutan_paper_rdata/randRanks_up.RData /home/davislab/data/comparative_analysis/probe_gene_mapping/out_10data_check
RUN mv /mforoutan_paper_rdata/CI99_up.RData /home/davislab/data/comparative_analysis/probe_gene_mapping/out_10data_check
RUN mv /mforoutan_paper_rdata/CI99_down.RData /home/davislab/data/comparative_analysis/probe_gene_mapping/out_10data_check
RUN mv /mforoutan_paper_rdata/down_permute_dens.RData /home/davislab/data/comparative_analysis/probe_gene_mapping/out_10data_check
RUN mv /mforoutan_paper_rdata/up_permute_dens.RData /home/davislab/data/comparative_analysis/probe_gene_mapping/out_10data_check
RUN git clone https://soroorh@bitbucket.org/soroorh/mforoutan_paper_rdata_2.git
RUN mv /mforoutan_paper_rdata_2/randRanks_down.RData /home/davislab/data/comparative_analysis/probe_gene_mapping/out_10data_check
RUN chown -R davislab:davislab /home/davislab/data/integrative_analysis/out_10data_check
RUN chmod 700 /home/davislab/data/integrative_analysis/out_10data_check
RUN mv /mforoutan_paper_rdata_2/Heiser /home/davislab/data/Heiser
RUN mv /mforoutan_paper_rdata_2/COSMIC /home/davislab/data/COSMIC
RUN (Rscript -e 'install.packages(c("dplyr","hexbin","colorRamps","survival","XML","ggplot2","matrixStats"), repos="http://cran.rstudio.com/")')
RUN (Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(c("limma","GSVA", "sva","org.Hs.eg.db"))')  
WORKDIR /mforoutan_tgfb_paper_2016
RUN mv generate_all_experiments.R /home/davislab
