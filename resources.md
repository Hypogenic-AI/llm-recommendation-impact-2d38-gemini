# Resources Catalog

## Summary
This catalog lists the papers, datasets, and code gathered to evaluate whether LLMs can outperform Spotify's recommendation algorithms.

## Papers
| Title | Year | File | Key Info |
|-------|------|------|----------|
| Uncovering ChatGPT’s Capabilities | 2023 | [2305.02182](papers/2305.02182_ChatGPT_RecSys.pdf) | Ranking strategies (List-wise). |
| MusiCRS Benchmark | 2025 | [2509.19469](papers/2509.19469_MusiCRS.pdf) | Conversational music dataset. |
| Harnessing Song Descriptors | 2024 | [2410.13470](papers/2410.13470_Harnessing_Descriptors.pdf) | NL-based music recommendation. |
| LLM-as-a-Judge for Spotify | 2024 | [2405.20457](papers/2405.20457_LLM_as_Judge_Spotify.pdf) | Evaluation framework using LLMs. |

## Datasets
| Name | Source | Task | Location |
|------|--------|------|----------|
| MusiCRS Sample | rohan2810/MusiCRS | Conversational Rec | `datasets/musicrs_sample.jsonl` |
| Spotify Tracks | maharshipandya/spotify-tracks | Metadata/Features | `datasets/spotify_tracks_sample.jsonl` |
| Listening History | talkpl-ai/listening-history | User History | `datasets/listening_history_sample.jsonl` |

## Code Repositories
| Name | Purpose | Location |
|------|---------|----------|
| MusiCRS | Audio-LLM Baselines | `code/musiCRS/` |
| LLM4RS | Prompting Frameworks | `code/LLM4RS/` |
| Recommenders | Traditional Baselines | `code/recommenders_team/` |

## Recommendations for Experiment Design
1. **Goal**: Compare LLM zero-shot/few-shot recommendations with a traditional CF baseline on the `Listening History` dataset.
2. **Setup**:
   - Input: User listening session (last 10-20 tracks).
   - Task: Predict the next 5 tracks.
   - LLM: Use Claude 3.5 Sonnet or GPT-4o with list-wise ranking prompts.
   - Baseline: Use LightGCN or BPR from the Microsoft Recommenders repo.
3. **Metrics**:
   - Recall@5, NDCG@5.
   - Qualitative comparison using "LLM-as-a-judge".
