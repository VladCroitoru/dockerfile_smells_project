from thomaschln/opticskxi

# Install plink 1.09
env PLINK       plink_linux_x86_64_20200428.zip
env PLINK_HOME          /usr/local
env PATH                $PLINK_HOME:$PATH
run wget http://s3.amazonaws.com/plink1-assets/$PLINK && \
    unzip $PLINK -d $PLINK_HOME && \
    rm $PLINK && \
    rm -rf /var/lib/apt/lists/*

# Install SHAPEIT
run wget -O shapeit.tgz https://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.v2.r904.glibcv2.17.linux.tar.gz \
  && tar -zxvf shapeit.tgz \
  && mv /shapeit.v2.904.3.10.0-693.11.6.el7.x86_64/bin/shapeit /bin/

# Install SNPClust 
run apt-get update && apt-get install -y libnetcdf-dev
run R -e "install.packages('BiocManager');BiocManager::install('GWASTools')"
run R -e "devtools::install_github('zhengxwen/SNPRelate')"

add ./ snpclust/
run R -e "devtools::install('snpclust', dependencies = TRUE)"
