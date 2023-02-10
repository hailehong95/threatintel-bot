#!/usr/bin/env python

from findomain.config import app
from findomain.schedule_task import schedule_start

if __name__ == "__main__":
    schedule_start()
    app.run()
