from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>DevOps CI/CD Pipeline</title>
        <style>
            body {
                background-color: #0f172a;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }
 
            .container {
                background-color: #1e293b;
                width: 70%;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0px 0px 15px rgba(0,0,0,0.5);
            }
 
            h1 {
                color: #38bdf8;
                font-size: 42px;
            }
 
            h2 {
                color: #22c55e;
            }
 
            p {
                font-size: 20px;
                line-height: 1.8;
            }
 
            .tools {
                margin-top: 30px;
            }
 
            .tool {
                display: inline-block;
                margin: 10px;
                padding: 12px 20px;
                background-color: #334155;
                border-radius: 8px;
                font-weight: bold;
            }
 
            .footer {
                margin-top: 40px;
                color: #94a3b8;
            }
        </style>
    </head>
 
    <body>
 
        <div class="container">
 
            <h1>DevOps CI/CD Pipeline Successfully Deployed</h1>
 
            <h2>Automation Using Jenkins, Docker & Ansible</h2>
 
            <p>
                This application demonstrates an automated CI/CD pipeline
                deployed on AWS EC2 using GitHub Webhooks, Jenkins,
                Docker Containerization and Ansible Automation.
            </p>
 
            <div class="tools">
                <span class="tool">GitHub</span>
                <span class="tool">Jenkins</span>
                <span class="tool">Docker</span>
                <span class="tool">Ansible</span>
                <span class="tool">AWS EC2</span>
            </div>
 
            <div class="footer">
                CI/CD Pipeline | Infrastructure Automation | DevOps POC
            </div>
 
        </div>
 
    </body>
    </html>
    '''
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
