Cold Email Sequence Generator
This application is a cold email sequence generator designed to automate the process of sending a series of follow-up emails to potential customers. It is particularly useful for sales and marketing teams looking to nurture leads and increase engagement over time. The app uses JSON-based input to customize the content of the emails based on specific customer and product information.

How It Works
JSON Input: The application takes input in the form of a JSON string, which contains details about the customer (e.g., name, company, position, email), product (e.g., name, features, benefits), and a sequence of email templates to be sent over time. Each email template includes placeholders for customer and product information, which are dynamically filled during email generation.

Email Generation: The app processes each email template in the sequence, replacing placeholders with actual data from the JSON input. This allows for personalized emails tailored to the recipient's role, the product's features, and benefits that align with their needs.

Scheduling: Using the schedule library, the application schedules emails to be sent at specified intervals. Each email in the sequence is sent after a set amount of time, allowing for a structured follow-up approach. For testing purposes, a short interval (e.g., 10 seconds) can be used, but in a production environment, this could be set to hours or days.

Sending Emails: A simple send_email function is used to simulate sending emails by printing the email subject and content to the console. In a real-world application, this function could be integrated with an email service to send actual emails.

Tracking and Limits: The application keeps track of the emails sent using a unique identifier for each email (subject and content). This prevents duplication and ensures that each email in the sequence is only sent once. A maximum number of emails to send is specified to control the overall number of emails sent during each run.

Features
Dynamic Content Personalization: Emails are personalized based on customer and product information, making them more relevant and engaging.
Automated Scheduling: Automatically schedules and sends emails at specified intervals, reducing manual effort and ensuring timely follow-ups.
Scalability: Can handle multiple email sequences and different customer-product combinations by modifying the JSON input.
Simple Integration: Uses standard Python libraries (json, schedule, datetime, etc.) for easy integration into existing workflows.
Usage
Prepare JSON Input: Define the customer, product, and email sequence details in a JSON string format.
