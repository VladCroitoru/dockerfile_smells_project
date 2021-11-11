FROM python:3.9-alpine

RUN apk update && apk add git gcc geos-dev proj-util proj-dev musl-dev

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "--host", "0.0.0.0", "--workers", "4", "vt_merge_proxy.server:app"]
