FROM python:2.7
RUN apt-get update && apt-get install --yes --force-yes gfortran libopenblas-dev liblapack-dev
RUN pip install numpy scipy scikit-learn redis beautifulsoup4 urlnorm chardet boto3 nltk coverage mock attrdict dill selenium

COPY . /app

WORKDIR /app

