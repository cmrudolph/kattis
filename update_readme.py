import glob
import os
import re

types = {
    "c": "C",
    "cpp": "C++",
    "cs": "C#",
    "go": "Go",
    "py": "Python"
}


def extract_desc(lines, comment):
    start_seen = False
    desc_lines = []

    for line in lines:
        line = line.lstrip(" " + comment).rstrip("\n")
        if "==========" in line:
            if not start_seen:
                start_seen = True
            else:
                break
        elif start_seen:
            desc_lines.append(line)

    return " ".join([x.strip() for x in desc_lines])


if __name__ == "__main__":
    files = []
    markdown = []

    for ext in types:
        files.extend(glob.glob("*/*." + ext))

    files = [f.replace("\\", "/") for f in files]
    for file in files:
        with open(file, "r") as f:
            lines = f.readlines()
            ext = os.path.splitext(file)[1][1:]
            lang = types[ext]
            name_result = re.search("NAME : (.*)", lines[0])
            url_result = re.search("URL  : (.*)", lines[1])
            if name_result is not None and url_result is not None:
                name = name_result.group(1)
                url = url_result.group(1)
                desc = extract_desc(lines, "/#")
                entry = (
                    name,
                    f"**{name} | {lang}** | [Problem]({url}) | [Solution]({file})</br>",
                    desc
                )
                markdown.append(entry)

    markdown.sort(key=lambda x: x[0])
    with open("README.md", "w") as f:
        for e in markdown:
            f.write(e[1] + "\n")
            f.write(e[2] + "\n")
            f.write("</br></br>\n")
