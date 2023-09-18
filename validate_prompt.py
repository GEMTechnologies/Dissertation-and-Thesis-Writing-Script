# validate_prompt.py
import re

def validate_prompt(prompt):
    # Check if prompt has a heading
    if not prompt.startswith("#"):
        prompt = "# " + prompt

    # Extract heading and content
    heading = re.search(r"#(.+)", prompt).group(1).strip()
    content = prompt.replace("#" + heading, "").strip()

    return heading, content
