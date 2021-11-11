FROM python:3.7 as intermediate
COPY requirements.txt /
WORKDIR /pip-packages/
RUN pip download -r /requirements.txt
FROM python:3.7
WORKDIR /pip-packages/
COPY --from=intermediate /pip-packages/ /pip-packages/
RUN pip install --no-index --find-links=/pip-packages/ /pip-packages/*

RUN git clone https://github.com/arontommi/VCFlat.git
RUN python -m pip install -e VCFlat