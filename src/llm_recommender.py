import os
import openai
from tenacity import retry, wait_exponential, stop_after_attempt

class LLMRecommender:
    def __init__(self):
        # OpenRouter for Claude
        self.openrouter_client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_KEY"),
        )
        # OpenAI for GPT-4o (Judge)
        self.openai_client = openai.OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    @retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(3))
    def get_claude_recommendations(self, user_profile, n=10):
        prompt = f"""You are a music recommendation expert. A user has provided the following description of their musical taste and current listening habits:

{user_profile}

Based on this, recommend {n} tracks they would love. Provide the artist and track name for each. 
Format your response as a numbered list, like this:
1. Track Name by Artist
2. Track Name by Artist
...
Only provide the list, no intro or outro."""

        response = self.openrouter_client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://github.com/gemini-cli",
                "X-Title": "Gemini CLI Research",
            },
            model="openai/gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    @retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(3))
    def judge_recommendations(self, user_profile, recs_a, recs_b):
        prompt = f"""You are an expert music critic. Your task is to compare two sets of music recommendations for a user.

User Profile/Context:
{user_profile}

Set A (Claude's Recommendations):
{recs_a}

Set B (Human/Reddit Recommendations):
{recs_b}

Compare these two sets based on:
1. Relevance: How well do the tracks match the user's specific request and taste?
2. Diversity: Does the set offer a good variety within the requested style?
3. Quality: Are the recommended tracks generally well-regarded or high-quality?

Which set is better? Provide a brief explanation and then end with "Winner: Set A" or "Winner: Set B" or "Winner: Tie"."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    # Test
    import os
    if os.getenv("OPENROUTER_KEY"):
        rec = LLMRecommender()
        print(rec.get_claude_recommendations("I love early 2000s R&B like Destiny's Child."))
