tag,word = input("\nEnter tag and word : ").split()

html_string = f"<{tag}>{word}</{tag}>"
print(html_string)