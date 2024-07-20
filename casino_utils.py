import datetime
import time
import json
import hashlib

import requests

BASE_URL = "https://fungamess.games/api/v2/kadromilyon"
API_KEY = "e42792aced9806cf74e03a4523949e0f"


def get_providers():
    r = requests.get(f"{BASE_URL}/providersList")
    return r.json()


def get_games(provider_id=None, game_type=None):
    if provider_id:
        r = requests.get(f"{BASE_URL}/gameList?provider={provider_id}")
    elif game_type:
        r = requests.get(f"{BASE_URL}/gameList?type={game_type}")
    else:
        r = requests.get(f"{BASE_URL}/gameList")
    return r.json()


def get_game_iframe(game_id, user_id, user_uuid, demo="true", bonus=None):
    demo = "true"
    # PROD WARNING: Remove this override in production websites
    if bonus:
        return f"{BASE_URL}/start?demo={demo}&gameId={game_id}&country=TR&userId={user_id}&token={user_uuid}&lang=tr&bonusName={bonus.bonus.bonus_name}&bonusRounds={bonus.bonus_amount}&bonusBet={bonus.bonus.round_value}&bonusExpired={int(time.time())+3600}"
    else:
        return f"{BASE_URL}/start?demo={demo}&gameId={ game_id }&country=TR&userId={user_id}&token={ user_uuid }&lang=tr"


def check_sign(request):
    hash_authorization_key = 'e42792aced9806cf74e03a4523949e0f'  # Key from back office

    hash_auth = request.headers.get('Hash-Authorization', '')  # Get hash from request or specify empty

    if request.method == 'POST':
        data = request.form.to_dict()
    else:
        data = request.args.to_dict()

    if 'extraData' in data:
        del data['extraData']

    sorted_data = {k: str(v) for k, v in sorted(data.items())}
    data_json = json.dumps(sorted_data)

    hash_auth_local = hashlib.sha256((data_json + hash_authorization_key).encode()).hexdigest()  # Hashing of data

    # Compare the collected hash and the one received from NUXGAME
    # Description returned: {true - Return an error!}, {false - Skip the request.}
    return hash_auth_local != hash_auth

