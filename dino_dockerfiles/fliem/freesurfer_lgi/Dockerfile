# see https://hub.docker.com/r/ninjaben/matlab-support/~/dockerfile/
FROM bids/freesurfer:v6.0.0-1

RUN apt-get update && apt-get install -y \
    libpng12-dev libfreetype6-dev \
    libblas-dev liblapack-dev gfortran build-essential xorg

ENV PATH="/usr/local/MATLAB/from-host/bin:${PATH}"
ENV MATLABPATH=/opt/freesurfer/matlab

RUN pip3 install ipython

RUN mkdir -p /code
COPY run.py /code/run.py
RUN chmod +x /code/run.py

#COPY version /version

ENTRYPOINT ["/code/run.py"]
