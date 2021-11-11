FROM continuumio/miniconda3

COPY . /app/impact_dashboard
COPY launch.sh /app/launch.sh

RUN  . /opt/conda/etc/profile.d/conda.sh &&\ 
    conda env create -f /app/impact_dashboard/environment.yml && \
    conda activate impact-dashboard && \
    pip install /app/impact_dashboard &&\
    chmod +x /app/launch.sh

ENV file_path /app/files

CMD /app/launch.sh