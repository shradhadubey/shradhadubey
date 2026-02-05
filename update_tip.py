import random

tips = [
    "💡 **Tip:** Use `enumerate()` instead of `range(len())` to get both index and value.",
    "💡 **Tip:** Use `zip()` to iterate over multiple lists at once.",
    "💡 **Tip:** `.get()` on dictionaries prevents `KeyError`.",
    "💡 **Tip:** `isinstance(obj, int)` is safer than `type(obj) == int`.",
    "💡 **Tip:** F-strings are faster and cleaner than `.format()`."
]

def update_readme():
    # Define markers clearly
    START = ""
    END = ""
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Safety Guard: Check if markers actually exist in the file
    if START not in content or END not in content:
        print(f"FAILED: Markers not found in README. Check for {START}")
        return

    # Logical split
    try:
        before = content.split(START)[0]
        after = content.split(END)[1]
        
        new_tip = random.choice(tips)
        
        # Re-build the file
        new_content = f"{before}{START}\n{new_tip}\n{END}{after}"
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("SUCCESS: README updated with a new tip.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    update_readme()
