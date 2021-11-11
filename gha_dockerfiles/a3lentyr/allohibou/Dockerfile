FROM python:3.9

RUN mkdir /app
COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

COPY pyx /app/pyx
COPY setup.py /app

RUN python setup.py build_ext --inplace

COPY main.py /app
COPY img /app/img
COPY missionDescriptor.json /app
COPY lib /app/lib

CMD python main.py