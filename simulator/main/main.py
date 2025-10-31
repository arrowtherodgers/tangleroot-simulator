from flask import Blueprint, render_template

import simulator.adapters.irepo as repo
import simulator.main.services as services

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/', methods=['GET'])
def main():
    plants = services.get_plants(repo.repo_instance)
    patches = services.get_patches(repo.repo_instance)
    farms = services.get_farms(repo.repo_instance)

    print(f"{len(farms)} Farms to use.")

    return render_template('main/main.html')