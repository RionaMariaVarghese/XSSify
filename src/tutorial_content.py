from tutorial_db import Session, TutorialPageContent

session = Session()
session.query(TutorialPageContent).delete()

content_entries = [
    TutorialPageContent(title="INTRODUCTION",
                        content="\nCross-Site Scripting (XSS) is a vulnerability in web applications that allows attackers to inject malicious scripts into web pages viewed by other users. XSS attacks can lead to various consequences, including data theft, session hijacking, defacement, and malware distribution. This tutorial aims to introduce beginners to XSS, exploitation, commonly used apps vulnerable to XSS, and preventive measures to mitigate this threat."),

    TutorialPageContent(title="UNDERSTANDING", 
                        content="\nXSS occurs when an attacker injects malicious scripts into web applications, which are then executed in the broswers of unsuspecting users.\nThere are three main types of XSS:\n\n1. Reflected XSS: \nThe injected script is reflected off a web server and executed in the user's browser.\n\n2. Stored XSS: \nThe injected script is stored on the server and executed whenever a user accesses the affected page.\n\n3. DOM-based XSS: \nThe payload is injected into the DOM (Document Object Model) and executed in the victim's browser."),

    TutorialPageContent(title="Common apps/websites vulnerable to XSS", 
                        content="\n1. Web Forums: Many online forums are vulerable to XSs, allowing attackers to execute scripts in the context of other users.\n\n2. Blogging Platforms: Context management systems like WordPress or Blogger may have XSS vulnerabilities, especially in user-generated content.\n\n3. E-commerce Websites: Online shopping sites often have XSS vulnerabilites in search fields, product reviews, or user comments sections.\n\n4. Webmail Service: Email services may be susceptible to XSS attacks, enabling attackers to steal session tokens or personal information."),

    TutorialPageContent(title="EXPLOITATION", 
                        content="\nIdentifying Vulnerabilities: Look for input fields, URLs and parameters that are not properly sanitized or validated\n\nCrafting Paylods: Craft malicious payloads using JavaScript to steal cookies, redirect users, deface pages, or perform malicious actions.\n\nInjection: Inject the payload into vulnerable input fields or URLs.\n\nTriggering: Once injected, the payload is triggere when another user accesses the affected page or performs certain actions"),

    TutorialPageContent(title="XSS Exploitation Tools", 
                        content="\nXSS Exploitation Tools refers to software or applications designed to identify, exploit, or defend against Cross-Site Scripting (XSS) vulnerabilities on websites and web applications. There are various tools available. They often provide features such as vulnerability scanning, payload injection, and real-time monitoring to help users detect and prevent XSS attacks effectively. Let us take a look at a few of these tools on the coming chapters."),

    TutorialPageContent(title="XSSer", 
                        content="""\nXsser is an tool for locating and taking advantage of XSS vulnerabilities in web applications. It is a useful tool for penetration testers because it offers a number of capabilities that automate the process of identifying and taking advantage of XSS vulnerabilities.\n\nINSTALLATION:\n    `git clone https://github.com/epsylon/xsser.git`\n    `cd xsser`\n    `./setup.py install`\n\nUSAGE:\n    Launch Xsser: `xsser`\n    For help: `xsser -h`\n    Perform a basic XSS scan on a target URL: `xsser -u <target_url>`\n    Specify a custom User-Agent: `xsser -u <target_url> --user-agent <custom_user_agent>`\n    User a proxy for HTTP requests: `xsser -u <target_url> --proxy http://<proxy_address>:<port>`\n\nEXAMPLE SCENARIO:\n    Suppose we have a web application hosted at "http://example.com/login"\n    Conduct Basic Scan: `xsser -u http://example.com/login`\n    Analyze results: Xsser will analyze the target URL for potential XSS vulnerabilities and display any discovered vulnerabilities\n    Exploit the vulnerabilty: Once a vulnerability is identified, Xsser provides options to exploit it\n    Xsser payload injection: Xsser will inject a payload into the vulnerable parameter and execute it in the context of the target application, demonstrating the exploitation of the XSS vulnerability\n
    """),
    
    TutorialPageContent(title="BeEF-XSS", 
                        content="""\nBeEF-XSS is a tool used for identifying and exploiting vulnerabilities in web browsers. It allows penetration testers to assess the security posture of web applications by targeting client-side vulnerabilities.     \nINSTALLATION:\n    `sudo apt update`\n    `sudo apt install beef-xss`\n\nUSAGE:\n    Start BeEF-XSS: `beef-xss`\n    Access BeEF-XSS: Open a web browser and navigate to `http://localhost:3000/ui/panel`\n    Create user account: Ensure that BeEF-XSS is properly configure and accessible through the web interface. After acecssing the web interface for the first time, you will be prompted to create a new user account. Follow the instructions to set up your account credetials.\n    Configure Hook: BeEF-XSS utilizes a JavaScript hook to establish communication with the target web browsers. Generate and copy the hook script provided by BeEF-XSS.\n    Inject Hook: Inject the hook script into the target web application or webpage. This can be done by adding the script tag with the hook code into the HTML code of the target page.\n\nEXAMPLE SCENARIO:\n    Suppose we have a web application hostead at "http://example.com/login"\n    Generate the hook script in the BeEF-XSS web interface and inject it into the login page of the target application\n    Once the hook script is injected, BeEF-XSS will establish a connection with any user who visits the compromised page\n    Exploit Browser: Below mentioned are some capabilities that BeEF-XSS allows the attacker:\n      * Execute commands in the victim's browser\n      * Capture the browser screenshots\n      * Redirect browser to malicious websites\n      * Gather information about the victim's system and browser\n    Monitor the BeEF-XSS dashboard for information gathered from the exploited browsers and analyze the data to understand the extent of the vulnerabilities and potential impact.
    """),

    TutorialPageContent(title="PwnXSS", 
                        content="""\nPwnXSS is a versatile tool designed for testing and exploiting Cross-Site Scripting (XSS) vulnerabilities in web applications. It provides an intuitive interface and powerful features for identifying, exploiting, and demonstrating the impact of XSS vulnerabilities.     \nINSTALLATION:\n    `git clone https://github.com/pwn0sec/PwnXSS.git`\n    `cd PwnXSS`\n    `chmod +x setup.sh`\n    `./setup.sh`\n\nUSAGE:\n    Start PwnXSS: `python3 pwnxss.py`\n    Access PwnXSS web interface: Open a web browser and navigate to `http://localhost:5000`\n    Configure settings:\n      * Set up proxy settings if required\n      * Customize other settings as per your preferences\n\nEXAMPLE SCENARIO:\n    Suppose we have a web application hostead at "http://example.com/login"\n    Set up the proxy settings in your web browser to route traffic through PwnXSS\n    Exploit XSS:\n      * Navigate to the login page of the target application\n      * Enter a malicious script in the input fields susceptible to XSS\n      * Submit the form to trigger the XSS vulnerability\n    Capture Data: PwnXSS will intercept the malicious script and capture data, including cookies, session tokens, and user credentials.                    
    """),

    TutorialPageContent(title="Preventive Measures", 
                        content="\nInput Validation: Validate and saitize all user inputs to prevent malicious scripts from being executed.\n\nOutput Encoding: Encode output data to prevent browsers from interpreting it as executable code.\n\nContent Security Policy (CSP): Implement CSP Headers to restrict the sources from which certain types of content can be loaded.\n\nRegular Security Audits: Regularly audit your web applications for vulnerabilites and promptly patch any identified issues.\n\nEducate Users: Train users to be cautious of suspicious links, and encourage the use of moder, secure browsers with built-in XSS protection."),
]

for entry in content_entries:
    session.add(entry)

session.commit()

session.close()
