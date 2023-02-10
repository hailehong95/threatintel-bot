#!/usr/bin/env python

from subfinder.config import app
from subfinder.schedule_task import schedule_start

if __name__ == "__main__":
    schedule_start()
    app.run()
