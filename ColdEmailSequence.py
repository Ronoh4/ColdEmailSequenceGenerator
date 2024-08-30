# Import Modules
import json
import schedule
import time
from datetime import datetime

# Example JSON Input 
json_input = '''{
  "customer": {
    "name": "Phil Kip",
    "company": "Sycular",
    "position": "CTO",
    "email": "ceophil@sycular.com"
  },
  "product": {
    "name": "NVIDIA H200 GPUs",
    "features": ["141GB of HBM3e Memory", "4.8 TB/s Memory Bandwidth", "Enhanced AI and HPC Performance"],
    "benefits": ["Accelerated Generative AI and LLMs", "Improved Energy Efficiency", "Faster Scientific Computing"]
  },
  "sequence": [
    {
      "day": 1,
      "subject": "1st Email - Introducing you to NVIDIA H200 GPUs Public Beta",
      "template": "\\n\\nHi {name},\\n\\nI wanted to introduce you to the new and much waited {product_name}, particularly its key feature: '{features[0]}' which can help you with {benefits[0]}. Sign up for the public preview beta and try it out!\\n\\nBest regards,\\nNVIDIA"
    },
    {
      "day": 2,
      "subject": "2nd Email - Follow-up on NVIDIA H200 GPUs Public Beta",
      "template": "\\n\\nHi {name},\\n\\nJust checking in to see if you had a chance to look at {product_name} and its feature of '{features[0]}'. Today I am following up with another cool feature: '{features[1]}' which can help you with {benefits[1]}. Try this out as well!\\n\\nBest Regards,\\nNVIDIA"
    },
    {
      "day": 3,
      "subject": "3rd Email - Final Reminder about NVIDIA H200 GPUs Public Beta",
      "template": "\\n\\nHi {name},\\n\\nI just wanted to send one last reminder about {product_name} which is currently still on public beta. Don't miss out on another cool feature: '{features[2]}' which is best for {benefits[2]}. Try it out before the beta window lapses!\\n\\nBest Regards,\\nNVIDIA"
    }
  ]
}'''

# Parse JSON Input
data = json.loads(json_input)

# Function to Generate Email Content
def generate_email(template, customer, product):
    try:
        email_content = template.format(
            name=customer['name'],
            product_name=product['name'],
            features=product['features'],
            benefits=product['benefits']
        )
    except KeyError as e:
        print(f"KeyError: {e} in template: {template}")
        raise
    return email_content

customer = data['customer']
product = data['product']
sequence = data['sequence']

emails = []

# Generate Emails Based on the Sequence
for email in sequence:
    email_content = generate_email(email['template'], customer, product)
    emails.append({
        "day": email['day'],
        "subject": email['subject'],
        "content": email_content
    })

# Function to Send Email 
def send_email(email):
    print(f"Subject: {email['subject']}")
    print(email['content'])
    print("\n---\n")

# I used 10 seconds interval to Schedule Emails for Testing
start_time = datetime.now()

# Keep track of emails sent with unique identifiers to avoid duplication
emails_sent = set()
emails_sent_count = 0
max_emails_to_send = 3

def get_email_identifier(email):
    return (email['subject'], email['content'])

def schedule_email(e=email):
    global emails_sent_count
    if emails_sent_count < max_emails_to_send:
        if get_email_identifier(e) not in emails_sent:
            send_email(e)
            emails_sent.add(get_email_identifier(e))
            emails_sent_count += 1
            if emails_sent_count >= max_emails_to_send:
                return schedule.CancelJob

# Schedule each email to be sent every 10 seconds
for i, email in enumerate(emails):
    schedule.every(10 * (i + 1)).seconds.do(schedule_email, e=email)

# Run Scheduler in the background to check every second)
while True:
    schedule.run_pending()
    time.sleep(1)
    if emails_sent_count >= max_emails_to_send:
        break
