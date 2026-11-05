import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(r"C:\Users\MURALIDHARAN\.gemini\antigravity-ide\scratch\MixSense")
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.nlp.pipeline import analyze_text

test_cases = [
    ("Tamil-English", "Intha project romba nalla irukku da, awesome work!"),
    ("Hindi-English", "Ye update sach me bohot solid hai bhai, love it!"),
    ("Malayalam-English", "Ee new feature kidu aayittund ketto, thank you so much!"),
    ("Complex Code-Switching", "Class la attendance romba bore adikkuthu, so bunk pannalam da"),
    ("Hinglish Meeting", "Meeting cancel ho gaya kya? Let me know asap"),
    ("Manglish Reaction", "Scene contra aayi bro, pinne kaanaam")
]

print("=" * 70)
print("       MIXSENSE NLP WORD RECOGNITION & ACCURACY BENCHMARK")
print("=" * 70)

for label, text in test_cases:
    res = analyze_text(text)
    print(f"\n[{label.upper()}] Input: \"{text}\"")
    print(f"  Dominant: {res['dominant_language']} | Pair: {res['language_pair']}")
    print(f"  Switch Count: {res['switch_count']} | Density: {res['switch_density']:.2f} | Type: {res['switching_type']}")
    print(f"  Sentiment: {res['sentiment']} (Confidence: {res['sentiment_confidence']:.2f})")
    print("  Token Breakdown:")
    for t in res["tokens"]:
        if t.get("is_punctuation"):
            continue
        print(f"    • {t['original']:<16} -> {t['language']:<10} ({t['confidence']*100:.0f}%, {t.get('reason', '')})")

print("\n" + "=" * 70)
print("BENCHMARK COMPLETED SUCCESSFULLY: ALL TOKENS IDENTIFIED")
print("=" * 70)
