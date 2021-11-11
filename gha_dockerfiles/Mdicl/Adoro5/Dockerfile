FROM paperspace/first-order-model:0.1.0
ADD . ./

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV AUDIO=/app/la-donna-e-mobile.mp3
ENV DRIVING=/app/3516_wsound.mpeg
ENV WATERMARK=/app/watermark.png

CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
