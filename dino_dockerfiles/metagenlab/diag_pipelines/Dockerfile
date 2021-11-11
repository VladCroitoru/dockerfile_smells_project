# Base Image
FROM continuumio/miniconda3:4.7.10
 
################## METADATA ######################
 
LABEL base.image="biocontainers:latest"
LABEL version="1"
LABEL software="diag-pipelines-singularity"
LABEL software.version="1.0"
LABEL description="combined toolset analysis"
LABEL tags="Genomics"
 
################## MAINTAINER ######################
 
MAINTAINER Trestan Pillonel

################## INSTALLATION ######################

ENV main=/usr/local/bin/
ENV pipeline_folder=${main}/snakemake_pipeline
ENV NCBI_API_KEY=719f6e482d4cdfa315f8d525843c02659408
#RUN vdb-config -s /repository/user/main/public/root="/home/pipeline_user/ncbi/public"

ENV TZ Europe/Zurich

RUN echo $TZ > /etc/timezone && \
    apt-get update && apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

# install qualimap dependancies
RUN export DEBIAN_FRONTEND=noninteractive TERM=linux && \
  apt-get update && \
  apt-get -y --no-install-recommends install libfontconfig1 file procps libsm6 libxext6

# create data directory
RUN mkdir -p /data/references

# download reference into data directory
RUN wget -qO- https://gembox.cbcb.umd.edu/mash/refseq.genomes.k21s1000.msh > /data/references/mash_sketch.msh
RUN mkdir -p data/references/centrifuge_db/
RUN wget -qO- ftp://ftp.ccb.jhu.edu/pub/infphilo/centrifuge/data/p_compressed+h+v.tar.gz | tar xvz -C /data/references/centrifuge_db/
RUN conda config --add channels defaults && conda config --add channels conda-forge && conda config --add channels bioconda

# update conda
RUN conda install conda=4.7.12

# install snakemake
RUN conda install snakemake=5.7.0 unzip sra-tools=2.9.1 biopython=1.72

# setup pipeline
RUN git clone https://github.com/metagenlab/diag_pipelines --single-branch --branch dev $pipeline_folder && echo ok666
RUN mkdir -p /opt/conda/envs/
ENV conda_folder=/opt/conda/envs/

WORKDIR /data

# setup VFDB database
RUN snakemake --snakefile ${pipeline_folder}/rules/downloading/fetch_VFDB.rules --use-conda --conda-prefix ${conda_folder} references/virulence/VFDB_larger_50aa.faa.phr references/virulence/VFDB_annotations.tab -j 4

#CREATE cgMLST BED FILES
RUN snakemake --snakefile ${pipeline_folder}/workflows/core_genomes/make_ridom.rules --use-conda --conda-prefix ${conda_folder} core_genomes/cgMLST/Staphylococcus_aureus.bed core_genomes/cgMLST/Mycobacterium_tuberculosis.bed core_genomes/cgMLST/Listeria_monocytogenes.bed core_genomes/cgMLST/Klebsiella_pneumoniae.bed core_genomes/cgMLST/Enterococcus_faecium.bed core_genomes/cgMLST/Acinetobacter_baumannii.bed core_genomes/cgMLST/Legionella_pneumophila.bed core_genomes/cgMLST/Clostridioides_difficile.bed -j 4
RUN snakemake --snakefile ${pipeline_folder}/workflows/core_genomes/make_enterobase.rules --use-conda --conda-prefix ${conda_folder} core_genomes/cgMLST/Salmonella_enterica.bed core_genomes/cgMLST/Escherichia_coli.bed references/538048/genome_gbff.gbff -j 4
RUN snakemake --snakefile ${pipeline_folder}/rules/downloading/adapting_genome_files.rules --use-conda --conda-prefix ${conda_folder} references/538048/genome_gbwithparts.gbk

# CREATE MTB RESISTANCE DATABASES
#RUN mkdir -p resistance_db/Mycobacterium_tuberculosis/mutations/
#RUN mkdir -p resistance_db/Mycobacterium_tuberculosis/metadata/
#RUN cp ${pipeline_folder}/data/Mycobacterium_tuberculosis/mutations/* resistance_db/Mycobacterium_tuberculosis/mutations/
#RUN cp ${pipeline_folder}/data/Mycobacterium_tuberculosis/metadata/* resistance_db/Mycobacterium_tuberculosis/metadata/
#RUN snakemake --snakefile ${pipeline_folder}/workflows/check_resistance_databases.rules --use-conda --conda-prefix ${conda_folder} resistance_db/Mycobacterium_tuberculosis/mutations/currated_db_all/correct.bed resistance_db/Mycobacterium_tuberculosis/mutations/level_four_agreement/correct.bed resistance_db/Mycobacterium_tuberculosis/mutations/rgi_annotated_full_2_0_0/correct.bed resistance_db/Mycobacterium_tuberculosis/mutations/mykrobe_annotated/correct.bed resistance_db/Mycobacterium_tuberculosis/mutations/miotto_high_moderate_minimum_confidence_annotated/correct.bed resistance_db/Mycobacterium_tuberculosis/mutations/walker_resistant_annotated/correct.bed
#RUN cp ${pipeline_folder}/*.tsv . && cp ${pipeline_folder}/config.yaml .
#RUN mkdir -p core_genomes/parsnp/Mycobacterium_tuberculosis/
#RUN echo '' > links/Myco-10_S10_L001_R1.fastq.gz && echo '' > links/Myco-10_S10_L001_R2.fastq.gz && echo '' > core_genomes/parsnp/Mycobacterium_tuberculosis/parsnp.xmfa

# fake dataset
WORKDIR /tmp 
RUN mkdir links
RUN echo '' > links/Myco-10_S10_R1.fastq.gz
RUN echo '' > links/Myco-10_S10_R2.fastq.gz
#RUN echo '' > links/ERR2130394.fastq.gz
#RUN echo '' > links/SRR6936587.fastq.gz
RUN ln -s /data/references .
RUN ln -s /data/core_genomes .
RUN ln -s ${pipeline_folder}/config.yaml .
RUN ln -s ${pipeline_folder}/data/Staphylococcus_aureus/virulence_factors.tsv .
RUN ln -s ${pipeline_folder}/example_local_samples.tsv .
RUN ln -s ${pipeline_folder}/example_sra_samples.tsv .
# setup envs
#RUN snakemake --snakefile ${pipeline_folder}/workflows/full_pipeline.rules --use-conda --create-envs-only --conda-prefix ${conda_folder} --configfile config.yaml report/multiqc_assembly/multiqc_report.html samples/M10/resistance/mykrobe.tsv report/figures/freebayes_joint_genotyping/cgMLST/bwa/distances_in_snp_mst_no_st.svg report/figures/gatk_gvcfs/core_parsnp_538048/bwa/distances_in_snp_mst_no_st.svg report/figures/gatk_gvcfs/full_genome_M10_assembled_genome/bwa/distances_in_snp_mst_no_st.svg virulence_summary.xlsx report/typing/mlst/summary.xlsx report/resistance/rgi_summary.xlsx report/resistance/mykrobe_summary.xlsx report/figures/freebayes_joint_genotyping/cgMLST/bwa/phylogeny_no_st.svg report/figures/gatk_gvcfs/full_genome_538048/bwa/phylogeny_no_st.svg report/figures/gatk_gvcfs/core_parsnp_538048/bwa/phylogeny_no_st.svg report/contamination/mash/assembly/distances_formated.xlsx samples/SE1/contamination/centrifuge/report.tsv -j 4 --config species="Mycobacterium_tuberculosis" && conda clean --all --yes
RUN snakemake --configfile config.yaml --snakefile ${pipeline_folder}/workflows/full_pipeline.rules --use-conda --create-envs-only --conda-prefix ${conda_folder} epidemiology --config species="Mycobacterium_tuberculosis" && conda clean --all --yes
RUN snakemake --configfile config.yaml --snakefile ${pipeline_folder}/workflows/full_pipeline.rules --use-conda --create-envs-only --conda-prefix ${conda_folder} resistance --config species="Mycobacterium_tuberculosis" && conda clean --all --yes
RUN snakemake --configfile config.yaml --snakefile ${pipeline_folder}/workflows/full_pipeline.rules --use-conda --create-envs-only --conda-prefix ${conda_folder} virulence --config species="Mycobacterium_tuberculosis" && conda clean --all --yes
RUN snakemake --configfile config.yaml --snakefile ${pipeline_folder}/workflows/full_pipeline.rules --use-conda --create-envs-only --conda-prefix ${conda_folder} strain_characterization phylogeny/checkm/tree.nwk --config species="Mycobacterium_tuberculosis" && conda clean --all --yes
RUN patch /opt/conda/envs/951e3846/lib/python2.7/site-packages/mykatlas/typing/typer/presence.py < ${pipeline_folder}/patches/mykrobe.patch

RUN conda init bash
ENTRYPOINT ["/bin/bash"]

WORKDIR /diag_pipeline/

#RUN mkdir -p ${main}/data/references/1493941/
#RUN  /bin/bash -c 'source activate /opt/conda/envs/db3680fa/ && efetch -db assembly -id 1493941 -format docsum | xtract -pattern DocumentSummary -element FtpPath_RefSeq | sed "s/\(\/GCF_.*\)/\\1\\1_genomic.fna.gz/" | xargs -I % wget -qO- % | gzip -d > ${main}/data/references/1493941/genome_fna.fna'
#RUN  /bin/bash -c 'source activate /opt/conda/envs/c327f08f/ && mash sketch -o ${main}/data/references/mash_sketch_human.msh ${main}/data/references/1493941/genome_fna.fna'
#RUN rm -rf ${main}/data/references/1493941/
#RUN rm -rf links/ &&  rm core_genomes/parsnp/Mycobacterium_tuberculosis/parsnp.xmfa && rm config.yaml && rm *.tsv