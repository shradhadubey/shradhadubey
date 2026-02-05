import random
import re

# Add as many tips as you want here!
tips = [
    "💡 **Tip:** Use `enumerate()` instead of `range(len())` to get both index and value.",
    "💡 **Tip:** Use `zip()` to iterate over two lists at the same time.",
    "💡 **Tip:** List comprehensions are usually faster than explicit `for` loops.",
    "💡 **Tip:** Use `f-strings` (f'{var}') for the most readable string formatting.",
    "💡 **Tip:** The `collections.Counter` class is great for counting items in a list.",
    "💡 **Tip:** Use `pathlib` instead of `os.path` for more modern file handling.",
    "💡 **Tip:** `isinstance(obj, int)` is better than `type(obj) == int`."
]

def update_readme():
    tip = random.choice(tips)
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # This regex finds the space between our markers and swaps the tip
    new_content = re.sub(
        r".*?",
        f"\n{tip}\n",
        content,
        flags=re.DOTALL
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
