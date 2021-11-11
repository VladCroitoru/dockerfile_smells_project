FROM andgineer/matplotlib

COPY requirements.txt /requirements.txt

RUN apk --no-cache --update add build-base cairo-dev cairo cairo-tools jpeg-dev zlib-dev \
                                        freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf ~/.pip/cache/ \
    && rm -rf /var/cache/apk/*

COPY src  /iot_calendar/
COPY tests /tests
COPY pytest.ini /
COPY conftest.py /
COPY test.sh /

EXPOSE 4444

WORKDIR /iot_calendar

CMD ["python3", "iot_calendar.py"]
