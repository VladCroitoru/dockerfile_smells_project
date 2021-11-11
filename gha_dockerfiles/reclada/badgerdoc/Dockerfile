FROM python:3.8.10-buster

RUN apt-get install apt-transport-https && \
    echo "deb https://notesalexp.org/tesseract-ocr/buster/ buster main" >> /etc/apt/sources.list && \
    wget -O - https://notesalexp.org/debian/alexp_key.asc | apt-key add -

RUN apt-get update && \
    apt-get -f install --yes locales build-essential libpoppler-cpp-dev python3-dev \
    python3-distutils poppler-utils libpoppler-qt5-1 poppler-data libleptonica-dev \
    libtesseract-dev tesseract-ocr pkg-config cmake wget curl libreoffice software-properties-common \
    default-jre libreoffice-java-common vim && rm -rf /var/lib/apt/lists/*

RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo "LANG=en_US.UTF-8" > /etc/locale.conf && \
    locale-gen en_US.UTF-8

RUN pip install poetry

RUN mkdir mmcv && wget -P mmcv https://download.openmmlab.com/mmcv/dist/1.2.1/torch1.7.0/cpu/mmcv_full-1.2.1%2Btorch1.7.0%2Bcpu-cp38-cp38-manylinux1_x86_64.whl

COPY pyproject.toml /
COPY poetry.lock /

RUN poetry config virtualenvs.create false && \
    poetry add mmcv/mmcv_full-1.2.1+torch1.7.0+cpu-cp38-cp38-manylinux1_x86_64.whl \
    && poetry install --no-interaction \
    && rm -rf poetry.lock pyproject.toml poetry.lock mmcv/

RUN pip install 'git+https://github.com/open-mmlab/mmdetection.git@v2.7.0'

RUN python -m nltk.downloader stopwords && \
    python -m nltk.downloader words && \
    python -m nltk.downloader punkt && \
    python -m nltk.downloader wordnet

RUN mkdir /models && \
    gdown "https://drive.google.com/uc?id=1Nn0g0gIupW6xIpBZnwHRcyEDq9j6AtX2" -O /models/3_cls_w18_e30.pth

ENV CASCADE_MODEL_PATH="/models/3_cls_w18_e30.pth"

COPY . /table-extractor
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="${PYTHONPATH}:/table-extractor"

WORKDIR /table-extractor

CMD ["/bin/bash"]
