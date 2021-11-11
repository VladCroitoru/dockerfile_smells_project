FROM alpine
ADD https://github.com/efritz/derision/releases/download/0.3/derision /
ADD https://github.com/efritz/derision-smtp/releases/download/0.1/derision-smtp /
COPY entrypoint.sh .
RUN chmod +x derision
RUN chmod +x derision-smtp

FROM alpine
COPY config.json .
COPY --from=0 derision .
COPY --from=0 derision-smtp .
COPY --from=0 entrypoint.sh .
ENTRYPOINT []
CMD ["./entrypoint.sh"]
