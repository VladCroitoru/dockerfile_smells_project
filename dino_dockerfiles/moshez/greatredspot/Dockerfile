FROM moshez/myubuntu:2017-04-23T16-39-22-608035

COPY jupyter.requirements.txt ncolony.requirements.txt remotemath.requirements.txt /

RUN python3.6 -m venv /jupyter && \
    python -m virtualenv /ncolony  &&\
    python3.6 -m venv /remotemath && \
    /jupyter/bin/pip install --upgrade pip wheel && \
    /jupyter/bin/pip install -r /jupyter.requirements.txt && \
    /ncolony/bin/pip install --upgrade pip wheel && \
    /ncolony/bin/pip install -r /ncolony.requirements.txt && \
    /remotemath/bin/pip install --upgrade pip wheel && \
    /remotemath/bin/pip install -r /remotemath.requirements.txt && \
    mkdir -p /var/run/ncolony/messages /var/run/ncolony/config /root/.jupyter

COPY jupyter.json remotemath.json /var/run/ncolony/config/

COPY slash_root_jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

ENTRYPOINT ["/ncolony/bin/twist", "ncolony", "--messages", "/var/run/ncolony/messages", "--config", "/var/run/ncolony/config"]
