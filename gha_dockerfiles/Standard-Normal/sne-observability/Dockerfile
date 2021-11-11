FROM python:3.7

WORKDIR /app

ENV PYTHONUNBUFFERED True

ADD main.py /
COPY sn-tools sn-tools

# Install Chrome

# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
#     curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
#     apt-get update && \
#     ACCEPT_EULA=Y apt-get install msodbcsql17 unixodbc-dev git -y

# Install Python dependencies.
COPY FRONTOFFICE-4a9964373eb2.json FRONTOFFICE-4a9964373eb2.json
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install zeep[xmlsec]

COPY . /app
ENV PORT 8080

CMD [ "python", "-u", "main.py"]
