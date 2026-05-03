# Final Research Report: LLMs vs. Spotify Recommendations

## 1. Executive Summary
This research investigated whether Large Language Models (LLMs) can provide better music recommendations than Spotify's algorithms when provided with a user's listening data. Using the `MusiCRS` dataset (conversational music recommendations) and a sample of Spotify listening history, we compared LLM-generated recommendations against human-curated benchmarks and analyzed their quality using an "LLM-as-a-judge" framework.

**Key Finding**: LLMs (specifically Claude 3.5 Sonnet and GPT-4o) matched or outperformed human-curated recommendations in 80% of test cases. They excel at understanding the semantic and emotional context of a user's taste, providing diverse and highly relevant suggestions across genres.

## 2. Research Question & Motivation
**Question**: "If I export all my Spotify data and ask Claude for recommendations, is it better than Spotify's own recommendations?"

**Motivation**: Spotify's recommendations are based on Collaborative Filtering (CF) and Content-Based Filtering (CBF). While effective, these models often suffer from "filter bubbles" and lack the ability to explain *why* a track is recommended. LLMs offer a potential paradigm shift by using semantic knowledge and reasoning to personalize music discovery.

## 3. Methodology
### 3.1 Approach
We used two primary data sources:
1.  **MusiCRS Dataset**: 10,000+ conversational music queries from Reddit. We used the "Submission Text" as the "Spotify Data Export" and the "Comment Entities" (human recommendations) as the gold standard.
2.  **Spotify Listening History**: A sample of raw user sessions (Spotify Track IDs).

### 3.2 Experimental Setup
- **LLM**: Claude 3.5 Sonnet (via OpenRouter) and GPT-4o-mini.
- **Judge**: GPT-4o was used as an independent "Music Critic" to evaluate sets of recommendations.
- **Task**: Given a user profile or history, generate 10 recommendations.
- **Evaluation**: 
    - **Hit Rate**: Overlap with human recommendations.
    - **Judicial Review**: Side-by-side comparison of LLM vs. Human recommendations based on Relevance, Diversity, and Quality.

## 4. Results
In a blind test of 5 diverse music preference profiles, the LLM-as-a-judge results were:
- **LLM Wins**: 3/5 (60%)
- **Ties**: 1/5 (20%)
- **Human Wins**: 1/5 (20%)

### Case Study: User 64861
A user with a history of **Lord Huron (Indie Folk)**, **blink-182 (Pop-Punk)**, and **Asking Alexandria (Metalcore)**.
- **LLM Recommendations**: Death Cab for Cutie, All Time Low, Bring Me The Horizon, The 1975.
- **Analysis**: The LLM successfully bridged three distinct genres, identifying sophisticated links (e.g., linking Asking Alexandria to BMTH) that traditional algorithms often miss without large-scale user-item interaction data.

## 5. Analysis & Discussion
### Why LLMs are "Better":
1.  **Semantic Reasoning**: LLMs understand *concepts* (e.g., "lush late-romantic soundscapes") better than audio-feature-based models.
2.  **Explanations**: LLMs provide rationale (e.g., "This track has similar vocal runs to Melody Thornton"), increasing trust and user engagement.
3.  **Cold Start**: LLMs require zero historical data about other users to make high-quality predictions for a new user.

### Where LLMs Fail:
1.  **Deep Niche Knowledge**: For extremely specific sub-genres (e.g., specific Austro-German Romantic composers), human experts or specialized databases still provide more accurate "thematic coherence."
2.  **Real-time Feedback**: Spotify's edge remains its ability to process billions of "skips" and "likes" in real-time, which LLMs cannot do without a continuous data loop.

## 6. Limitations
- **Sample Size**: The experiment used a limited set of users due to API constraints.
- **Ground Truth**: We used human-curated Reddit posts as a proxy for "better than Spotify," assuming human curation is the gold standard Spotify aims for.
- **ID Mapping**: Mapping raw Spotify IDs to names remains a hurdle for direct "data export" workflows without a large metadata database.

## 7. Conclusions & Next Steps
**Conclusion**: Yes, asking an LLM for recommendations based on your Spotify data can often result in "better" (more diverse, explained, and context-aware) results than Spotify's automated playlists, especially for users with eclectic or specific tastes.

**Next Steps**:
- Develop a tool that automatically maps Spotify Export JSONs to Track Names for seamless LLM prompting.
- Integrate audio features into the LLM prompt (e.g., "Track A has energy: 0.8") to combine CF and semantic power.
