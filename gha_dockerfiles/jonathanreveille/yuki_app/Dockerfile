FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN apt-get --yes update && \
    apt-get --yes upgrade && \
    apt-get --yes install \
      postgresql-client \
      libxmlsec1-dev \
      netcat \
    && apt-get --yes clean

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src /usr/src/app

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
