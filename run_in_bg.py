from app import app
from betting_utils import live_betting, register_open_bet
import time

total_seconds = 0

with app.app_context():
    while True:
        print(total_minutes)
        if total_seconds > 7200:
            register_open_bet()
            total_minutes = 0
        live_betting()
        total_seconds += 3
        time.sleep(3)

# latest process id: kmcron
# tmux attach-session -t kmcron
# tmux kill-session -t kmcron
# tmux ls
# tmux new -s kmcron
