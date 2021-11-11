# vim:set ft=dockerfile:
FROM continuumio/miniconda3
MAINTAINER https://github.com/cp4cds/copernicus
LABEL Description="CP4CDS WPS Demo" Vendor="CP4CDS" Version="0.4.0"

# Update Debian system
RUN apt-get update && apt-get install -y \
 build-essential \
&& rm -rf /var/lib/apt/lists/*

# Update conda
RUN conda update -n base conda

# Copy WPS project
COPY . /opt/wps

WORKDIR /opt/wps

# Create conda environment
RUN conda env create -n wps -f environment.yml

# Install WPS
RUN ["/bin/bash", "-c", "source activate wps && python setup.py develop"]

# Start WPS service on port 5000 on 0.0.0.0
EXPOSE 5000
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["source activate wps && exec copernicus start -b 0.0.0.0 -c /opt/wps/etc/demo.cfg"]

# docker build -t cp4cds/copernicus .
# docker run -p 5000:5000 cp4cds/copernicus
# http://localhost:5000/wps?request=GetCapabilities&service=WPS
# http://localhost:5000/wps?request=DescribeProcess&service=WPS&identifier=all&version=1.0.0
