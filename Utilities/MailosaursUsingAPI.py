from datetime import datetime, timedelta
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
from bs4 import BeautifulSoup


class Mailosaurs:

    def getthecode(self):
        # this is assigning your api to an object
        mailosaur = MailosaurClient("g1QBgTUc0o85ea2voY2O711XiRkTpyja")

        # Calculate a datetime for yesterday
        yesterday = datetime.today() - timedelta(days=1)

        # Search criteria for mail
        criteria = SearchCriteria()
        criteria.sent_to = "through-flies@fbivwb1j.mailosaur.net"  # Search using the receiver's mail
        criteria.sent_from = "no-reply@verificationemail.com"  # Search using the sender's mail

        # Use this timestamp in the search
        message = mailosaur.messages.get("fbivwb1j", criteria,received_after=yesterday)  # This will search all the mails from current time to yesterday

        # Let's say 'html_content' contains the HTML response from Mailosaur
        html_content = message.html.body  # From your Mailosaur response
        #print(html_content)

        # Parse the HTML, using Beautifulsoup which will make it look readable
        soup = BeautifulSoup(html_content, "html.parser")

        # Find all <span> tags with bold font style
        forgotpassword_spans = soup.find("span", style=lambda s: s and "font-weight: bold" in s)  # span for forgotpassword html.parser
        newpassword_spans = soup.find_all("span", style=lambda value: value and "font-weight: bold" in value)  # span for newpassword html.parser

        if forgotpassword_spans:
            password = forgotpassword_spans.text.strip()
            return password# strips the code from Span
        else:
            if len(newpassword_spans) >= 2:
                password = newpassword_spans[1].text.strip()
                return password# Strips the password from Span
            else:
                print("Password span not found.")
