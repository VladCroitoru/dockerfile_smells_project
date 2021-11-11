FROM hdfgroup/h5py:2.7.0

COPY requirements.txt /application/
WORKDIR /application
RUN pip install pip==20.3.4
RUN pip install -r requirements.txt --ignore-installed six

COPY setup.py .
COPY config config
COPY sumstats sumstats

RUN pip install . --ignore-installed six
RUN mkdir logs

# Expose ports
EXPOSE 8000

ENV SS_CONFIG "/application/config/properties.json"
ENV GACC_LOGS "logs/gaccess.log"
ENV GERR_LOGS "logs/gerror.log"
ENV GUNI_LOGS "logs/glogger.log"

ENV USER docker

ENV UID 1000
ENV GID 1000

RUN addgroup --gid "$GID" "$USER" \
  && adduser \
  --disabled-password \
  --gecos "" \
  --home "$(pwd)" \
  --ingroup "$USER" \
  --no-create-home \
  --uid "$UID" \
  "$USER"
