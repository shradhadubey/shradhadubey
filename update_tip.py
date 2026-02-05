import random

tips = [
    "💡 **Tip:** Use `enumerate()` instead of `range(len())` to get both index and value.",
    "💡 **Tip:** Use `zip()` to iterate over multiple lists at once.",
    "💡 **Tip:** `.get()` on dictionaries prevents `KeyError`.",
    "💡 **Tip:** `isinstance(obj, int)` is safer than `type(obj) == int`.",
    "💡 **Tip:** F-strings are faster and cleaner than `.format()`."
]

def update_readme():
    start_marker = ""
    end_marker = ""
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    if start_marker not in content or end_marker not in content:
        print("Markers missing! Check your README.")
        return

    # Split the file into three static parts
    before_part = content.split(start_marker)[0]
    after_part = content.split(end_marker)[1]
    
    new_tip = random.choice(tips)
    
    # Reassemble: [Everything Before] + [Start] + [New Tip] + [End] + [Everything After]
    new_content = f"{before_part}{start_marker}\n{new_tip}\n{end_marker}{after_part}"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
