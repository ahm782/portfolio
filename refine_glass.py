import re

file_path = r"c:\Users\aoraz\Desktop\cv website\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update CSS Variables
text = text.replace("--glass-bg: rgba(10, 10, 20, 0.3);", "--glass-bg: rgba(255, 255, 255, 0.03);")
text = text.replace("--glass-border: rgba(201, 168, 76, 0.075);", "--glass-border: rgba(201, 168, 76, 0.2);")

# 2. Update .glass-card base
glass_card_old = """        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);"""
glass_card_new = """        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.1);"""
text = text.replace(glass_card_old, glass_card_new)

# 3. Update .card-front
# Using regex to replace the background/backdrop block
text = re.sub(
    r'\.card-front\s*\{\s*background:\s*[^;]+;\s*backdrop-filter:\s*[^;]+;\s*-webkit-backdrop-filter:\s*[^;]+;',
    '.card-front {\n            background: rgba(255, 255, 255, 0.03);\n            backdrop-filter: blur(20px);\n            -webkit-backdrop-filter: blur(20px);',
    text
)
# Add inner glow to .card-front box-shadow
text = re.sub(
    r'(\.card-front\s*\{[^\}]*box-shadow:\s*)(0 4px 30px rgba\(0, 0, 0, 0\.2\));',
    r'\g<1>\g<2>, inset 0 1px 0 rgba(255,255,255,0.1);',
    text
)

# 4. Update .card-back
text = re.sub(
    r'\.card-back\s*\{\s*background:\s*[^;]+;\s*backdrop-filter:\s*[^;]+;\s*-webkit-backdrop-filter:\s*[^;]+;',
    '.card-back {\n            background: rgba(255, 255, 255, 0.03);\n            backdrop-filter: blur(20px);\n            -webkit-backdrop-filter: blur(20px);',
    text
)
text = re.sub(
    r'(\.card-back\s*\{[^\}]*box-shadow:\s*)(0 4px 30px rgba\(0, 0, 0, 0\.2\));',
    r'\g<1>\g<2>, inset 0 1px 0 rgba(255,255,255,0.1);',
    text
)

# 5. Update .skill-card
text = re.sub(
    r'\.skill-card\s*\{\s*background:\s*[^;]+;\s*backdrop-filter:\s*[^;]+;\s*border:\s*[^;]+;',
    '.skill-card {\n            background: rgba(255, 255, 255, 0.03);\n            backdrop-filter: blur(20px);\n            border: 1px solid rgba(201, 168, 76, 0.2);',
    text
)
# Note: we already added `box-shadow: none !important;` to .skill-card in the previous script. Let's replace it with the inner glow.
text = text.replace(
    ".skill-card {\n            box-shadow: none !important;",
    ".skill-card {\n            box-shadow: inset 0 1px 0 rgba(255,255,255,0.1) !important;"
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Glassmorphism update complete")
