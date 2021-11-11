FROM mgymrek/docker-rstudio-server
MAINTAINER Melissa Gymrek <mgymrek@mit.edu>
RUN mkdir -p /scripts
RUN mkdir -p /data
RUN wget http://gbsc-share.stanford.edu/HGDP_RNAseq/scripts/technical_replicates/supplemental_script_input_files/gene_fpkm_table_run1.txt
RUN wget http://gbsc-share.stanford.edu/HGDP_RNAseq/scripts/technical_replicates/supplemental_script_input_files/gene_fpkm_table_run2.txt
RUN wget http://gbsc-share.stanford.edu/HGDP_RNAseq/scripts/allele_specific_expression/supplemental_script_input_files/ase_total30_sample30.csv
RUN mv gene_fpkm_table_run1.txt /data
RUN mv gene_fpkm_table_run2.txt /data
RUN mv ase_total30_sample30.csv /data
RUN ln -s /scripts /home/guest/scripts
RUN ln -s /data /home/guest/data
RUN Rscript -e 'install.packages(c("ops","gplots"), repos="http://cran.rstudio.com/")'
ADD martin_etal_figS1.R /scripts/martin_etal_figS1.R
ADD martin_etal_figS7B.R /scripts/martin_etal_figS7B.R
