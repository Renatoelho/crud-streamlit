FROM python:3.12-slim

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY ./src /app

RUN pip install -U \
    pip \
    setuptools \
    wheel \
    streamlit==1.41.1 \
    pandas==2.2.3 \
    --no-cache-dir

ENTRYPOINT streamlit run app.py --server.port 8501