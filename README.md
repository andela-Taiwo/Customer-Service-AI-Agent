# Customer Service AI Agent

An industrial-grade AI-powered customer service agent that autonomously handles customer inquiries, order tracking, and issue resolution using Large Language Models and secure tool integration.

## 🚀 Features

- **Autonomous Customer Support**: Handles common customer inquiries without human intervention
- **Order Management**: Real-time order status and tracking information
- **Shipping Integration**: Multi-carrier shipping status updates
- **Coupon System**: Automated discount generation for customer retention
- **Secure Database Access**: Protected data access with input validation
- **Conversation Memory**: Maintains context across customer interactions
- **Production Ready**: Built with scalability, security, and monitoring in mind

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Framework** | LangChain |
| **LLM** | OpenAI GPT-4 |
| **Backend** | FastAPI |
| **Database** | PostgreSQL (primary), Redis (caching/sessions) |
| **Deployment** | Docker, Kubernetes |
| **Monitoring** | LangSmith, Custom logging |
| **Security** | Input validation, SQL injection prevention, API key management |

## 📋 Prerequisites

- Python 3.11+
- OpenAI API key
- PostgreSQL database
- Redis server

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-org/customer-service-ai-agent.git
cd customer-service-ai-agent
```

### Environment Setup
```bash
cp .env.example .env
# Edit .env with your configuration
```
### Configure Environment
Add the following to your .env file:
``` OPENAI_API_KEY=your_openai_api_key_here
    DATABASE_URL=postgresql://user:password@localhost/customer_service_db
    REDIS_URL=redis://localhost:6379
    LOG_LEVEL=INFO
    ENVIRONMENT=development
```

### Install Dependencies
You can choose Pip or UV
```bash
    
    # UV will automatically create a virtual environment
        # Install UV (if not already installed)
        curl -LsSf https://astral.sh/uv/install.sh | sh

        # 3. Create virtual environment and install dependencies
        uv sync

        # 4. Activate the virtual environment
        source .venv/bin/activate  # On Windows: .venv\Scripts\activate
        # Run the application with UV
        uv run python main.py


    # with pip 
        pip install -r requirements.txt
        # Run the application
        python main.py

 ```
 🚀 Quick Start
### Basic Usage
```bash
from customer_service_agent import setup_customer_service_agent

# Initialize the agent
agent = setup_customer_service_agent()

# Handle customer inquiries
response = agent.run("Where is my order #12345?")
print(response)
```

### Start API Server
```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload

```
## 📞 Support

- 🐛 [Bug Reports](https://github.com/andela-Taiwo/customer-service-ai-agent/issues)
- 💬 [Discussions](https://github.com/andea-Taiwo/customer-service-ai-agent/discussions)
- 📧 **Email**: sokunbitaiwo82@gmail.com


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
<div align="center">

### ⭐ **Don't forget to star this repo if you find it useful!** ⭐

**Made with ❤️ by Our Team**

</div>
