FROM openmicroscopy/ome-files-jupyter:latest

USER root
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN pip3 install -r /requirements.txt

USER jupyter
ENV HOME /home/jupyter
COPY notebooks/*.ipynb ${HOME}/notebooks/
WORKDIR ${HOME}/notebooks
COPY data/ ${HOME}/notebooks/
RUN jupyter nbconvert --ExecutePreprocessor.kernel_name="python3" --to notebook --execute --stdout CMSO_PM.ipynb >/dev/null
