# Downloaded Datasets

This directory contains samples of datasets used for the research project. Full datasets can be downloaded using the provided scripts or HuggingFace identifiers.

## 1. MusiCRS (Conversational)
- **Source**: [rohan2810/MusiCRS](https://huggingface.co/datasets/rohan2810/MusiCRS)
- **Format**: JSONL (sample)
- **Description**: Conversational music recommendations from Reddit, grounded in YouTube audio.
- **Location**: `datasets/musicrs_sample.jsonl`

## 2. Spotify Tracks (Metadata)
- **Source**: [maharshipandya/spotify-tracks-dataset](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset)
- **Format**: JSONL (sample)
- **Description**: 114k Spotify tracks with audio features (danceability, energy, etc.).
- **Location**: `datasets/spotify_tracks_sample.jsonl`

## 3. Listening History (User Data)
- **Source**: [talkpl-ai/listening-history-filtered](https://huggingface.co/datasets/talkpl-ai/listening-history-filtered)
- **Format**: JSONL (sample)
- **Description**: User listening history sessions with Spotify track IDs and user demographics.
- **Location**: `datasets/listening_history_sample.jsonl`

## Download Instructions

To download full datasets, use the following Python snippet:

```python
from datasets import load_dataset

# MusiCRS
ds_musicrs = load_dataset("rohan2810/MusiCRS")

# Spotify Tracks
ds_spotify = load_dataset("maharshipandya/spotify-tracks-dataset")

# Listening History
ds_history = load_dataset("talkpl-ai/listening-history-filtered")
```
