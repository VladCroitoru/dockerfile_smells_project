FROM python:3.8.5-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8 \
    TZ=Europe/Stockholm
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && \
    apt-get install --no-install-recommends -y libpq-dev=11.13-0+deb10u1 build-essential=12.6 && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /home/app
COPY requirements.txt ./ddpcr/ /home/app/
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "ddpcr.wsgi:application"]
