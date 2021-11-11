FROM alpine:latest
MAINTAINER James Rasell <jamesrasell@gmail.com>

ADD /dashboard_duty /dashboard_duty

RUN apk --no-cache add \
    	ca-certificates \
    	python \
    	py-pip \
        && pip install Flask requests \
        && echo "Build complete."

CMD [ "/usr/bin/python", "/dashboard_duty/app.py" ]
