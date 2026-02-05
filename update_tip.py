import random

def update_readme():
    tips = [
        "💡 **Tip:** Use `enumerate()` instead of `range(len())` to get both index and value.",
        "💡 **Tip:** Use `zip()` to iterate over multiple lists at once.",
        "💡 **Tip:** `.get()` on dictionaries prevents `KeyError`.",
        "💡 **Tip:** `isinstance(obj, int)` is safer than `type(obj) == int`.",
        "💡 **Tip:** F-strings are faster and cleaner than `.format()`."
    ]

    start_m = ""
    end_m = ""
    
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        skip = False
        
        for line in lines:
            if start_m in line:
                new_lines.append(line)
                new_lines.append(random.choice(tips) + "\n")
                skip = True
            elif end_m in line:
                new_lines.append(line)
                skip = False
            elif not skip:
                new_lines.append(line)

        with open("README.md", "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Done!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_readme()
