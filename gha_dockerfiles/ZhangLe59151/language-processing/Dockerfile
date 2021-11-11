FROM huggingface/transformers-tensorflow-gpu
WORKDIR /usr/src/app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["main.py"]
ENTRYPOINT ["python3"]