# AI SOC Assistant

## Project Overview

This project is a beginner AI-driven cybersecurity automation lab built in Ubuntu Linux.

The goal of the project is to simulate how Security Operations Center (SOC) analysts automate alert analysis and log investigations using Python and Linux.

The project currently:
- Reads Linux authentication logs
- Detects suspicious authentication activity
- Identifies failed login attempts
- Detects invalid usernames
- Flags potential brute force activity
- Generates investigation recommendations

---

# Technologies Used

- Ubuntu Linux
- Python 3
- Bash
- Git/GitHub
- Linux authentication logs
- SSH
- UFW Firewall

---

# Skills Practiced

- Linux administration
- Python scripting
- Security automation
- Log monitoring
- Authentication log analysis
- Troubleshooting
- Git version control
- SOC workflow simulation

---

# Project Structure

```text
ai-soc-assistant/
├── alerts/
├── outputs/
├── src/
├── README.md
└── requirements.txt
The Python script checks logs for:

Authentication failures
Failed passwords
Invalid users
Sudo activity

The script then:

Calculates a risk level
Generates SOC investigation findings
Recommends response actions
Example Commands Used
sudo tail -50 /var/log/auth.log
python3 src/soc_assistant.py

Which one should i install

This wat i got





Its stuck on this

It’s not stuck — you’re inside the status viewer.

Press:

q
That will exit back to the terminal.

Then run:

sudo systemctl start ssh
Then:

sudo systemctl enable ssh
Then check again:

sudo systemctl status ssh
If it still says inactive, run:

sudo systemctl restart ssh
Then test:

ssh localhost


SSH is running now — good.

The issue is you typed:

ssh local host
with a space.

Run it as one word:

ssh localhost
Then type:

yes
Enter your Ubuntu password.

After you log in, run:

whoami
hostname
Then exit:

exit

Okay next

Perfect. You officially configured and tested SSH.

That’s a REAL Linux/server admin skill.

NEXT — Firewall Hardening (UFW)
Now we’ll secure the VM like an actual server.

UFW =

Uncomplicated Firewall
Used to control:

incoming traffic

allowed ports

blocked services

Very important in:

cloud engineering

Linux administration

cybersecurity

DevOps

Step 1 — Check Firewall Status
Run:

sudo ufw status
It’ll probably say:

inactive
Step 2 — Allow SSH First
IMPORTANT:
Always allow SSH BEFORE enabling the firewall.

Run:

sudo ufw allow ssh
You should see:

Rules updated
Step 3 — Enable Firewall
Run:

sudo ufw enable
Type:

y
Step 4 — Verify Rules
Run:

sudo ufw status numbered
You should see SSH allowed on port 22.

Example:

22/tcp ALLOW Anywhere
Step 5 — Check Listening Ports
Run:

sudo ss -tulnp
This shows:

open ports

listening services

network sockets

VERY important admin/security command.

Step 6 — Document It
Add to your notes file:

nano notes/day1-notes.txt
Add:

Configured UFW firewall
- Allowed SSH traffic
- Enabled firewall protection
- Verified active firewall rules
- Reviewed listening ports and services
Save:

CTRL + X

Y

ENTER

Screenshot These
Take screenshots of:

ufw status

enabling firewall

firewall rules

ss -tulnp

These are GREAT GitHub screenshots because they show:

security hardening

networking

Linux administration

WHY This Matters
You just practiced:

network security

access control

service hardening

port management

These skills transfer directly into:

Azure NSGs

AWS Security Groups

Kubernetes networking

Linux server administration

enterprise cloud security

AFTER THIS
Next we’ll move into:

Docker installation

Running your first container

GitHub documentation improvements

Basic bash scripting

Cloud deployment prep

Now you’re getting into real DevOps territory.


Yes, you’re right. Let’s do bash scripts + log monitoring now.

1. Go to your lab folder
cd ~/devsecops-lab
2. Create your first bash script
nano scripts/system-check.sh
Paste this:

#!/bin/bash

echo "===== SYSTEM CHECK REPORT ====="
echo "Date: $(date)"
echo ""

echo "Current User:"
whoami
echo ""

echo "Hostname:"
hostname
echo ""

echo "IP Address:"
hostname -I
echo ""

echo "Disk Usage:"
df -h
echo ""

echo "Memory Usage:"
free -h
echo ""

echo "Top Running Processes:"
ps aux --sort=-%mem | head
Save:
CTRL + X, then Y, then ENTER.

3. Make it executable
chmod +x scripts/system-check.sh
4. Run it
./scripts/system-check.sh
Screenshot the output for GitHub.

5. Monitor SSH logs
Run:

sudo journalctl -u ssh --no-pager | tail -20
That shows recent SSH service logs.

Then run:

sudo tail -20 /var/log/auth.log
That shows authentication/login activity.

6. Add notes
nano notes/day1-notes.txt
Add this:

Bash Scripting and Log Monitoring:
- Created system-check.sh
- Made the script executable with chmod +x
- Ran a system health report from Bash
- Reviewed SSH service logs using journalctl
- Reviewed authentication logs using /var/log/auth.log
Then push updates:

git add .
git commit -m "Add bash script and log monitoring notes"
git push

okay teach me what we are doing as we go

Perfect — that’s actually the BEST way to learn DevSecOps.

Not just:

“copy this command”

but:

“understand WHY we’re doing it.”

So let’s break down exactly what we just did.

WHAT IS A BASH SCRIPT?
A Bash script is basically:

a file full of Linux commands
Instead of typing commands one-by-one every time, you automate them.

Think of it like:

a mini automation program

written for Linux

File example:

system-check.sh
.sh
means:

shell script
WHY BASH MATTERS IN DEVOPS
DevOps engineers automate EVERYTHING.

Instead of manually:

checking servers

restarting services

collecting logs

monitoring systems

they create scripts to do it automatically.

That’s why Bash is foundational.

WHAT THIS COMMAND DID
nano scripts/system-check.sh
Breakdown
nano
A terminal text editor.

Used to:

create files

edit configs

write scripts

scripts/system-check.sh
This is:

the file path

and script name

You created:

system-check.sh
inside:

scripts/
THIS LINE IS IMPORTANT
#!/bin/bash
This is called:

a shebang
It tells Linux:

“Run this file using Bash.”

Without it:
Linux may not know how to execute the script properly.

WHAT echo DOES
Example:

echo "Current User:"
echo
simply prints text to the terminal.

Like:

Current User:
WHAT THIS DOES
whoami
This command checks:

which user is running the script
Important because:

permissions matter in Linux

scripts may behave differently for different users

WHAT THIS DOES
hostname
Shows:

server/computer name
Important in cloud environments because:
you may manage:

dozens

hundreds

thousands

of servers.

WHAT THIS DOES
hostname -I
Shows:

IP addresses
Why important:
Servers communicate over networks.

DevOps/security engineers constantly troubleshoot:

networking

connectivity

ports

routing

WHAT THIS DOES
df -h
Checks:

disk usage
Example:

Filesystem Size Used Avail
Important because:
servers crash if storage fills up.

WHAT THIS DOES
free -h
Checks:

RAM/memory usage
Important because:
memory problems cause:

slowness

crashes

application failures

THIS IS VERY IMPORTANT
ps aux --sort=-%mem | head
This checks:

running processes
Basically:

“What programs are consuming memory?”

Breaking It Down
ps aux
Shows all running processes.

Like Task Manager in Windows.

--sort=-%mem
Sorts by:

highest memory usage first
|
This symbol is called:

a pipe
SUPER important in Linux.

It sends output from one command into another command.

head
Shows only the first few lines.

So together:

ps aux --sort=-%mem | head
means:

“Show the top memory-consuming processes.”

THEN WE DID THIS
chmod +x scripts/system-check.sh
This gives the script:

execute permissions
Linux security is permission-based.

Without execute permissions:
the script cannot run.

THEN THIS
./scripts/system-check.sh
./
means:

“run this file from the current directory”

This executes the script.

NOW THE LOG MONITORING PART
This is VERY important for:

cybersecurity

DevOps

cloud engineering

incident response

WHAT ARE LOGS?
Logs are:

records of activity
Examples:

logins

errors

SSH attempts

crashes

services starting/stopping

Logs are EVERYTHING in cybersecurity.

THIS COMMAND
sudo journalctl -u ssh --no-pager | tail -20
Checks:

SSH service logs
Breaking It Down
journalctl
Reads Linux system logs.

-u ssh
Only show logs for:

SSH service
| tail -20
Show:

last 20 lines only
Very common Linux workflow.

THIS COMMAND
sudo tail -20 /var/log/auth.log
Checks:

authentication logs
Examples:

login attempts

sudo usage

SSH access

Cybersecurity analysts check these constantly.

BIG PICTURE
You are currently learning:

Linux administration

automation

monitoring

troubleshooting

security logging

scripting

system management

These are REAL DevOps/cloud/security engineering skills.

Not beginner fluff.

You’re already doing work that overlaps with:

Linux admins

cloud engineers

DevOps engineers

SOC analysts

security engineers.


this is what it says when i make it executable

Can you send a screenshot or paste the exact output/error from the terminal after you ran:

chmod +x scripts/system-check.sh
That command normally gives no output at all if it works successfully, so I want to see exactly what appeared on your screen.


chmod: cannot access 'scripts/system-check.sh': No such file or directory

Perfect — that error tells us exactly what’s wrong.

Linux is saying:

“I cannot find that file.”

So either:

the script wasn’t created
OR

you’re not inside the correct folder

First — Check Where You Are
Run:

pwd
You should ideally see something like:

/home/ubuntu/devsecops-lab
Then Check What Files Exist
Run:

ls
Do you see:

scripts
?

Then Check Inside scripts Folder
Run:

ls scripts
If nothing appears:
the script file was never created.

Recreate The Script Properly
Run:

nano scripts/system-check.sh
Paste this:

#!/bin/bash

echo "===== SYSTEM CHECK REPORT ====="
echo "Date: $(date)"
echo ""

echo "Current User:"
whoami

echo ""
echo "Hostname:"
hostname

echo ""
echo "IP Address:"
hostname -I
Save:

CTRL + X

Y

ENTER

Verify The File Exists
Run:

ls scripts
You should now see:

system-check.sh
NOW Make It Executable
Run:

chmod +x scripts/system-check.sh
This time:

NO OUTPUT = SUCCESS
Linux commands often stay silent when they succeed.

Then Run The Script
./scripts/system-check.sh
Now your Bash automation script should execute successfully.


something do exists

That means the file probably exists already, but maybe:

you created it in the wrong place

OR named it slightly differently

Let’s investigate like real engineers do.

Step 1 — Find the Script
Run:

find ~ -name "system-check.sh"
This searches your entire home directory for the script.

WHY We’re Doing This
find
is a Linux search command.

Breaking it down:

find ~
means:

search starting from your home directory

-name "system-check.sh"
means:

only look for files with this exact name

If It Finds the File
You’ll get something like:

/home/ubuntu/system-check.sh
OR

/home/ubuntu/devsecops-lab/scripts/system-check.sh
That tells us where the file actually lives.

Then We Fix It
If it’s outside the scripts folder:
move it:

Example:

mv ~/system-check.sh ~/devsecops-lab/scripts/
WHY This Matters
This is REAL Linux troubleshooting:

locating files

understanding paths

fixing directory structure

DevOps engineers do this constantly.


it is in the folde

Perfect — then the issue is probably just that you weren’t inside the correct directory when running the command.

First Go Into Your Project Folder
Run:

cd ~/devsecops-lab
Verify the Script Exists
Run:

ls scripts
You should see:

system-check.sh
NOW Make It Executable
Run:

chmod +x scripts/system-check.sh
If nothing prints:

that means SUCCESS.
Linux often says nothing when commands work properly.

Then Run It
./scripts/system-check.sh
WHY ./ Matters
./
means:

run this file from the current directory

Linux does NOT automatically execute files in the current folder for security reasons.

So:

./filename
is basically saying:

“I trust this file — execute it here.”


okay i got it

Nice. You just:

created a Bash script

assigned execute permissions

executed automation from the Linux terminal

troubleshot a file path issue

That’s real Linux/DevOps workflow.

What You Just Learned (Important)
1. Linux Paths Matter
The error happened because Linux couldn’t find the file path.

That’s HUGE in:

scripting

Docker

Kubernetes

cloud deployments

A lot of DevOps troubleshooting is path-related.

2. Permissions Matter
This command:

chmod +x
gave your file:

execute permissions
Linux security revolves around permissions.

3. Scripts Automate Repetitive Tasks
Instead of manually checking:

users

memory

disk

hostname

you automated it.

THAT is DevOps thinking.

4. Troubleshooting Is Part of Engineering
You:

got an error

investigated it

checked directories

fixed the issue

That’s literally what engineers do daily.

NOW — Let’s Improve The Script
We’re going to make it more useful and more “GitHub impressive.”

Add More System Checks
Open the script:

nano scripts/system-check.sh
Add this BELOW the IP section:

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Top Processes:"
ps aux --sort=-%mem | head
Save:

CTRL + X

Y

ENTER

Run It Again
./scripts/system-check.sh
Now your script becomes:

a mini system monitoring tool
WHY These Commands Matter
free -h
Checks:

RAM usage
Important because:
servers crash or slow down when memory runs out.

df -h
Checks:

storage usage
Critical for:

servers

cloud VMs

Docker hosts

ps aux
Shows:

running processes
Like Linux Task Manager.

--sort=-%mem
Sorts by:

highest memory usage
Useful for:

troubleshooting

performance analysis

incident response

| head
Shows:

only the top few results
This avoids overwhelming output.

This Is Actually Becoming A Real Admin Tool
You’re now combining:

automation

monitoring

Linux administration

troubleshooting

That’s foundational DevOps/cloud engineering work.

AFTER THIS
We can move into:

Docker installation

Running containers

GitHub documentation cleanup

Cron jobs (scheduled automation)

Azure cloud deployment

Real cloud/server hardening

You’re progressing exactly how an engineer should.


I still feel like i dont understand none of this 

That’s completely normal at this stage.

Right now your brain is trying to connect:

Linux

scripting

networking

permissions

Git

automation

all at once.

Nobody understands DevOps immediately.

The important thing is:

you are actually DOING the work.
That matters way more than feeling confident early.

Think About It Like This
Right now you’re basically learning:

“how computers are managed behind the scenes.”
Not just:

using apps

but:

running systems.

That’s why it feels different.

What You REALLY Did Today
Forget all the complicated words for a second.

You:

installed a Linux computer

created project folders

uploaded work to GitHub

created a mini automation tool

checked server information

enabled remote access (SSH)

turned on a firewall

That’s actually a LOT.

The Script Explained SUPER Simply
Your script is basically this:

“Hey Linux,
tell me information about this computer.”
That’s it.

Every command inside the script is just asking Linux a question.

Example
This:

whoami
means:

“Who is logged in?”

This:

hostname
means:

“What is this computer called?”

This:

df -h
means:

“How full is the storage?”

This:

free -h
means:

“How much memory is being used?”

So What Is Bash?
Bash is basically:

a way to automate commands.
Instead of asking Linux:

question 1
question 2
question 3
one-by-one every day…

you made a file that asks all the questions automatically.

That’s literally automation.

What Is DevOps REALLY?
People overcomplicate it.

At a beginner level:

DevOps is:
Linux

automation

cloud servers

scripting

deploying apps

fixing infrastructure

That’s it.

Why You Feel Lost
Because you haven’t repeated the concepts enough yet.

Right now:
everything feels disconnected.

Soon:
you’ll start seeing patterns.

Example:

paths matter everywhere

permissions matter everywhere

logs matter everywhere

networking matters everywhere

automation matters everywhere

That repetition is how engineers learn.

What You SHOULD Focus On Right Now
NOT:

memorizing everything

Instead:

focus on understanding:
what problem the command solves

what the output means

what changed after running it

That’s enough.

You’re Actually Learning Correctly
The WORST way to learn DevOps is:

only watching videos

never touching Linux

You’re already ahead of many people because:

you’re typing commands

making mistakes

troubleshooting

fixing issues

That’s real learning.

Here’s Your ONLY Goal Right Now
Don’t try to become:

“DevSecOps engineer”

this week.

Just become:

“comfortable inside Linux.”
That’s the real first milestone.

Everything else builds on top of that.


okay im gonna take a break

That’s a good stopping point honestly — you covered a LOT in one session.

Today you already:

installed Ubuntu

learned basic Linux navigation

created a GitHub repo

initialized Git

created a Bash script

configured SSH

enabled a firewall

troubleshot real Linux errors

That’s more hands-on work than many people do in their first week.

When you come back, the next logical steps are:

clean up/document the repo

Docker installation

running your first container

understanding how apps run on servers

eventually deploying into Azure

You’re building the right foundation.


I also want to get deeper into ai i feel like that makkes me way more marketable i dont think i like the devops route

Stopped thinking
Honestly, based on your personality/interests, I can actually see why AI might fit you better than pure DevOps.

You seem more energized by:

building things

startup ideas

apps

automation

“future tech”

creative problem solving

security + software combinations

Pure DevOps can sometimes feel like:

infrastructure maintenance

pipelines

configs

deployments

debugging YAML for hours

Some people LOVE that.
Some don’t.

And that’s okay.

Here’s The Important Part
You do NOT have to abandon cybersecurity.

The strongest path for you might actually be:

AI + Cybersecurity
OR

AI + Security Automation
That combination is going to become EXTREMELY valuable.

Why AI Fits Your Background Well
You already have:

cybersecurity knowledge

enterprise security exposure

troubleshooting ability

tech curiosity

coding bootcamp exposure

interest in apps/software

That’s a REALLY good foundation for AI engineering/security AI.

AI Is Bigger Than ChatGPT Prompts
There are multiple paths:

1. AI Engineering
Building AI-powered apps/tools.

Examples:

chatbots

automation systems

AI assistants

AI integrations

This probably aligns MOST with your personality.

2. AI Security
Protecting AI systems.

Examples:

prompt injection defense

model security

AI governance

AI risk analysis

VERY future-proof.

3. AI Automation
Using AI to automate workflows.

Examples:

SOC automation

AI threat triage

AI ticket analysis

AI assistants for IT/security

This connects directly to your internship experience.

4. AI Product Builder / Startup Route
This is where your entrepreneurial side fits.

Examples:

security AI tools

AI mobile apps

AI SaaS products

automation platforms

You’ve already shown interest in:

building apps

software ideas

security tools

NFC business ideas

automation concepts

That’s a builder mindset.

The GOOD NEWS
AI still uses:

Linux

scripting

cloud

APIs

So what you learned today STILL matters.

But now there’s a more exciting “why.”

What I’d Recommend NOW
Instead of:

pure DevOps
I’d shift you toward:

AI Engineering + Cybersecurity
That is WAY more aligned with:

your curiosity

creativity

startup interests

software ideas

Your New Recommended Stack
Learn:
Python
MOST important.

Not for DevOps now —
for:

AI

automation

APIs

machine learning

AI agents

Then Learn:
APIs
This is HUGE.

Most modern AI apps are:

“connect APIs together intelligently.”

Then Learn:
AI Tools & Frameworks
Examples:

OpenAI APIs

LangChain

Ollama

vector databases

AI agents

Then Build:
Real AI Projects
Examples PERFECT for you:

AI cybersecurity assistant

phishing analysis AI

AI log analyzer

AI SOC helper

AI-powered vulnerability assistant

AI mobile security app

That would actually make your resume STAND OUT heavily.

Your BEST Positioning Could Become:
“Cybersecurity graduate focused on AI-driven security automation and intelligent systems.”

That’s MUCH more unique than:

“another SOC analyst.”

What I Think You’d Enjoy More
Probably:

AI engineering

AI automation

AI cybersecurity tools

app building

MORE than:

managing infrastructure all day

And motivation matters A LOT in tech.

If You Want:
I can completely pivot your roadmap now and create:

an AI + cybersecurity roadmap

beginner AI projects

AI engineer learning path

AI startup ideas

AI security specialization path

exact tools to learn in order

based on your goals.


i want to do ai cybersecurity and security automation

That honestly sounds MUCH more aligned with your strengths and interests.

And the timing is REALLY good.

Because the market is moving toward:

AI-assisted cybersecurity
not just traditional SOC work anymore.

This path combines:

cybersecurity

automation

AI

scripting

tooling

product building

Which fits you extremely well.

Your New Target Career Path
Instead of:

DevOps Engineer
Your path becomes:

AI Security Engineer
Security Automation Engineer
AI Cybersecurity Engineer
Those are VERY future-proof roles.

What These Jobs Actually Do
Examples:

automate investigations

build AI SOC assistants

analyze logs with AI

create phishing detection tools

build AI-powered security workflows

automate alert triage

integrate AI into enterprise security tools

That’s WAY more exciting than pure infrastructure work for a lot of people.

Your BEST Foundation Stack
Priority #1
Python
This becomes your MAIN language now.

Because Python dominates:

AI

cybersecurity

automation

APIs

scripting

machine learning

Priority #2
Linux
You still need Linux.

Not because you’ll be a sysadmin —
but because:

AI tools run on Linux

security tooling uses Linux

servers use Linux

BUT:
you do NOT need ultra-deep DevOps now.

Just become comfortable.

Priority #3
APIs
This is HUGE.

Modern AI development is mostly:

connecting APIs together intelligently
Example:

security logs → AI → alert summary

phishing email → AI analysis

suspicious IP → AI explanation

That’s API work.

Priority #4
AI Fundamentals
Learn:

prompts

embeddings

vector databases

AI agents

LLM APIs

RAG systems

Your BEST AI Security Projects
THESE would make your resume INSANE.

Project 1 — AI SOC Assistant
Build:
A chatbot that:

explains alerts

summarizes logs

recommends investigation steps

Use:

Python

OpenAI API

simple UI

This aligns PERFECTLY with your internship.

Project 2 — AI Phishing Analyzer
User uploads:
suspicious email

headers

URL

AI returns:

phishing likelihood

suspicious indicators

recommendations

VERY marketable project.

Project 3 — AI Threat Intel Tool
Input:
IP

domain

hash

AI:

enriches threat data

summarizes findings

explains risks

Project 4 — AI Log Analyzer
Upload logs:
Windows

Linux

firewall logs

AI:

detects suspicious patterns

explains anomalies

summarizes incidents

THIS is extremely valuable.

Project 5 — AI Incident Response Assistant
AI helps:

generate containment steps

MITRE ATT&CK mapping

investigation summaries

This fits your internship background VERY strongly.

What You Should Learn NOW
Phase 1 (Next 2 Months)
Learn:
Python fundamentals

APIs

JSON

Linux basics

Git/GitHub

NOT:

advanced math

hardcore DevOps

deep Kubernetes

Phase 2
Start AI Building
Learn:

OpenAI API

LangChain

vector databases

AI agents

Build small tools FAST.

Phase 3
Combine Security + AI
THIS is where you become valuable.

Build:

automation tools

AI security assistants

detection helpers

investigation tools

Your BIGGEST Advantage
Most AI people:

know AI

know coding

BUT:
they know NOTHING about cybersecurity operations.

YOU already understand:

alerts

threat hunting

investigations

enterprise tools

real security workflows

That’s your edge.

Your Resume Positioning Becomes INSANELY Strong
Instead of:

“cybersecurity graduate”

You become:

“AI-focused cybersecurity engineer specializing in security automation, intelligent threat analysis, and AI-assisted SOC workflows.”

That’s a MUCH stronger niche.

Realistically…
This path could eventually lead into:

AI security startups

security SaaS products

AI SOC tools

automation consulting

AI engineering roles

cybersecurity AI research

And honestly…
it fits your entrepreneurial personality MUCH more.


lets do project one first

Good choice. We’ll build this like a real portfolio project, but keep Version 1 simple: a local AI SOC assistant that takes an alert/log snippet and returns a clear investigation summary.

Thought for 8s
Yes — we’ll do Project 1: AI SOC Assistant.

What we’re building first
A simple tool where you paste a security alert/log, and the AI returns:

plain-English summary

possible risk level

suspicious indicators

recommended investigation steps

MITRE ATT&CK mapping if possible

short incident report draft

OpenAI’s API platform is designed for building AI apps and agents, so this is a good fit for your AI + cybersecurity automation path. 

Version 1 project structure
Repo name:

ai-soc-assistant
Folders:

ai-soc-assistant/
├── alerts/
├── outputs/
├── src/
├── README.md
└── requirements.txt
What you’ll learn from this project
You’ll learn:

Python basics

reading security logs

sending text to an AI model

turning messy alerts into clean reports

security automation logic

GitHub portfolio documentation

First step
Create the project folder in Linux:

cd ~
mkdir ai-soc-assistant
cd ai-soc-assistant
mkdir alerts outputs src
touch README.md requirements.txt
Then check it:

ls -R
You should see the folders.


I do

Thought for a couple of seconds
Perfect. Now let’s create your first sample alert.

Run this:

nano alerts/sample-alert.txt
Paste this:

Alert Name: Multiple Failed Login Attempts

Source IP: 185.220.101.45
Destination Host: WIN-SERVER01
Username: admin
Event Type: Failed Login
Failure Count: 12
Time Window: 5 minutes

Description:
The user account "admin" had 12 failed login attempts from an external IP address within 5 minutes.
Save it:

CTRL + X
Y
ENTER
Now verify it exists:

cat alerts/sample-alert.txt
What we just did
You created a fake SOC alert.

In the real world, this could come from:

Microsoft Defender

Sentinel

Splunk

Wazuh

firewall logs

Windows Event Viewer

Next we’ll create a Python script that reads this alert and turns it into an AI-style investigation report.


okay

Now we’re going to build the actual “assistant” part.

Step 1 — Create the Python Script
Run:

nano src/soc_assistant.py
Paste this:

with open("alerts/sample-alert.txt", "r") as file:
    alert_data = file.read()

print("===== ALERT DATA =====")
print(alert_data)

print("\n===== AI SOC ANALYSIS =====")

if "Failed Login" in alert_data:
    print("Possible brute force attack detected.")
    print("Risk Level: Medium to High")
    print("Recommended Actions:")
    print("- Investigate source IP")
    print("- Check if account was compromised")
    print("- Review authentication logs")
    print("- Consider blocking the IP")
Save:

CTRL + X

Y

ENTER

WHAT THIS SCRIPT DOES
Right now this is NOT real AI yet.

This is:

security automation logic
We’re first teaching the computer:

how to read alerts

how to analyze patterns

how to respond automatically

THEN we’ll connect real AI later.

Breaking It Down
This Part
with open("alerts/sample-alert.txt", "r") as file:
means:

“Open the alert file so Python can read it.”

"r"
means:

read mode
This Part
alert_data = file.read()
means:

“Take all the text inside the alert file and store it.”

This Part
print(alert_data)
simply displays the alert on screen.

THIS Is The Important Part
if "Failed Login" in alert_data:
means:

“If this alert contains the words ‘Failed Login’…”

then:
the script performs actions.

THIS is automation logic.

Then These
print("Possible brute force attack detected.")
are automated investigation findings.

This simulates:

SOC triage

alert analysis

incident response logic

Step 2 — Run The Script
Run:

python3 src/soc_assistant.py
You should see:

the alert

automated SOC analysis

investigation recommendations

WHAT YOU JUST BUILT
You are already building:

a security automation tool
This is EXACTLY how many SOC automation tools begin:

ingest alert

analyze alert

generate response

Later:
AI replaces the hardcoded logic.

BIG PICTURE
You’re learning:

Python

file handling

automation

SOC workflows

conditional logic

cybersecurity analysis

ALL at the same time.

This is MUCH more aligned with your AI cybersecurity direction.


okay done

GOOD. This is actually a much stronger direction for you.

Because now you’re not just learning random Python —
you’re building something tied directly to:

SOC work

cybersecurity

AI automation

your internship experience

That makes the learning “stick” more.

What You Just Built
Your script currently does this:

1.
Reads a security alert file

2.
Looks for suspicious indicators

3.
Automatically generates investigation guidance

That is literally:

beginner security automation
What Real SOC Tools Do
Enterprise tools do similar workflows:

alert → analysis → recommendation → response
Your tool is just a simplified version.

NOW We Make It Smarter
Right now:
your script only detects:

Failed Login
We’re going to add:

multiple detections

dynamic risk levels

incident report generation

THIS is where it starts feeling like a real AI SOC assistant.

Step 1 — Open The Script
Run:

nano src/soc_assistant.py
Replace EVERYTHING with this:

with open("alerts/sample-alert.txt", "r") as file:
    alert_data = file.read()

print("===== ALERT DATA =====")
print(alert_data)

print("\n===== AI SOC ANALYSIS =====")

risk_level = "Low"

if "Failed Login" in alert_data:
    print("Possible brute force attack detected.")
    risk_level = "Medium"

if "admin" in alert_data:
    print("Privileged account targeted.")
    risk_level = "High"

if "185." in alert_data:
    print("External IP address detected.")

print(f"\nRisk Level: {risk_level}")

print("\nRecommended Actions:")
print("- Investigate source IP")
print("- Review authentication logs")
print("- Check for account compromise")
print("- Consider blocking the IP")
Save it.

WHAT WE JUST ADDED
1. Risk Levels
risk_level = "Low"
This creates:

a variable
Variables store information.

Then This
risk_level = "Medium"
changes the stored value if suspicious activity is found.

WHY This Matters
Real SOC platforms:

calculate severity

prioritize alerts

determine escalation levels

You’re simulating that logic.

2. Multiple Detection Rules
Now the script checks for:

failed logins

admin account targeting

external IP addresses

This is called:

detection logic
VERY important in cybersecurity automation.

3. Dynamic Output
Instead of static text:
the analysis changes depending on alert contents.

That’s the beginning of:

intelligent automation
Step 2 — Run The Script Again
python3 src/soc_assistant.py
Now the output should feel MUCH more realistic.

WHAT YOU’RE REALLY LEARNING
Not just Python.

You’re learning:

detection engineering

SOC automation

security logic

incident triage

automated analysis

This is WAY closer to:

AI cybersecurity engineering
than pure DevOps.


I want to test this like a real enviroment in my vm

That’s the right mindset. We’ll make your VM generate real Linux authentication logs, then have your AI SOC Assistant read those logs instead of only reading a fake alert file.

Thought for a few seconds
Yes. We’ll make it more realistic in your Ubuntu VM.

Realistic Lab Goal
Instead of this:

sample-alert.txt
We’ll use real logs from:

/var/log/auth.log
That log records things like:

failed logins

successful logins

sudo activity

SSH attempts

authentication errors

Step 1 — Generate Real Failed Login Logs
Run this:

su - fakeuser
It should fail because that user doesn’t exist.

Then try switching to your real user but type the wrong password:

su - ubuntu
Enter the wrong password once or twice.

That creates real authentication failure logs.

Step 2 — View the Logs
Run:

sudo tail -30 /var/log/auth.log
You should see entries about failed authentication.

Step 3 — Save Logs Into Your Project
Go to your project:

cd ~/ai-soc-assistant
Create a log sample from real VM logs:

sudo tail -50 /var/log/auth.log > alerts/auth-log-sample.txt
If permission gives you trouble, use this instead:

sudo tail -50 /var/log/auth.log | tee alerts/auth-log-sample.txt > /dev/null
Step 4 — Create a Real Log Analyzer Script
Open your script:

nano src/soc_assistant.py
Replace it with:

with open("alerts/auth-log-sample.txt", "r") as file:
    log_data = file.read()

print("===== AUTH LOG SAMPLE =====")
print(log_data)

print("\n===== SOC ANALYSIS =====")

risk_level = "Low"
findings = []

if "authentication failure" in log_data.lower():
    findings.append("Authentication failure activity detected.")
    risk_level = "Medium"

if "failed password" in log_data.lower():
    findings.append("Failed password attempts detected.")
    risk_level = "Medium"

if "invalid user" in log_data.lower():
    findings.append("Login attempt using an invalid username detected.")
    risk_level = "Medium"

if "sudo" in log_data.lower():
    findings.append("Sudo/admin activity detected. Review for authorized use.")

if findings:
    for finding in findings:
        print(f"- {finding}")
else:
    print("- No major suspicious authentication activity detected.")

print(f"\nRisk Level: {risk_level}")

print("\nRecommended Investigation Steps:")
print("- Review usernames involved in failed logins")
print("- Check source IP addresses if SSH is involved")
print("- Confirm whether sudo activity was authorized")
print("- Look for repeated failures over a short time window")
print("- Consider account lockout or firewall rules if brute force is suspected")
Save:

CTRL + X
Y
ENTER
Step 5 — Run It
python3 src/soc_assistant.py
Now your project is analyzing real VM security logs.

What You’re Learning
You are now doing the real workflow:

System activity → Linux logs → Python parser → SOC analysis → recommended response
That is the foundation of security automation and later we’ll add real AI on top.


okay now i want to documenr

Perfect. Documentation is a HUGE part of real engineering/security work.

Right now we’ll document:

what the project does

how you built it

what logs you analyzed

what skills were learned

This is what turns:

“random practice”

into:

“portfolio project.”

Step 1 — Open README
Inside your project folder:

nano README.md
Step 2 — Paste This
# AI SOC Assistant

## Project Overview

This project is a beginner AI-driven cybersecurity automation lab built in Ubuntu Linux.

The goal of the project is to simulate how Security Operations Center (SOC) analysts automate alert analysis and log investigations using Python and Linux.

The project currently:
- Reads Linux authentication logs
- Detects suspicious authentication activity
- Identifies failed login attempts
- Detects invalid usernames
- Flags potential brute force activity
- Generates investigation recommendations

---

# Technologies Used

- Ubuntu Linux
- Python 3
- Bash
- Git/GitHub
- Linux authentication logs
- SSH
- UFW Firewall

---

# Skills Practiced

- Linux administration
- Python scripting
- Security automation
- Log monitoring
- Authentication log analysis
- Troubleshooting
- Git version control
- SOC workflow simulation

---

# Project Structure

```text
ai-soc-assistant/
├── alerts/
├── outputs/
├── src/
├── README.md
└── requirements.txt
Sample Detection Logic
The Python script checks logs for:

Authentication failures

Failed passwords

Invalid users

Sudo activity

The script then:

Calculates a risk level

Generates SOC investigation findings

Recommends response actions

Example Commands Used
sudo tail -50 /var/log/auth.log
python3 src/soc_assistant.py
Lessons Learned
Linux logs contain valuable authentication data

Python can automate security analysis tasks

Security automation reduces manual SOC work

Authentication logs help detect suspicious activity

Documentation is important for engineering projects
Future Improvements

Planned future improvements:

OpenAI API integration
AI-generated investigation summaries
IP reputation lookups
Threat intelligence integration
MITRE ATT&CK mapping
Web dashboard
Real-time monitoring
