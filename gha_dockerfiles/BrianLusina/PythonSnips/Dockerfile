# FROM python:3
FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# add
ADD requirements.txt .

# Install app dependencies
RUN pip install -r requirements.txt

# Bundle app source
# COPY . /src/simpleapp.py

# EXPOSE  8000
# CMD ["py.test", "tests/"]

