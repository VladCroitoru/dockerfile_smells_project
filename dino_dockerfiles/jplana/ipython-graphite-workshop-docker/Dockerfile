FROM jupyter/scipy-notebook

MAINTAINER Jose Plana <jplana@gmail.com>
VOLUME /home/jovyan/work
EXPOSE 8888
RUN bash -c ". /opt/conda/envs/python2/bin/activate python2; pip install git+https://github.com/jplana/whisper.git@45cd927"
RUN bash -c ". /opt/conda/envs/python2/bin/activate python2; pip install git+https://github.com/htch/grafana_api_client.git"
CMD ["start-notebook.sh", "--NotebookApp.base_url='/ipython'", "--NotebookApp.allow_origin='*'"]
