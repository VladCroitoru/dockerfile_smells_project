FROM python:2-alpine
# Following label schema convention described at http://label-schema.org/rc1/
LABEL \
    org.label-schema.schema-version="1.0" \
    org.label-schema.name="BingRewards" \
    org.label-schema.vcs-url="http://github.com/sealemar/BingRewards" \
    org.label-schema.description="BingRewards is an automated point earning script that works with Bing.com to earn points that can be redeemed for giftcards." \
    org.label-schema.docker.cmd="docker run -it --rm -v /path/to/config.xml:/usr/src/app/config.xml elisiano/bingrewards" \
    org.label-schema.docker.maintainer="Elisiano Petrini <elisiano@gmail.com>"

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN apk --no-cache add bash mailx \
  && pip install -r requirements.txt
CMD ["python", "main.py"]
