FROM tiangolo/uvicorn-gunicorn:python3.8

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/* && \
    git clone https://github.com/Daniel-Fernandez-951/Nauclerus-API && \
    mv -v Nauclerus-API/app/* /app && \
    mv -v Nauclerus-API/requirements.txt /app && \
    mkdir /app/logo && \
    mv -v Nauclerus-API/images/logo2-nauclerusAPIV1_dark.png /app/logo/ && \
    pip install -r requirements.txt && \
    rm -rf Nauclerus-API
