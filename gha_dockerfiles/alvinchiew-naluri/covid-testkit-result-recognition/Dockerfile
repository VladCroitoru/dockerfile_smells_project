FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
LABEL maintainer="alvin.chiew@naluri.life"

COPY ./get_covid_result.py ./requirements.txt ./testkit_ext_service.py  /app/

WORKDIR /app


RUN \
    apt-get update && \
    apt-get install -y apt-transport-https && \
    apt install -y wget && \
    apt install -y gnupg && \
    echo "deb https://notesalexp.org/tesseract-ocr-dev/bullseye/ bullseye main" >> /etc/apt/sources.list && \
    wget -O - https://notesalexp.org/debian/alexp_key.asc | apt-key add - && \
    # apt-get update -oAcquire::AllowInsecureRepositories=true && \
    # apt-get install -y notesalexp-keyring && \
    # -oAcquire::AllowInsecureRepositories=true && \
    apt-get update && \
    # apt-get install -y software-properties-common && \
    # add-apt-repository ppa:alex-p/tesseract-ocr-devel && \
    # apt-get update && \

    # apt install -y tesseract-ocr-eng && \
    apt-get install -y tesseract-ocr && \
    # apt install -y libtesseract-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

CMD ["uvicorn", "testkit_ext_service:app", "--host", "0.0.0.0"]

EXPOSE 8000