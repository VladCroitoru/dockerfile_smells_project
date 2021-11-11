FROM continuumio/miniconda:4.0.5p0

RUN conda install mpi4py numpy cython scipy matplotlib h5py setuptools colorama

COPY spyking-circus-0.3.tar.gz /tmp/spyking-circus-0.3.tar.gz
RUN pip install /tmp/spyking-circus-0.3.tar.gz
RUN pip install click

COPY spyking /
RUN chmod 777 /spyking

COPY probes/ /probes

RUN mkdir ~/spyking-circus

ENV DOCKER=True

CMD /spyking