#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

file_path = os.path.join(os.path.dirname(__file__), 'index.html')

# Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Color mapping
old_new_colors = [
    ('#2D1B69', '#B0183D'),  # Dark text color
    ('#2d1b69', '#B0183D'),  # Dark text color (lowercase)
    ('#e91e63', '#E23C64'),  # Primary magenta
    ('#E91E63', '#E23C64'),  # Primary magenta (uppercase)
    ('#4caf50', '#FFD464'),  # Success green → gold
    ('#4CAF50', '#FFD464'),  # Success green uppercase
    ('#f44336', '#FF5E5E'),  # Error red → coral
    ('#F44336', '#FF5E5E'),  # Error red uppercase
    ('#ff9800', '#FFD464'),  # Warning orange → gold
    ('#FF9800', '#FFD464'),  # Warning orange uppercase
    ('#2196f3', '#FF5E5E'),  # Info blue → coral
    ('#2196F3', '#FF5E5E'),  # Info blue uppercase
    ('#e53935', '#FF5E5E'),  # Error darker → coral
    ('#E53935', '#FF5E5E'),  # Error darker uppercase
    ('#ff6b6b', '#FF5E5E'),  # Light red → coral
    ('#FF6B6B', '#FF5E5E'),  # Light red uppercase
    # Gradients
    ('#1A0E3D, #2D1B69', '#B0183D, #E23C64'),
    ('#e91e63, #ff6b6b', '#E23C64, #FF5E5E'),
]

# Apply replacements
for old, new in old_new_colors:
    content = content.replace(old, new)

# Write the file back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully updated color palette in {file_path}")
print("Replacements applied:")
for old, new in old_new_colors:
    print(f"  {old} → {new}")
