from pathlib import Path
from flask import Flask

import simulator.adapters.irepo as repo
from simulator.adapters.memory_repo import MemoryRepo
from simulator.adapters.populate import populate


def create_app():

    app = Flask(__name__)
    data_path = Path('simulator') / 'adapters' / 'data'

    repo.repo_instance = MemoryRepo()
    populate(data_path, repo.repo_instance)

    with app.app_context():
        from .main import main
        app.register_blueprint(main.main_bp)

    return app