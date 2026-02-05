import random

tips = [
    "💡 **Tip:** Use `enumerate()` instead of `range(len())` to get both index and value.",
    "💡 **Tip:** Use `zip()` to iterate over multiple lists at once.",
    "💡 **Tip:** `.get()` on dictionaries prevents `KeyError`.",
    "💡 **Tip:** `isinstance(obj, int)` is safer than `type(obj) == int`.",
    "💡 **Tip:** F-strings are faster and cleaner than `.format()`."
]

def update_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Hard-coded strings to avoid "empty separator" variable issues
        if "" not in content:
            print("Missing start marker!")
            return

        # Splitting directly using the string literals
        before = content.split("")[0]
        after = content.split("")[1]
        
        new_tip = random.choice(tips)
        
        # Rebuild
        new_content = before + "\n" + new_tip + "\n" + after
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully updated README.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    update_readme()
