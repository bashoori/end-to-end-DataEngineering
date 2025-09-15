# docker/Dockerfile
FROM apache/airflow:2.9.3-python3.11

# --- OS deps: Microsoft ODBC Driver 18 + tools ---
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
      curl gnupg ca-certificates apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
      > /etc/apt/sources.list.d/microsoft-prod.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
      msodbcsql18 mssql-tools18 unixodbc-dev && \
    ln -s /opt/mssql-tools18/bin/sqlcmd /usr/local/bin/sqlcmd && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/mssql-tools18/bin:${PATH}"

# --- Python deps ---
USER airflow
COPY requirements.txt /requirements.txt
# Install your project deps + MSSQL provider + pyodbc
RUN pip install --no-cache-dir -r /requirements.txt \
    && pip install --no-cache-dir apache-airflow-providers-microsoft-mssql pyodbc

WORKDIR /opt/airflow
