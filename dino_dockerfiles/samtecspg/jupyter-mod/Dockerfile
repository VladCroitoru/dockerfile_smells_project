FROM jupyter/minimal-notebook

ENV NB_USER jovyan

USER root
COPY jupyter_notebook_config.py /etc/jupyter/
RUN chown -R $NB_USER:users /etc/jupyter/

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_USER
