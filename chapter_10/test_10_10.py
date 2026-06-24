from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding = 'utf-8')

num1 = contents.lower().count('the')
num2 = contents.lower().count('the ')
print(f"单词the在全文中出现了{num1}次！")
print(f"单词the 在全文中出现了{num2}次！")