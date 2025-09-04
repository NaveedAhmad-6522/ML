text = "  Naveed is learning Python!  "

print(text.upper())       # All caps
print(text.strip())       # Remove outer spaces
print(text.replace("Python", "ML"))  # Replace word
print(text.split())       # Split by spaces



sentence = "   Hello Naveed   "
processing =sentence.strip().replace("Hello","Hi").lower().split()
print(processing)