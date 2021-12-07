import json
from pathlib import Path

songs_path = Path(__file__).parent / "songs.json"

class DataLoader:
    def load(self):
        with open(songs_path, 'r') as f:
            return json.loads(f.read())
