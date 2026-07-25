import random
import re
import urllib.request
import json

# Curated list of actionable Python tips
PYTHON_TIPS = [
    "💡 **Tip:** Use `zip()` to iterate over multiple iterables simultaneously without managing manual counters.",
    "💡 **Tip:** Leverage `pathlib.Path` instead of `os.path` for object-oriented, cross-platform file path handling.",
    "💡 **Tip:** Use `collections.defaultdict` to avoid key-checking logic when initializing dictionary values.",
    "💡 **Tip:** Use list comprehension `[x for x in data if condition]` for clean, concise filtering.",
    "💡 **Tip:** Enumerate over sequences with `for idx, item in enumerate(items):` to track indices cleanly.",
    "💡 **Tip:** Use `f-strings` with formatting specifiers (e.g., `f'{value:.2f}'` or `f'{date:%Y-%m-%d}'`) for fast string formatting.",
    "💡 **Tip:** Use `dataclasses.dataclass` to auto-generate `__init__`, `__repr__`, and equality methods for data containers.",
    "💡 **Tip:** Use `itertools.chain()` to combine multiple iterables into a single sequence without loading everything into memory."
]

def fetch_dev_joke() -> str:
    """Fetch a clean programming joke from JokeAPI fallback to local list if API fails."""
    url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            if data.get("error"):
                raise ValueError("API returned error status")

            if data.get("type") == "single":
                return data["joke"]
            elif data.get("type") == "twopart":
                return f"{data['setup']}\n\n*{data['delivery']}*"
    except Exception:
        # Fallback jokes in case the external API is temporarily down
        fallbacks = [
            "Software developers like to solve problems. If there are no problems handily available, they will create their own.",
            "There are 10 types of people in the world: those who understand binary, and those who don't.",
            "A SQL query walks into a bar, walks up to two tables, and asks... 'Can I join you?'",
            "Why do programmers prefer dark mode? Because light attracts bugs."
        ]
        return random.choice(fallbacks)

def update_readme():
    tip = random.choice(PYTHON_TIPS)
    joke = fetch_dev_joke()

    with open("README.template", "r", encoding="utf-8") as f:
        template_content = f.read()

    updated_content = template_content.replace("PYTHON_TIP_HERE", tip)
    updated_content = updated_content.replace("PYTHON_JOKE_HERE", joke)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Successfully updated README.md from README.template!")

if __name__ == "__main__":
    update_readme()
