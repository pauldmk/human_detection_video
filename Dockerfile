FROM python:3.7.6-buster

ARG APT_DEPS="libgl1-mesa-dev"

RUN mkdir app

COPY requirements.txt app/requirements.txt
COPY src app/src

WORKDIR app

RUN mkdir data
RUN mkdir output

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
           ${APT_DEPS} \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    &&  pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/video_detection.py"]