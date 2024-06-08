from app import app
from betting_utils import live_betting, register_open_bet
import time

total_seconds = 0

with app.app_context():
    while True:
        if total_seconds > 7200:
            register_open_bet()
            total_seconds = 0
        live_betting()
        total_seconds += 60
        time.sleep(60)

# latest process id: kmcron
# tmux attach-session -t kmcron
# tmux kill-session -t kmcron
# tmux ls
# tmux new -s kmcron
