import random

# Our list of tips
tips = [
    "💡 **Tip:** Use `enumerate()` instead of `range(len())` to get both index and value.",
    "💡 **Tip:** Use `zip()` to iterate over multiple lists at once.",
    "💡 **Tip:** `.get()` on dictionaries prevents `KeyError`.",
    "💡 **Tip:** `isinstance(obj, int)` is safer than `type(obj) == int`.",
    "💡 **Tip:** F-strings are faster and cleaner than `.format()`."
]

def update_readme():
    # ENSURE THESE STRINGS ARE NOT EMPTY
    start_marker = ""
    end_marker = ""
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Safety Check: If markers aren't there, don't crash
    if start_marker not in content or end_marker not in content:
        print(f"Error: Could not find {start_marker} or {end_marker} in README.md")
        return

    # Split the file: [Before the tip, The tip itself, After the tip]
    parts_start = content.split(start_marker)
    parts_end = parts_start[1].split(end_marker)

    before_everything = parts_start[0]
    after_everything = parts_end[1]
    
    new_tip = random.choice(tips)
    
    # Reconstruct the file safely
    new_content = f"{before_everything}{start_marker}\n{new_tip}\n{end_marker}{after_everything}"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
