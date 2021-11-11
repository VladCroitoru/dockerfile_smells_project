FROM centos:7.9.2009
MAINTAINER Bruce Moran <bruce01campus@gmail.com>
LABEL software="tumortype-wgs" \
  container="tumortype-wgs" \
  about.summary="classify tumor using DNN on VCF" \
  about.home="https://github.com/brucemoran/TumorType-WGS" \
  software.version="0.0.1-deb" \
  version="1" \
  about.copyright="Apache License 2.0" \
  about.license="Apache License 2.0" \
  about.license_file="Apache License 2.0" \
  extra.binaries="none" \
  about.tags="biology::variants, field::biology, field::biology:bioinformatics,:dnn, role::program, use::analysing,:variants"
ENV CENTOS_FRONTEND noninteractive
COPY requirements.txt .
RUN yum install -y git python3 && yum -y clean all
RUN python3 -m pip install --upgrade pip
RUN pip3 install --user --no-warn-script-location -r requirements.txt && pip3 install --upgrade tensorflow && git clone https://github.com/brucemoran/TumorType-WGS && chmod a+x /TumorType-WGS/DNN-Model/predict_cancer.py && chmod a+x /TumorType-WGS/DNN-Model/vcf2input.py && rm -rf /root/.cache
ENV PATH="/root/.local/bin:/TumorType-WGS/DNN-Model/:${PATH}"
