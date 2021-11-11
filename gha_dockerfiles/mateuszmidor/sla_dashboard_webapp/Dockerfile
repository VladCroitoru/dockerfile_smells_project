# syntax=docker/dockerfile:1
FROM python:3.9-slim

# install GCC, that is needed by `pip install` on ARM64
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential=12.6 && \
    rm -rf /var/lib/apt/lists/*

# setup non-root user
ARG USER=sla-dashboard-user
RUN useradd --create-home ${USER}
USER ${USER}
ENV PATH=/home/${USER}/.local/bin:$PATH

# install SLA dashboard app
WORKDIR /app
COPY domain domain
COPY infrastructure infrastructure
COPY presentation presentation
COPY generated generated
COPY main.py .
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# configure default command for the image
CMD ["gunicorn", "--config=data/gunicorn.conf.py", "main:run()"]
