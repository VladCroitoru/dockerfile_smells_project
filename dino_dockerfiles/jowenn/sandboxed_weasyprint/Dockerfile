FROM debian:buster-slim as base
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info file && useradd -d /sandboxed_weasyprint sandboxed_weasyprint
COPY requirements.txt /sandboxed_weasyprint/
WORKDIR /sandboxed_weasyprint
RUN pip3 install --no-cache-dir -r ./requirements.txt

FROM scratch as collected
COPY controllers /collected/controllers/
COPY models /collected/models/
COPY swagger /collected/swagger/
COPY encoder.py sandboxed_weasyprint.py util.py /collected/

FROM base
COPY --from=collected /collected /sandboxed_weasyprint
WORKDIR /sandboxed_weasyprint
USER sandboxed_weasyprint
CMD ["python3","./sandboxed_weasyprint.py"]
