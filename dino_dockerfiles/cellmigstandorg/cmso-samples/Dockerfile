FROM openmicroscopy/ome-files-jupyter:latest

USER root
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN pip3 install -r /requirements.txt

USER jupyter
ENV HOME /home/jupyter
COPY overlay.ipynb ${HOME}/notebooks
WORKDIR ${HOME}/notebooks
COPY UGent/BaF3 ${HOME}/notebooks/UGent/BaF3
RUN jupyter nbconvert --ExecutePreprocessor.kernel_name="python3" --to notebook --execute --stdout overlay.ipynb >/dev/null
