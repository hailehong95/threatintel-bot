from cve_monitor.config import app, db
from cve_monitor.models import AppMonitor, app_schema, apps_schema


# Lay ra tat ca cac app name trong db
def read_all_app():
    with app.app_context():
        apps = AppMonitor.query.all()
        if apps is not None:
            return apps_schema.dump(apps)
        else:
            return None


# Lấy ra một app name trong db
def read_one_app(app_id):
    with app.app_context():
        app_name = AppMonitor.query.get(app_id)
        if app_name is not None:
            return app_schema.dump(app_name)
        else:
            return None


# Tao moi mot app name
def create_one_app(data):
    # data = {"app_name": "Example"}
    with app.app_context():
        app_name = data.get("app_name")
        existing_app = AppMonitor.query.filter(AppMonitor.app_name == app_name).one_or_none()
        if existing_app is None:
            new_app = app_schema.load(data, session=db.session)
            db.session.add(new_app)
            db.session.commit()
            return True
        else:
            return False
