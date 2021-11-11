FROM python:3.8-alpine

WORKDIR /app

# Copy repo contents
COPY setup.py README.md requirements*.txt ./
COPY optimade_gateway ./optimade_gateway
COPY .ci ./.ci
RUN pip install -e .

EXPOSE 80

ARG CONFIG_FILE=optimade_config/config.json
COPY ${CONFIG_FILE} ./config.json
ENV OPTIMADE_CONFIG_FILE /app/config.json

CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "80", "optimade_gateway.main:APP" ]
