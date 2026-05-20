'''
Author:     Bharat Dhuva
LinkedIn:   https://www.linkedin.com/in/bharatdhuva27/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/bharatdhuva

Support me: https://github.com/sponsors/GodsScion

version:    26.01.20.5.08
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "Bharat_Dhuva_Resume.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "1"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = ""                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/bharatdhuva27/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Other"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 1200000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 0            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 0                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Software Engineering Student & Ex-Intern at YV Thinkers | React.js, Node.js, Python, ASP.NET Core" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
Third-year CS student at MS University Baroda building production-grade platforms independently. 
Strong in clean architecture, SOLID principles, REST APIs, and real-time systems.

Key Projects:
- InterviewOS: Real-time collaborative interview platform using WebRTC, Socket.IO, Y.js, Judge0 API, and Monaco Editor.
- Outly: AI-powered career automation tool with GPT-4, Gmail API, and Redis/Bull Queue.
- Bookstage: Full-stack ticket booking system using ASP.NET Core, SQL Server, and Docker.

Experience:
- Software Development Intern at YV Thinkers (MERN Stack, JWT authentication, MongoDB).
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I am a Software Engineering student at The Maharaja Sayajirao University of Baroda, with hands-on experience as a Software Development Intern at YV Thinkers and a strong track record of building production-grade platforms independently.

My expertise includes JavaScript, React.js, Node.js, Python, and ASP.NET Core. I have built real-time systems like InterviewOS (collaborative interview platform using WebRTC, Socket.IO, and Y.js CRDTs), AI-powered tools like Outly (integrating GPT-4, Gmail API, and Redis distributed queues), and high-performance backends. I am passionate about writing clean, maintainable code adhering to SOLID principles and clean architecture.

I am excited about the opportunity to contribute my technical skills and enthusiasm to your team. Thank you for your time and consideration.

Sincerely,
Bharat Dhuva
bharatdhuva27@gmail.com | +91-9624828661
"""
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all ="""
BHARAT DHUVA
Contact: +91-9624828661 | bharatdhuva27@gmail.com | Vadodara, Gujarat, India
LinkedIn: https://www.linkedin.com/in/bharatdhuva27/
GitHub: https://github.com/bharatdhuva

Summary:
Third-year CS student at MS University Baroda building production-grade platforms independently. Built InterviewOS (WebRTC + Y.js CRDT collaborative interview platform), Outly (GPT-4 career automation + Gmail API + Redis queue), and Bookstage (ASP.NET Core ticket booking + seat locking engine). Ex-intern at YV Thinkers. Strong in clean architecture, SOLID principles, REST APIs, and real-time systems.

Education:
- Bachelor of Engineering in Computer Science & Engineering (2024 - 2027)
  The Maharaja Sayajirao University of Baroda, Vadodara (Expected Graduation: May 2027)
- Diploma in Computer Engineering (2021 - 2024)
  (GTU) Government Polytechnic, Jamnagar (CGPA: 7.51)

Experience:
Software Development Intern | YV Thinkers (Jul 2023 - Sep 2023, Onsite)
- MERN | REST APIs | JWT | MongoDB
- Built full-stack CRM using MERN stack for Admin and Customer-facing workflows.
- Implemented role-based JWT authentication with dual-token strategy and clean architecture.
- Automated customer record lifecycle via MongoDB aggregation pipelines (reduced manual data entry by ~70%).

Projects:
- InterviewOS - Real-Time Interview Platform (Nov 2025 - Present)
  React.js, Node.js, MongoDB, WebRTC, Socket.IO, Y.js, Judge0, Monaco Editor
  - WebRTC P2P video, Y.js CRDT collaborative editor, shared whiteboard, Socket.IO.
  - Judge0 API integration for sandboxed code execution, built tab-switch/paste proctoring.
- Outly - AI-Powered Career Automation (Jan 2026 - Present)
  React.js, Node.js, Gmail API, Redis, Bull Queue, GPT-4, OAuth 2.0
  - LLM pipeline using GPT-4 for company research and cold email drafts via Gmail API.
  - Bull + Redis distributed job queue and Telegram bot scheduler.
- Bookstage - Full-Stack Ticket Booking (Feb 2026 - Apr 2026)
  React.js, ASP.NET Core, SQL Server, Docker, JWT, REST API
  - Seat locking engine (5-min expiry) and modular REST API with JWT auth and Docker deployment.

Technical Skills:
- Languages: JavaScript, Java, Python, SQL, C#
- Web & Frameworks: React.js, Node.js, Express.js, ASP.NET Core, REST APIs, Socket.IO, WebRTC
- Databases: MongoDB, PostgreSQL, MySQL, Redis, SQL Server
- AI & APIs: GPT-4, Groq API, Judge0, Gmail API, OAuth 2.0, JWT
- DevOps & Tools: Git, GitHub, Docker, Postman, CI/CD, Bull Queue
- CS Fundamentals: DSA, SOLID Principles, Clean Architecture, OOP, System Design (basics)
"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "YV Thinkers" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "8"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''
############################################################################################################