import re
import os

file_path = r"c:\Users\aoraz\Desktop\cv website\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. COLORS
text = text.replace("--gold-bright: #FFD700;", "--gold-bright: #C9A060;")
text = text.replace("--gold: #C9A84C;", "--gold: #B4913C;")

lines_to_remove = [
    r"text-shadow:\s*0\s+0\s+40px[^;]+;",
    r"text-shadow:\s*0\s+0\s+20px[^;]+;",
    r"text-shadow:\s*0\s+0\s+10px[^;]+;",
    r"text-shadow:\s*0\s+0\s+30px[^;]+;"
]
for pattern in lines_to_remove:
    text = re.sub(pattern, "", text)

css_hero_name = """
        #heroLine1 .magnetic-letter,
        #heroLine1 .magnetic-letter.attracted,
        #heroLine2 .magnetic-letter,
        #heroLine2 .magnetic-letter.attracted {
            color: #FFFFFF !important;
            text-shadow: none !important;
        }
"""
text = text.replace("/* Magnetic Letters Glow */", "/* Magnetic Letters Glow */\n" + css_hero_name)

def halve_rgba_alpha(m):
    prefix = m.group(1)
    alpha = float(m.group(2))
    new_alpha = alpha * 0.5
    return f"rgba({prefix}, {new_alpha:g})"

text = re.sub(r'rgba\((\d+,\s*\d+,\s*\d+),\s*([0-9.]+)\)', halve_rgba_alpha, text)
text = text.replace("--glow-gold: rgba(201, 168, 76, 0.4);", "--glow-gold: rgba(201, 168, 76, 0.2);")

# 2. ANIMATIONS
text = re.sub(r'(transition:[^;]+?)0\.[1234]5?s', r'\g<1>0.5s', text)

text = text.replace("Float32Array(800 * 3)", "Float32Array(500 * 3)")
text = text.replace("i<800*3", "i<500*3")
text = text.replace("(Math.random() - 0.5) * 0.02", "(Math.random() - 0.5) * 0.012")

text = re.sub(r'(duration:\s*)1[.]?\d*,', r'\g<1>0.8,', text)

# 3. WHITESPACE
text = text.replace("padding: 100px 20px;", "padding: 130px 20px;")
text = re.sub(r'(\.card-back\s*\{[^}]*?padding:\s*)24px', r'\g<1>32px', text)
text = re.sub(r'(\.about-grid\s*\{[^}]*?gap:\s*)60px', r'\g<1>100px', text)

# 4. REMOVE glow from skill card borders
text = re.sub(r'(\.skill-card\s*\{)', r'\g<1>\n            box-shadow: none !important;', text)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
