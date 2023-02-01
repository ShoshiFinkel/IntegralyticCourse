ARG IMAGE_VARIANT=slim-buster
ARG OPENJDK_VERSION=19
ARG PYTHON_VERSION=3.10.9

FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT} AS py
FROM openjdk:${OPENJDK_VERSION}-${IMAGE_VARIANT}

COPY --from=py / /

ARG PYSPARK_VERSION=3.3.1

RUN pip --no-cache-dir install pyspark==${PYSPARK_VERSION}
RUN pip --no-cache-dir install pandas
RUN pip --no-cache-dir install ipykernel

ENTRYPOINT ["bash"]
