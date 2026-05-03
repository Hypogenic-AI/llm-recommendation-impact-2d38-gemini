import pandas as pd
import json
import os

def load_jsonl(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data

def preprocess():
    print("Loading datasets...")
    history_data = load_jsonl('datasets/listening_history_sample.jsonl')
    tracks_data = load_jsonl('datasets/spotify_tracks_sample.jsonl')
    
    # Create track mapping
    print("Creating track mapping...")
    track_df = pd.DataFrame(tracks_data)
    # Some tracks might be missing from our small sample, let's check
    track_map = {row['track_id']: f"{row['track_name']} by {row['artists']}" for _, row in track_df.iterrows()}
    
    # Process history
    print("Processing listening history...")
    processed_sessions = []
    for session in history_data:
        user_id = session['user_id']
        track_ids = session['track_ids']
        
        # Map IDs to names
        track_names = [track_map.get(tid, tid) for tid in track_ids]
        
        # We only want tracks that we actually have names for, otherwise the LLM can't recommend
        # But for the baseline, IDs are fine.
        # Let's keep both.
        
        processed_sessions.append({
            'user_id': user_id,
            'track_ids': track_ids,
            'track_names': track_names,
            'user_info': session['user_info']
        })
    
    # Save processed sessions
    print(f"Saving {len(processed_sessions)} processed sessions...")
    with open('results/processed_sessions.json', 'w') as f:
        json.dump(processed_sessions, f)
    
    # Save track map
    with open('results/track_map.json', 'w') as f:
        json.dump(track_map, f)

if __name__ == "__main__":
    preprocess()
