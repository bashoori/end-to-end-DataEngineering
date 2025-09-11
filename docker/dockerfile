# Extend an official Airflow image
FROM apache/airflow:2.9.3-python3.11

# (Optional) Install OS deps you need
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential && rm -rf /var/lib/apt/lists/*

# Copy and install Python requirements (if present at project root)
COPY requirements.txt /requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r /requirements.txt || true

# Default workdir
WORKDIR /opt/airflow
