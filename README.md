# ADIF Importer

This Python project allows you to import **ADIF** (Amateur Data Interchange Format) log files into various databases, including **MariaDB**, **PostgreSQL**, **Oracle**, and **MSSQL**. The database type is specified in a `config.yaml` file, and the ADIF file is parsed and imported into the corresponding database.

---

## Features

- **Parses ADIF log files** and converts them into structured data.
- **Supports multiple databases**: MariaDB, PostgreSQL, Oracle, MSSQL.
- **Database configuration is externalized** in a `config.yaml` file.
- **Flexible and extensible**: easily add new database backends by modifying the factory.

---

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

---

## Installation

1. Clone this repository:

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

The database connection details are stored in the `config.yaml` file. This file is used to specify which database backend to use and to provide the necessary connection details.

### Example `config.yaml`

```yaml
database:
  type: "postgres"  # Options: mariadb, oracle, postgres, mssql

  mariadb:
    host: "localhost"
    port: 3306
    user: "user"
    password: "password"
    database: "adif_logs"

  oracle:
    host: "localhost"
    port: 1521
    user: "user"
    password: "password"
    service_name: "orcl"

  postgres:
    host: "localhost"
    port: 5432
    user: "user"
    password: "password"
    database: "adif_logs"

  mssql:
    host: "localhost"
    port: 1433
    user: "user"
    password: "password"
    database: "adif_logs"
```

### How to modify the configuration:

- Set `database.type` to the desired database type (`mariadb`, `oracle`, `postgres`, or `mssql`).
- Fill in the appropriate connection details for the selected database type (host, user, password, etc.).

---

## Usage

1. **Prepare your ADIF file**: Ensure your ADIF log file is available. Example file name: `log.adif`.

2. **Run the Importer**: Execute the following command to parse the ADIF file and import it into the database:

   ```bash
   python main.py <path_to_adif_file>
   ```

   Example:

   ```bash
   python main.py logs/log.adif
   ```

3. **Verify the Data**: After the script finishes, the data from the ADIF file will be imported into the configured database.

---

## Example Command Output

```bash
$ python main.py logs/log.adif
Imported 120 QSOs successfully.
```

---

## Adding a New Database Backend

To add a new database backend:

1. Create a new class that implements the `DatabaseInterface` in the `db/` folder.
2. Update `DatabaseFactory` to include your new class.
3. Ensure that `config.yaml` is updated with the correct database configuration.

---

## Dependencies

The following Python packages are required to run the project:

- `pyyaml` - For reading the `config.yaml` file.
- `adif` - For parsing ADIF files.
- `pymysql` - MariaDB driver.
- `psycopg2` - PostgreSQL driver.
- `cx_Oracle` - Oracle driver.
- `pyodbc` - MSSQL driver.

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License - see the [LICENCE](LICENCE) file for details.

---
