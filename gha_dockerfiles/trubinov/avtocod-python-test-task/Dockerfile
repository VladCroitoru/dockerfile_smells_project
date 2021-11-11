FROM python:3.9-slim AS nonrootimage
RUN useradd -u 8877 -m pynt
USER pynt
ENV PATH="/home/pynt/.local/bin:$PATH"

FROM nonrootimage
COPY ./requirements.txt ./requirements-dev.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt -r requirements-dev.txt
COPY spider.py .
CMD python
