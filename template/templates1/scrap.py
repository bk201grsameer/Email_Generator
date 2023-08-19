import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.flowrite.com/blog/thank-you-email"

# Fetch the webpage content
response = requests.get(url)
webpage_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(webpage_content, "html.parser")

# Find all the divs with class "div-block-138"
email_divs = soup.find_all("div", class_="div-block-138")

# Extract and print the email templates
print("Extracted Email Templates:")
for email_div in email_divs:
    # Find the title of the email from the preceding h2 tag
    email_title = email_div.find_previous("h3")
    if email_title:
        print("Template Title:", email_title.get_text())

    email_content = email_div.find("div", class_="paragraph-60")
    if email_title:
        if email_content:
            email_text = email_content.get_text().strip()
            print("Email Content:", email_text.strip())
            with open(
                email_title.get_text() + ".txt", "w", encoding="utf-8"
            ) as output_file:
                output_file.write(email_text)
            print("[+] Template Created..")

    print("=" * 30)  # Separate templates with a line of equal signs
    break
