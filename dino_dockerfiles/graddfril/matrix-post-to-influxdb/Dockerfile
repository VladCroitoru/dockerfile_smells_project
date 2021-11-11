FROM python:3.5.2-alpine

# Follows conventions set by python:onbuild
WORKDIR /usr/src/app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./main.py" ]
