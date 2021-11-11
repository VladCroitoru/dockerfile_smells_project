FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN apt-get update -y   
RUN apt-get install -y python3-pip python3-dev build-essential libgl1-mesa-dev tesseract-ocr-rus 

#libsqlite3-dev

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip3 install -r requirements.txt 

WORKDIR /usr/src/app

RUN mkdir /usr/src/app/output
RUN mkdir /usr/src/app/models

# COPY models/*.pkl /usr/src/app/models/

RUN gdown --id 1-172My1T8VvCSPCc4eHcJZXkZvuXlo9V -O models/type.pkl \
    && gdown --id 10scZJVWomVktMUdjd1QIlwxd1kXclmwT -O models/orient.pkl


COPY config.yaml /usr/src/app/models
COPY *.py /usr/src/app/


# ENTRYPOINT ["unicorn"]   
CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "9095", "--workers", "4"]