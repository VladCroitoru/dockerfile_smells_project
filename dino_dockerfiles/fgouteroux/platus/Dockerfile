FROM python:2.7
MAINTAINER François Gouteroux <francois.gouteroux@gmail.com>

RUN useradd --user-group --create-home --shell /bin/false platus

ENV INSTALL_PATH /platus
RUN mkdir -p $INSTALL_PATH && chown -R platus:platus /platus

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

USER platus

COPY app.py app.py
COPY platus platus

VOLUME data

CMD gunicorn -c "platus/config/gunicorn.py" app:application --reload
