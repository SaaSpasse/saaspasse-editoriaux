#!/usr/bin/env python3
"""Debug édito detection."""

import re
import html as html_lib
from pathlib import Path

html_file = Path.home() / "claude-code/posts-infolettre/samples/sample_1.html"

with open(html_file, 'r', encoding='utf-8') as f:
    raw_html = f.read()

# Décoder
text = html_lib.unescape(raw_html)

# Chercher "What's up folks"
matches = list(re.finditer(r"What.{0,5}s.{0,5}up.{0,5}folks", text, re.IGNORECASE | re.DOTALL))
print(f"Found {len(matches)} matches for 'What's up folks'")

if matches:
    for i, m in enumerate(matches[:3]):
        print(f"\nMatch {i+1}:")
        snippet = text[max(0, m.start()-50):min(len(text), m.end()+100)]
        print(repr(snippet))

# Chercher "Merci d'être"
matches2 = list(re.finditer(r"Merci.{0,5}d.{0,5}être", text, re.IGNORECASE | re.DOTALL))
print(f"\n\nFound {len(matches2)} matches for 'Merci d\\'être'")

if matches2:
    for i, m in enumerate(matches2[:3]):
        print(f"\nMatch {i+1}:")
        snippet = text[max(0, m.start()-50):min(len(text), m.end()+100)]
        print(repr(snippet))
