## Telegram bot service

### telegram bot

- Docker MySQL
    ```bash
    $ docker run -d --name telegram_bot -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<Your-Password> -e MYSQL_DATABASE=<Your-DB> mysql:8.0.31
    ```
- Edit `.env`
- Create database

  ```bash
  $ python3
  >>> from telegram_bot.build_db import build_db
  >>> build_db()
  >>>
  ```

- Verify in db:

- Docker build image
  ```bash
  $ docker build -t telegram_bot .
  ```

- Updating..!