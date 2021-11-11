FROM jupyter/base-notebook:hub-1.4.2

ARG USER="prmluser"
ARG UID="1001"
# same gid as jovyan 
ARG GID="100"

USER root
RUN useradd ${USER} -u ${UID} -g ${GID} && \
    mkdir -p /home/${USER} && \ 
    chown "${USER}:${GID}" "/home/${USER}/"

USER ${USER}
ENV HOME="/home/${USER}/" \ 
    PYTHONPATH="$PYTHONPATH:/home/${USER}/PRML"

WORKDIR ${HOME}
RUN mkdir PRML && \ 
    fix-permissions ${HOME}

COPY --chown=${USER}:${GID} . PRML/
RUN pip install -r /home/${USER}/PRML/requirements.txt && \
    chmod 755 PRML/setup.sh
# ENTRYPOINT ["PRML/setup.sh"]