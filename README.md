# end-to-end-DataEngineering

end-to-end-dataengineering/
│── Airflow/
│   ├── dags/
│   ├── plugins/
│   └── logs/            # keep in .gitignore
│── docker/
│   ├── docker-compose.yml
│   └── Dockerfile
│── requirements.txt
│── README.md
│── .gitignore

How to run Airflow

From the project root:

# 1) Create folders if missing
mkdir -p Airflow/{dags,plugins,logs}

# 2) Initialize the Airflow DB and admin user
docker compose -f docker/docker-compose.yml up airflow-init

# 3) Start services (detached)
docker compose -f docker/docker-compose.yml up -d