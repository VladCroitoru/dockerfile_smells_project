FROM nginx:1.11.3-alpine
ADD /entrypoint.sh /
HEALTHCHECK --interval=5s --timeout=3s --retries=2 CMD wget -qO- localhost
CMD ["/entrypoint.sh"]
