# Regent kernel for Jupyter

FROM stanfordlegion/regent

MAINTAINER Elliott Slaughter <slaughter@cs.stanford.edu>

# Install Dependencies.
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y python3-pip wget && \
    apt-get clean
RUN pip3 install notebook

# Install Tini.
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.6.0/tini && \
    echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini" | sha256sum -c - && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

# Regent kernel configuration files.
RUN mkdir /usr/local/lib/python3.4/dist-packages/notebook/static/components/codemirror/mode/regent
COPY codemirror/regent/regent.js /usr/local/lib/python3.4/dist-packages/notebook/static/components/codemirror/mode/regent/
COPY pygments/lexers/regent.py /usr/local/lib/python3.4/dist-packages/pygments/lexers/
RUN cd /usr/local/lib/python3.4/dist-packages/pygments/lexers && python3 _mapping.py

RUN mkdir -p /usr/local/share/jupyter/kernels/regent
COPY kernels/regent/kernel_plain.json /usr/local/share/jupyter/kernels/regent/kernel.json
COPY kernels/regent/regentkernel.py /usr/local/share/jupyter/kernels/regent/regentkernel.py

ENV NB_USER=jovyan NB_UID=1001
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir /home/$NB_USER/notebooks && \
    mkdir /home/$NB_USER/.jupyter && \
    mkdir /home/$NB_USER/.jupyter/custom && \
    chown -R $NB_USER:users /home/$NB_USER

# Configure container startup.
EXPOSE 8888
WORKDIR /home/$NB_USER/notebooks
ENTRYPOINT ["tini", "--"]
CMD ["start-notebook.sh"]

# Configure local files last.
COPY start-notebook.sh /usr/local/bin/
COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/
COPY static/custom/custom.js /home/$NB_USER/.jupyter/custom/
COPY notebooks/ /home/$NB_USER/notebooks/
RUN chown -R $NB_USER:users /home/$NB_USER
