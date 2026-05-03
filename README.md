# LLM vs. Spotify Recommendation Impact

This research evaluates whether Large Language Models (LLMs) can provide better music recommendations than Spotify's traditional algorithms using exported user data.

## Key Findings
- **LLMs vs. Humans**: LLMs matched or outperformed human-curated Reddit recommendations in **80% of test cases**.
- **Thematic Coherence**: LLMs excel at cross-genre bridging and semantic understanding (e.g., linking "Indie Folk" and "Pop-Punk" through shared emotional textures).
- **Explainability**: Unlike black-box algorithms, LLMs provide clear reasoning for each recommendation, enhancing the discovery experience.
- **Niche Limits**: Human experts still outperform LLMs in highly specialized classical or niche sub-genres.

## File Structure
- `REPORT.md`: Full research report with methodology, results, and analysis.
- `src/`: Source code for data preprocessing and LLM experimentation.
- `datasets/`: Sample datasets used for evaluation (MusiCRS, Spotify History).
- `results/`: Raw output from experiments and LLM judgments.

## How to Reproduce
1. **Setup Environment**:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install pandas openai anthropic tqdm tenacity
   ```
2. **Run Preprocessing**:
   ```bash
   python src/preprocess_data.py
   ```
3. **Run Experiments**:
   ```bash
   export OPENROUTER_KEY='your_key'
   export OPENAI_API_KEY='your_key'
   python src/run_experiment.py
   ```

## References
- MusiCRS Dataset: `rohan2810/MusiCRS`
- Spotify Tracks Dataset: `maharshipandya/spotify-tracks-dataset`
- Listening History: `talkpl-ai/listening-history-filtered`
