import random

tips = [
    "💡 **Tip:** Use `enumerate()` instead of `range(len())` to get both index and value.",
    "💡 **Tip:** Use `zip()` to iterate over multiple lists at once.",
    "💡 **Tip:** `isinstance(obj, int)` is safer than `type(obj) == int`.",
    "💡 **Tip:** Use `.get()` on dictionaries to avoid `KeyError`.",
    "💡 **Tip:** F-strings are faster and cleaner than `.format()`."
]

def update_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Split the file by our markers
    start_marker = ""
    end_marker = ""
    
    try:
        # We split the text into three parts: Before, Old Tip, After
        before_part = content.split(start_marker)[0]
        after_part = content.split(end_marker)[1]
        
        new_tip = random.choice(tips)
        
        # Reconstruct the file with the new tip in the middle
        new_content = f"{before_part}{start_marker}\n{new_tip}\n{end_marker}{after_part}"
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
            
    except IndexError:
        print("Markers not found in README.md! Make sure they exist.")

if __name__ == "__main__":
    update_readme()
