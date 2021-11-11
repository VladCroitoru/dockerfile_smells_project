FROM ubuntu

EXPOSE 8001
ENV PYTHONUNBUFFERED 0

RUN useradd app

# Install packages from README
# see https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#apt-get
RUN apt-get -y update && \
    apt-get -y install python3 python3-pip librsvg2-bin ghostscript imagemagick unoconv libreoffice inkscape && \
    rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --no-cache --upgrade pip
RUN mkdir -p /app/printathpi/
WORKDIR /app/
COPY LICENSE /app/
COPY requirements.txt /app/
COPY start.sh /app/

RUN pip install --no-cache -r requirements.txt

RUN chown -R app /app
USER app
ENV HOME /app

COPY printathpi/ /app/printathpi/


ENTRYPOINT ["./start.sh"]
