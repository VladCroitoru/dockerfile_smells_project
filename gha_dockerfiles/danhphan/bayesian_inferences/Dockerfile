
FROM pymc/pymc3:version-3.9.0

LABEL name="bayesian_ml"
LABEL version="1.0"
LABEL description="Environment for building Bayesian Neural Networks"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

COPY requirements.txt .

RUN pip3 install -r requirements.txt

#Setup File System
RUN mkdir /home/jovyan/workspace
ENV HOME=/home/jovyan/workspace
ENV SHELL=/bin/bash
WORKDIR /home/jovyan/workspace

# Start jupyter notebook
ENTRYPOINT ["jupyter", "notebook", "--allow-root", "--ip=0.0.0.0"]




