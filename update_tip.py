import random
import pyjokes          

def update_readme():
    tips = [
        "💡 **Tip:** Use `enumerate()` instead of `range(len())` to get both index and value.",
        "💡 **Tip:** Use `zip()` to iterate over multiple lists at once.",
        "💡 **Tip:** `.get()` on dictionaries prevents `KeyError`.",
        "💡 **Tip:** `isinstance(obj, int)` is safer than `type(obj) == int`.",
        "💡 **Tip:** F-strings are faster and cleaner than `.format()`."
    ]

    try:
        # 1. Read the template
        with open("README.template", "r", encoding="utf-8") as f:
            template = f.read()

        # 2. Pick a tip & joke
        new_tip = random.choice(tips)
        # Using 'neutral' category for professional profiles
        new_joke = f"奏 {pyjokes.get_joke(language='en', category='neutral')}"

        # 3. Replace the placeholder with the tip
        final_content = template.replace("PYTHON_TIP_HERE", new_tip)
        final_content = final_content.replace("PYTHON_JOKE_HERE", new_joke)

        # 4. Write to the actual README.md
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(final_content)
            
        print("Successfully generated README from template.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_readme()
