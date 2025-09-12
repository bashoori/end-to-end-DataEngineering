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



docker-compose restart



1) Is the stack up and healthy?
docker compose -f docker/docker-compose.yml ps
docker compose -f docker/docker-compose.yml logs -n 100 webserver
docker compose -f docker/docker-compose.yml logs -n 100 scheduler
docker compose -f docker/docker-compose.yml logs -n 100 postgres


If webserver is restarting/crashed, the last ~20 lines of its logs will tell us why (common causes below).

2) Did you initialize the DB?

If you skipped init, the webserver dies with DB/migration errors.

docker compose -f docker/docker-compose.yml down
docker compose -f docker/docker-compose.yml up airflow-init
docker compose -f docker/docker-compose.yml up -d

3) Make sure port 8080 is actually exposed

Your compose file must have ports: - "8080:8080" on the webserver.

In Codespaces, open the Ports panel → ensure 8080 shows up, and set Visibility → Public.

Inside the Codespace shell, confirm it’s reachable:

curl -I http://localhost:8080


You should get HTTP/1.1 200 OK (or a 302).