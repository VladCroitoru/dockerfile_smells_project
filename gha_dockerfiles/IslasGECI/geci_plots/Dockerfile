FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    mutmut \
    pylint \
    pytest \
    pytest-cov \
    pytest-mpl
