import re
import os

file_path = r"c:\Users\aoraz\Desktop\cv website\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Fix particle count if my previous replace failed because it was a variable
text = text.replace("const particleCount = 800;", "const particleCount = 500;")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed particle count")
