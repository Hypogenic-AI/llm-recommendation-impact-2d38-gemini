# Literature Review: LLMs vs. Traditional Recommendation Algorithms for Music

## Research Area Overview
Large Language Models (LLMs) are increasingly being applied to Recommendation Systems (RecSys). Traditional systems primarily rely on Collaborative Filtering (CF) and Content-Based Filtering (CBF). LLMs offer a new paradigm by treating recommendation as a natural language task, allowing for zero-shot and few-shot capabilities, conversational interfaces, and reasoning over unstructured data.

## Key Papers

### 1. Uncovering ChatGPT’s Capabilities in Recommender Systems (2023)
- **Authors**: Sunhao Dai et al.
- **Key Contribution**: Investigates how to align ChatGPT with recommendation tasks using point-wise, pair-wise, and list-wise ranking.
- **Key Findings**: List-wise ranking provides the best balance of cost and performance. ChatGPT shows strong zero-shot performance but still struggles in some traditional metrics compared to state-of-the-art specialized models.
- **Relevance**: Provides the foundational prompting strategies (list-wise ranking) for evaluating LLMs as recommenders.

### 2. MusiCRS: Benchmarking Audio-Centric Conversational Recommendation (2025)
- **Authors**: Rohan Surana et al.
- **Key Contribution**: Introduces a benchmark for music recommendation that integrates authentic user conversations (Reddit) with audio grounding.
- **Key Findings**: Current systems struggle with cross-modal integration (audio + text). LLMs excel at dialogue semantics but fail to ground abstract musical concepts in actual audio.
- **Relevance**: Provides a specific benchmark and dataset for conversational music recommendation, which is a key part of the hypothesis.

### 3. Music Recommendation with Large Language Models: Challenges, Opportunities, and Evaluation (2025)
- **Key Contribution**: Discusses the transition from ranking-based to generative evaluation.
- **Key Findings**: Evaluation of LLMs requires new metrics beyond NDCG/Recall, such as "LLM-as-a-judge" or human-centric qualitative assessment.
- **Relevance**: Directly addresses the "evaluation" aspect of the hypothesis—how to tell if LLM recommendations are "better" than Spotify's.

### 4. Evaluating Podcast Recommendations with Profile-Aware LLM-as-a-Judge (2025)
- **Key Contribution**: Specifically looks at Spotify data (podcasts) and uses LLMs to evaluate recommendation quality.
- **Relevance**: Proof of concept for using LLMs to evaluate Spotify-like recommendations.

## Common Methodologies
1. **Prompting Strategies**: List-wise ranking is preferred over point-wise (too expensive) or pair-wise (too many combinations).
2. **In-Context Learning (ICL)**: Providing a few examples of user history to the LLM to improve personalization.
3. **Multimodal Integration**: Combining track metadata (text) with audio features or raw audio.

## Evaluation Metrics
- **Traditional**: NDCG, Recall@K, Precision@K.
- **LLM-Specific**: Diversity, Explainability, "LLM-as-a-judge" (using a stronger LLM like GPT-4o or Claude 3.5 Sonnet to score recommendations).

## Recommendations for Our Experiment
- **Dataset**: Use `talkpl-ai/listening-history-filtered` as a proxy for Spotify export data.
- **Baseline**: Compare LLM (Claude/GPT) against traditional baselines from the `Microsoft Recommenders` repo and `MusiCRS` baselines.
- **Evaluation**: Use both traditional metrics (Recall@K) and an "LLM-as-a-judge" setup where the LLM explains why a recommendation is good based on the user's history.
