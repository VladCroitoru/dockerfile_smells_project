FROM python:3.7.11-stretch

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    curl \
    lsb-release

RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN lsb_release -a
RUN exit
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./requirements-dev.txt .
RUN pip install -r requirements-dev.txt

COPY . .

CMD python application.py run -h 0.0.0.0