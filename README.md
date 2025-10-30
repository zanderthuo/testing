# Project Title

## DT1-25 — AI Chat System using Docker, OpenRouter & GCP

### Student Information

Name: Alexander Thuo
Institution: Berner Fachhochschule
Assignment: DT1-25 Practical Deployment
Evaluator: Sid Singh (sid027)

### Project Overview

This project implements a two-container system deployed on Google Cloud Platform (GCP).
It integrates a Flask backend API and a Streamlit frontend UI, both containerized with Docker, and uses OpenRouter’s DeepSeek model for generating responses.

Users can enter prompts through the Streamlit interface, which sends requests to the Flask API.
The API calls the OpenRouter Chat Completions API to get model responses and returns them to the frontend.

### System Architecture
🔹 Architecture Diagram

(Insert your PNG here — e.g., /docs/architecture.png)


⚙️ Technologies Used

🐍 Python 3.11 (Flask, Streamlit, Requests)

🐳 Docker & Docker Compose

☁️ Google Cloud Platform (Compute Engine VM)

🔑 OpenRouter API (DeepSeek Chat Model)

🔒 GCP Firewall Rules & Network Security

🧩 Repository Structure
.
├── api.py                  # Flask backend
├── frontend.py             # Streamlit frontend
├── Dockerfile.api          # Backend Dockerfile
├── Dockerfile.frontend     # Frontend Dockerfile
├── docker-compose.yml      # Orchestration
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
├── docs/
│   └── architecture.png
└── README.md

⚙️ Setup Instructions
🧭 1. Clone the Repository
git clone https://github.com/<username>/alexander_thuo-dt1-25.git
cd alexander_thuo-dt1-25

🧠 2. Configure Environment Variables

Create a .env file in the root directory:

OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
BASE_URL=https://openrouter.ai/api/v1
MODEL_NAME=deepseek/deepseek-chat
API_URL=http://api:5001
PORT=5001


(Do not share your real API key in the public repo — only use .env.example.)

🐳 3. Build and Run the Containers
docker compose down
docker compose up --build


This launches:

Flask API → http://localhost:5001

Streamlit UI → http://localhost:8501

🧱 4. Test Endpoints Locally
curl http://localhost:5001/ping
# → {"ack": "pong"}

curl -X POST http://localhost:5001/chat \
     -H "Content-Type: application/json" \
     -d '{"input": "hello"}'
# → {"answer": "Hi there!"}

☁️ Deployment on Google Cloud VM
🧩 1. Create and SSH into VM

Go to Compute Engine → VM Instances → Create Instance

OS: Debian 12 (Bookworm)

Allow HTTP & HTTPS traffic

SSH into the VM:

gcloud compute ssh <your-instance-name>

🐳 2. Install Docker and Docker Compose
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bookworm stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo systemctl enable docker --now

⚙️ 3. Clone Repo & Run Compose
git clone https://github.com/<username>/alexander_thuo-dt1-25.git
cd alexander_thuo-dt1-25
sudo docker compose up -d

🔒 4. Configure Firewall Rules

Allow access only from your IP and Sid Singh’s network:

Setting	Value
Direction	Ingress
Action on match	Allow
Targets	Specified target tags
Target tags	dt1-vm
Source IPv4 ranges	83.77.144.17/32, 147.87.0.0/16
Protocols & Ports	tcp:22,5001,8501
🧠 5. Access the App

In your browser, visit:

http://<your-external-ip>:8501


✅ The Streamlit UI should appear.

🧠 Troubleshooting Checklist
Issue	Solution
Connection timed out	Check GCP firewall and network tags
404 Client Error	Confirm valid model (deepseek/deepseek-chat)
Invalid API key	Recreate .env with correct key
Frontend cannot reach API	Verify API_URL=http://api:5001
Docker container exits immediately	Run docker compose logs for details
🧩 Security Considerations

API key stored securely in .env

Only selected CIDR ranges (you + Sid Singh) can access ports

Docker isolation for each service

No sensitive data in GitHub

🏁 Deliverables Summary
Task	Points	Status
Clone repo locally	1	✅
Draw system architecture	2	✅
Build Docker image locally	1	✅
Push image to Docker Hub	1	✅
Create OpenRouter API Key	1	✅
Create private GitHub repo	1	✅
Launch GCP VM	1	✅
SSH into VM	1	✅
Install Docker + Compose	1	✅
Run compose file	1	✅
Secure with firewall	2	✅
Create Streamlit UI	2	✅
Connect UI to API	2	✅
Display model response	2	✅
Add Sid Singh to firewall + repo	3	✅
Write detailed README	2	✅

Total: 🎯 25/25 marks potential

🧾 Acknowledgements

Special thanks to Berner Fachhochschule and Sid Singh for the assignment guidance and evaluation.

Would you like me to include a sample docs/architecture.png (Mermaid diagram) section you can directly paste in your README (for GitHub auto-rendering)?
It’ll visualize your backend–frontend–OpenRouter pipeline beautifully without needing to upload a separate PNG.