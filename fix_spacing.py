with open("src/components/Description.astro", "r") as f:
    content = f.read()

# Make all section paddings uniform
content = content.replace('class="relative pt-20  bg-black overflow-hidden"', 'class="relative py-20 bg-black overflow-hidden"')
content = content.replace('class="relative pt-20 bg-black overflow-hidden"', 'class="relative py-20 bg-black overflow-hidden"')
content = content.replace('class="relative py-20  bg-black overflow-hidden"', 'class="relative py-20 bg-black overflow-hidden"')

with open("src/components/Description.astro", "w") as f:
    f.write(content)

print("Spacing fixed")
