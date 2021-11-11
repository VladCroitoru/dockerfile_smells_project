FROM python:3.8.5

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app/khaja_khaja
COPY requirements.txt /usr/src/app/khaja_khaja
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /usr/src/app/khaja_khaja
RUN chmod +x /usr/src/app/khaja_khaja/seeder.sh