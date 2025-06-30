import re
from bs4 import BeautifulSoup

INDEX_HTML_PATH = "/Users/abhisheksingh/Desktop/zer-0-ne.github.io/index.html"

# Read the content of index.html
with open(INDEX_HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Define the old and new strings
old_string_pattern = r"""<div class=\"content\">\s*<ul class=\"list-unstyled\">\s*<li><i class=\"fa fa-book\"></i> The Master Algorithm</li>.*?</ul>\s*</div><!--//content-->"""

new_string = r"""<ul class=\"list-unstyled\">\n                                    <li><i class=\"fa fa-book\"></i> The Master Algorithm</li>\n                                    <li><i class=\"fa fa-book\"></i> The One thing</li>\n                                    <li><i class=\"fa fa-book\"></i> The Monk who sold his Ferrari</li>\n                                    <li><i class=\"fa fa-book\"></i> The Monk who sold his Ferrari</li>\n                                    <li><i class=\"fa fa-book\"></i> Everything is f*cked: A book about Hope</li>\n                                    <li><i class=\"fa fa-book\"></i> Elon Musk - Biography</li>\n                                    <li><i class=\"fa fa-book\"></i> Life is what you make it</li>\n                                    <li><i class=\"fa fa-book\"></i> The unthethered Soul</li>\n                                    <li><i class=\"fa fa-book\"></i> Revolution 2020</li>\n                                    <li><i class=\"fa-book\"></i> Unstoppable Confidence</li>\n                                    <li><i class=\"fa fa-book\"></i> Ikigai: The Japanese Secret to a Long and Happy Life</li>\n                                    <li><i class=\"fa fa-book\"></i> Essentialism: The Disciplined Pursuit of Less</li>\n                                    <li><i class=\"fa fa-book\"></i> Rich Dad, Poor Dad</li>\n                                    <li><i class=\"fa fa-book\"></i> The Top Five Regrets of The Dying</li>\n                                    <li><i class=\"fa fa-book\"></i> The Alchemist - Paulo Coelho</li>\n                                    <li><i class=\"fa fa-book\"></i> Think and Grow Rich</li>\n                                    <li><i class=\"fa fa-book\"></i> The Habit of Winning - Prakash Iyer</li>\n                                    <li><i class=\"fa fa-book\"></i> Men from Mars, Women from Venus</li>\n                                    <li><i class=\"fa fa-book\"></i> Emotional Intelligence 2.0</li>\n                                    <li><i class=\"fa fa-book\"></i> Man's Search for Meaning</li>\n                                    <li><i class=\"fa fa-book\"></i> Hit Refresh - Satya Nadella</li>\n                                    <li><i class=\"fa fa-book\"></i> Brief Answers to the Big Questions</li>\n                                    <li><i class=\"fa fa-book\"></i> The White Tiger</li>\n                                    <li><i class=\"fa fa-book\"></i> Khaled Hosseini - The Kite Runner</li>\n                                    <li><i class=\"fa fa-book\"></i> Grace - Richard Paul Evans</li>\n                                    <li><i class=\"fa fa-book\"></i> The Subtle Art of Not Giving a Fuck</li>\n                                    <li><i class=\"fa fa-book\"></i> Atomic Habits</li>\n                                    <li><i class=\"fa fa-book\"></i> 12 Rules for Life - Jordan Peterson</li>\n                                    <li><i class=\"fa fa-book\"></i> The Power of your Subconscious Mind</li>\n                                    <li><i class=\"fa fa-book\"></i> Life 3.0</li>\n                                    <li><i class=\"fa fa-book\"></i> The God of Small Things</li>\n                                </ul>"""

# Perform the replacement using re.sub
# re.DOTALL allows . to match newlines
modified_content = re.sub(old_string_pattern, new_string, html_content, flags=re.DOTALL)

# Write the modified content back to the file
with open(INDEX_HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(modified_content)

print("Successfully fixed index.html by removing nested content div.")
