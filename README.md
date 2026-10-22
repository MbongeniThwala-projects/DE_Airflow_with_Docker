Setting up Apache Airflow with Docker

We will use are service account credentials (A JSON file) to pass our credentials, these credentials.json can be downloaded from GCP under IAM & Admin > service Accounts then you can add keys. 
Idealy we want our Docker desktop to have 8GB of RAM available (this can be changed under Setting > Resources)

We will download the docker-compose YAML file for the lastest airflow version **curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml'**  in a subdir and create a new .env in the same dir to setup Airflow User. In .env file, we'll have AIRFLOW_UID=5000 or use the following command in the cli **echo -e "AIRFLOW_UID=$(id -u)" > .env**

Because we are starting with a blank setup we will create our dags logs and plugins folders (mkdir -p ./dags ./logs ./plugins), *WHY DO WE NEED THESE FOLDERS?*

DAGS= This is where we will store our airflow pipeline with is called DAGS
LOGS= Stores the log information/communication between the schedula and the workers
PLUGINS= are for any customer plugins or header functions or utilities that we might need to use within our DAGS

We will need a requirements.txt to install dependencies- apache-airflow-providers-google(so airflow can use GCP SDK) and pyarrow (which is used for the conversion of data into Apache Parquet(columnar file formats))

changed AIRFLOW__CORE__LOAD_EXAMPLES inside the docker-compose.yaml and set it to false => this will prevent airflow from populating its interface with DAG examples.
AIRFLOW_CONN_GOOGLE_CLOUD-DEFUALT
GOOGLE_APPLICATION_CREDENTIALS

Execution
1. Build the image. This can take several minutes, and needs to be done only once, the first time you run Airflow or if you modify hte Dockerfile or the requirements file. 
    => docker compose build
2. Init configs
    => docker compose up airflow-init
3. Run Airflow
    => docker compose up -d

Note: The YAML file uses *CeleryExecutor* as its executor type, this means that tasks will be pushed to workers (external Docker containers) rather than running them locally (as regular processes). This can be changed by modifying the `AIRFLOW__CORE__EXECUTOR` enviroment variable under the `x-airflow-common` envirmoment defination.