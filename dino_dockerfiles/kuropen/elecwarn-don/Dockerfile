FROM python:3.9-bullseye AS pip

RUN apt-get update && \
    apt-get -y install build-essential \
    gfortran \
    libatlas-base-dev \
    liblapack-dev
RUN mkdir -p /src
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt -t .

FROM public.ecr.aws/lambda/python:3.9
COPY --from=pip /src .
CMD ["app.handler"]

