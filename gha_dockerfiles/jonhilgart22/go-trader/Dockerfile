FROM lambci/lambda:build-python3.8

# make directories / folders
RUN mkdir app app/utils app/ftx app/mlcode app/awsUtils app/src app/structs

## PYTHON
# COPY poetry env over
COPY poetry.lock pyproject.toml ./

# Poetry install
RUN  pip install poetry
RUN set -x \
    && pip install --no-cache-dir --upgrade pip \
    && pip install wheel  \
    && poetry export --without-hashes -f requirements.txt -o requirements.txt \
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

## GOLANG
RUN yum -y install go
RUN echo $(ls)
ENV PATH="/usr/local/go/bin:${PATH}"

COPY go.mod go.sum ./
ENV GO111MODULE=on

RUN  go mod download

# Copy files over
ADD app app


RUN cd app/src && go build -o go-trader .

ENTRYPOINT  ["app/src/go-trader"]
