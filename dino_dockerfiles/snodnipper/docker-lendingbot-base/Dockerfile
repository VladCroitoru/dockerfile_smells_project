FROM python:2
RUN useradd -b /home -U -m jupyter && \
    python -m pip install \
        jupyter \
        matplotlib \
        pandas==0.20.3 \
        numpy \
        hypothesis \
        requests \
        pytz

EXPOSE 8888
WORKDIR /home/jupyter/notebooks
VOLUME /home/jupyter/notebooks
USER jupyter
HEALTHCHECK CMD ["curl", "-f", "http://localhost:8888/"]
CMD ["sh", "-c", "jupyter notebook --ip 0.0.0.0 --no-browser"]

