from app import run_pending_jobs, app
from betting_utils import live_betting, register_open_bet
import time

total_minutes = 0

with app.app_context():
    while True:
        try:
            print(total_minutes)
            if total_minutes == 120:
                register_open_bet()
                total_minutes = 0
            live_betting()
            total_minutes += 1
            time.sleep(60)
        except:
            pass

# latest process id: kmcron
# tmux attach-session -t
# tmux ls
# tmux new -s kmcron
