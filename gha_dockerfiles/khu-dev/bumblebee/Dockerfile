FROM alpine
# DB를 쓰는 경우 Timezone 데이터가 필요한데 alpine에는 기본적으로 존재하지 않음
RUN apk add tzdata
WORKDIR /khumu
# build한 output binary를 삽입
COPY bumblebee /khumu/bumblebee
ENV KHUMU_HOME /khumu
ENV KHUMU_ENVIRONMENT DEV
CMD ["./bumblebee"]