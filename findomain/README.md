## Findomain service

### findomain

- Get latest binaries: https://github.com/Findomain/Findomain
- Place them in the correct directory
- Docker MySQL
    ```bash
    $ docker run -d --name findomain -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<Your-Password> -e MYSQL_DATABASE=domain_monitor mysql:8.0.31
    ```
- Edit `.env`
- Create database

    ```bash
    $ python3
    >>> from findomain.build_db import build_db
    >>> build_db()
    >>>
    ```

- Verify in db:

  ```sql
  mysql> use domain_monitor;
  Database changed
  mysql> show tables;
  +--------------------------+
  | Tables_in_domain_monitor |
  +--------------------------+
  | domain                   |
  | subdomain                |
  +--------------------------+
  2 rows in set (0.00 sec)
  
  mysql> select * from domain;
  +----+----------------+---------------------+
  | id | domain         | timestamp           |
  +----+----------------+---------------------+
  |  1 | vccorp.vn      | 2022-12-04 15:15:21 |
  |  2 | bizflycloud.vn | 2022-12-04 15:15:21 |
  +----+----------------+---------------------+
  2 rows in set (0.00 sec)
  
  mysql> select * from subdomain;
  +----+-----------+-----------------------+---------------------+
  | id | domain_id | subdomain             | timestamp           |
  +----+-----------+-----------------------+---------------------+
  |  1 |         1 | salary.vccorp.vn      | 2022-12-04 15:15:21 |
  |  2 |         1 | bonus.vccorp.vn       | 2022-12-04 15:15:21 |
  |  3 |         2 | dichvu.bizflycloud.vn | 2022-12-04 15:15:21 |
  |  4 |         2 | gate.bizflycloud.vn   | 2022-12-04 15:15:21 |
  +----+-----------+-----------------------+---------------------+
  4 rows in set (0.00 sec)
  ```

- Docker build image
  ```bash
  $ docker build -t findomain .
  ```

- Updating..!