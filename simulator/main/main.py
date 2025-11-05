from flask import Blueprint, render_template

import simulator.adapters.irepo as repo

from simulator.main.simulation import Simulation

from collections import Counter
from random import choice

main_bp = Blueprint('main_bp', __name__)

FARM_CHECKS_PER_DAY = 10
ACTIVE_HOURS = 10
MAX_DAYS_TO_RUN = 1000

SIMULATIONS_TO_RUN = 1000

@main_bp.route('/', methods=['GET'])
def main():
    tangleroot_forms = ["normal", "crystal", "dragonfruit", "guam", "lily", "redwood"]
    tangleroot_image = f"tangleroot_{choice(tangleroot_forms)}.png"

    successful_runs = len(s_outs)
    total_harvests = dict(sum((s_out.count_harvests() for s_out in s_outs), Counter()))
    average_days_elapsed = round(sum((s_out.days_elapsed for s_out in s_outs)) / len(s_outs), 2)

    return render_template('main/main.html',
                        image=tangleroot_image,
                        simulations_run=SIMULATIONS_TO_RUN,
                        successful_runs=successful_runs,
                        harvests=total_harvests,
                        average_days_elapsed=average_days_elapsed,
                        fastest_pet=s_outs[0].result()
                    )

@main_bp.route('/simulate', methods=['GET'])
def simulate():
    simulations = [Simulation(repo.repo_instance, FARM_CHECKS_PER_DAY, ACTIVE_HOURS, MAX_DAYS_TO_RUN) for _ in
                   range(SIMULATIONS_TO_RUN)]
    s_outs = list()

    for s in simulations:
        s.initialize()
        s_out = s.run()
        if s_out.pet_obtained:
            s_outs.append(s_out)

    s_outs.sort(key=lambda s: s.days_elapsed)

