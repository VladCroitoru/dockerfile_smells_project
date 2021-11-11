FROM python:3.8-slim
RUN pip install --no-cache-dir aiohttp
RUN pip install --no-cache-dir click
ENTRYPOINT [ "python", "-u", "/app.py" ]
CMD ["web-app"]
COPY app.py /app.py
