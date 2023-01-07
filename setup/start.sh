tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 api.v1.app:app'
tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 front_end.index:app'
