FROM waggle/plugin-base:1.1.1-base
LABEL version="0.2.7" \
      description="Periodical/Trigger-based Image sampler"

# COPY app.py /app/
COPY app.py requirements.txt /app/
RUN pip3 install --no-cache-dir -U -r /app/requirements.txt

ENTRYPOINT ["python3", "-u", "/app/app.py"]
