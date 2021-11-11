FROM continuumio/miniconda3:4.9.2-alpine
LABEL maintainer c.sachs@fz-juelich.de

USER root

ENV PATH "$PATH:/opt/conda/bin:/bin/sbin:/usr/bin"

COPY . /tmp/package


RUN \
    wget https://github.com/modsim/mycelyso-inspector/archive/main.tar.gz -O - | tar zx -C /tmp && \
    # conda build needs bash
    apk add --no-cache bash git && \
    conda install -c conda-forge conda-build conda-verify && \
    conda build -c conda-forge -c modsim /tmp/mycelyso-inspector-main/recipe && \
    conda build -c conda-forge -c modsim /tmp/package/recipe && \
    conda install -c conda-forge -c modsim -c local -y python==3.7 jupyter mycelyso mycelyso-inspector && \
    mv /tmp/package/examples / && \
    rm -rf /tmp/package && \
    busybox adduser --disabled-password user && \
    ln -s /examples /home/user && \
    mkdir /data && \
    chown -R user:users /data /examples /home/user && \
    su -s /bin/sh user -c "jupyter notebook --generate-config" && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> /home/user/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.notebook_dir = '/home/user'" >> /home/user/.jupyter/jupyter_notebook_config.py && \
    conda clean -afy || true && \
    # conda build purge-all && \ # keep the package in the Docker image
    echo Done

USER user

WORKDIR /data

EXPOSE 8888

ENTRYPOINT ["python", "-m", "mycelyso"]