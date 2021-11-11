FROM dart:2-sdk as build

WORKDIR /app

COPY . .

RUN dart pub get

CMD dart run /app/bin/uptodate.dart github -f $INPUT_CONFIG -r $INPUT_REPOSITORY -t $INPUT_TOKEN -v