import json
import os
from llm_recommender import LLMRecommender
from tqdm import tqdm

def load_jsonl(file_path, limit=5):
    data = []
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            if i >= limit:
                break
            data.append(json.loads(line))
    return data

def main():
    recommender = LLMRecommender()
    samples = load_jsonl('datasets/musicrs_sample.jsonl', limit=5)
    results = []

    print(f"Running experiments on {len(samples)} samples...")
    for i, sample in enumerate(tqdm(samples)):
        user_profile = sample['combined_text']
        human_recs = ", ".join(sample['combined_comment_entities'])
        
        # Get Claude's recommendations
        try:
            claude_recs = recommender.get_claude_recommendations(user_profile)
            
            # Judge them
            judgment = recommender.judge_recommendations(user_profile, claude_recs, human_recs)
            
            results.append({
                'sample_id': i,
                'user_profile': user_profile,
                'human_recs': human_recs,
                'claude_recs': claude_recs,
                'judgment': judgment
            })
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"Error on sample {i}: {e}")

    # Save results
    with open('results/experiment_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    # Summarize winners
    winners = [r['judgment'].split('Winner:')[-1].strip() for r in results if 'Winner:' in r['judgment']]
    print("\nSummary of results:")
    for winner in set(winners):
        count = winners.count(winner)
        print(f"{winner}: {count}")

if __name__ == "__main__":
    main()
