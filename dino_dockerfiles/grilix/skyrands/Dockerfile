from ruby:2

ADD . /app
ENV PORT=3000
ENV RACK_ENVIRONMENT=production
ENV HOST=0.0.0.0
EXPOSE 3000

WORKDIR /app
RUN ["gem", "install", "dep", "shotgun"]
RUN ["dep", "install"]
CMD ["shotgun"]
