FROM jupyter/all-spark-notebook
MAINTAINER Yu-Hsin Lu <kerol2r20@gmail.com>

USER root

WORKDIR /


RUN rm -rf /home/* && \
    pip install pypandoc && \
    pip install oauthenticator

CMD ["jupyterhub"]