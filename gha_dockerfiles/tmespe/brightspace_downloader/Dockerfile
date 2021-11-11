FROM ubuntu:latest

EXPOSE 4444

RUN apt-get update -y
RUN apt-get install -y tzdata

ENV TZ Europe/Paris
ENV PATH="/root/.local/bin:${PATH}"


RUN apt-get install firefox python3 python3-pip python3-virtualenv python3-dev curl build-essential -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /app

ARG GECKODRIVER_NAME="geckodriver-v0.30.0-linux64"
ARG GECKODRIVER_EXTENSION="tar.gz"

WORKDIR "/app"

ADD https://github.com/mozilla/geckodriver/releases/download/v0.30.0/${GECKODRIVER_NAME}.${GECKODRIVER_EXTENSION} .

RUN tar -xvf ${GECKODRIVER_NAME}.${GECKODRIVER_EXTENSION} --directory=/usr/local/bin && rm ${GECKODRIVER_NAME}.${GECKODRIVER_EXTENSION}
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
RUN poetry install


ENTRYPOINT ["poetry", "run", "python3", "main.py"]