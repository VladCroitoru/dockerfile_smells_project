FROM continuumio/miniconda
LABEL maintainer="stephen.gaffney _at_ yale.edu"

COPY environment.abstract.yaml /tmp/environment.yaml
RUN conda env create -n journals -f /tmp/environment.yaml \
    && conda clean -afy \
    && find /opt/conda/ -follow -type f -name '*.a' -delete \
    && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
    && find /opt/conda/ -follow -type f -name '*.js.map' -delete \
    && echo "source activate journals" > ~/.bashrc

ENV PATH=/opt/conda/envs/journals/bin:$PATH

WORKDIR /app
COPY src ./src

# gunicorn only works on mac/unix/linux
#ENTRYPOINT ["gunicorn", "--worker-tmp-dir", "/dev/shm", "--log-file=-", \
#            "journal_targeter.journals:app", "--workers=2", "--threads=4", \
#            "--worker-class=gthread"]
#CMD ["--bind=0.0.0.0:5000"]
ENV FLASK_APP=./src/journal_targeter/journals.py FLASK_ENV=development \
    FLASK_CONFIG=development PYTHONPATH=/app/src
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
