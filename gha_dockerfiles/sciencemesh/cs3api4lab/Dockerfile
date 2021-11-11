FROM jupyter/base-notebook:lab-3.0.15

COPY cs3api4lab /opt/cs3/cs3api4lab
COPY src /opt/cs3/src
COPY style /opt/cs3/style
COPY jupyter-config /opt/cs3/jupyter-config
COPY setup.py /opt/cs3/setup.py
COPY README.md /opt/cs3/README.md
COPY package.json /opt/cs3/package.json
COPY yarn.lock /opt/cs3/yarn.lock
COPY tsconfig.json /opt/cs3/tsconfig.json
COPY pyproject.toml /opt/cs3/pyproject.toml

USER root

RUN cd /opt/cs3 && \
	python -m pip install --upgrade pip && \
    pip install --no-cache-dir -e . && \
    jlpm && \
    jlpm build && \
    jupyter labextension install . && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/opt/cs3" && \
    fix-permissions "/home/${NB_USER}" && \
    jupyter lab clean -y && \
    npm cache clean --force && \
    jupyter server --generate-config -y && \
    jupyter lab --generate-config -y && \
    rm -rf "/home/${NB_USER}/.cache/yarn" && \
    rm -rf "/home/${NB_USER}/.node-gyp" && \
    sed -i -e '$ac.NotebookApp.contents_manager_class = \x27cs3api4lab.CS3APIsManager\x27' /etc/jupyter/jupyter_notebook_config.py

ENV JUPYTER_ENABLE_LAB = 1

EXPOSE 8888

USER $NB_UID

WORKDIR $HOME
