# Research Plan: LLMs vs. Spotify Recommendation Algorithms

## Motivation & Novelty Assessment

### Why This Research Matters
Users are increasingly interested in "bringing their own data" to LLMs to get more personalized experiences. Music recommendation is a highly personal and emotional domain where traditional algorithms (like Spotify's) have set a high bar. Understanding if a general-purpose LLM can outperform these specialized systems is crucial for the future of personalized AI.

### Gap in Existing Work
Most RecSys research focuses on collaborative filtering on static datasets (MovieLens, Amazon). While "LLM-as-recommender" is a growing field, there is a lack of direct comparison between the "data export + LLM" workflow and specialized music recommendation baselines on real-world listening sequences.

### Our Novel Contribution
We will simulate the "Spotify Export" workflow using a real-world listening history dataset. We will compare Claude 3.5 Sonnet's zero-shot and few-shot recommendations against a strong traditional baseline (BPR/LightGCN) using both predictive metrics (Recall@K) and qualitative "LLM-as-a-judge" evaluations.

### Experiment Justification
- **Experiment 1: Next-Item Prediction (Quantitative)**
  - *Why*: To measure the objective ability of the LLM to capture the user's immediate musical trajectory.
  - *Metric*: Recall@5, NDCG@5.
- **Experiment 2: Recommendation Quality (Qualitative)**
  - *Why*: "Better" in music is often about discovery, diversity, and thematic coherence, which Recall doesn't capture.
  - *Metric*: LLM-as-a-judge scores for Relevance, Diversity, and Serendipity.

---

## Research Question
"If I export all my Spotify data and ask Claude for recommendations, is it better than Spotify's own recommendations?"

## Hypothesis Decomposition
1. **H1 (Utility)**: Claude can predict the next tracks in a user session with accuracy comparable to traditional baselines.
2. **H2 (Quality)**: Claude's recommendations are perceived as more "thematically coherent" and "personalized" than traditional baselines when evaluated qualitatively.

## Proposed Methodology

### Approach
We will use the `listening-history-sample.jsonl` dataset as a proxy for Spotify export data. Each user session will be split into a "History" (prefix) and "Target" (remainder). 
- **LLM**: Claude 3.5 Sonnet (via API).
- **Baseline**: A traditional Matrix Factorization or Graph-based model (from `recommenders_team`).
- **Evaluation**: 
  - Compare predicted tracks with target tracks.
  - Use a separate "Judge LLM" to compare the quality of LLM vs. Baseline outputs.

### Experimental Steps
1. **Data Preprocessing**:
   - Map Spotify IDs to Track/Artist names using `spotify_tracks_sample.jsonl`.
   - Filter sessions to ensure minimum length (e.g., 10 tracks).
2. **Baseline Implementation**:
   - Train a BPR (Bayesian Personalized Ranking) model on the training portion of the listening history.
3. **LLM Prompting**:
   - Design a prompt that takes the user history (Track Name - Artist) and asks for 5-10 recommendations.
   - Test Zero-shot and Few-shot (if possible with session data).
4. **Evaluation**:
   - Calculate Recall@5 and NDCG@5 for both.
   - Run LLM-as-a-judge on a sample of users.

### Baselines
- **BPR (Bayesian Personalized Ranking)**: A standard and strong baseline for implicit feedback.
- **Popularity**: To see how much "better" the models are than just suggesting top tracks.

### Evaluation Metrics
- **Recall@5**: Fraction of target tracks captured in top 5 recommendations.
- **NDCG@5**: Normalized Discounted Cumulative Gain (ranking quality).
- **Quality Score (1-10)**: Judged by an independent LLM on relevance to history.

## Expected Outcomes
We expect the LLM to have lower Recall than the baseline (as it hasn't seen millions of other users' patterns) but higher Quality scores (as it understands the *meaning* of the track titles and genres).

## Timeline and Milestones
- **Hour 1**: Data prep and environment setup.
- **Hour 2**: Baseline training and evaluation.
- **Hour 3**: LLM evaluation and qualitative judging.
- **Hour 4**: Analysis and Report writing.

## Success Criteria
The research is successful if we can quantify the trade-off between traditional "collaborative" intelligence and LLM "semantic" intelligence in music recommendation.
