# 🚀 Encryption & Decryption Project Using AES + RSA


---

## ⚙️ **Tech Stack**  
- **Programming Language**: Python, JavaScript, HTML5, CSS3   
- **Frameworks/Libraries**: Django  
- **Database**: SQLite  


---
## 🐳 Setup Using Docker
You can also run this project using Docker:

### 🔹 1. Pull and run this image on any machine using
```bash
docker pull sudeeprd001/encryption_project-web
```

### 🔹 2. Run the Docker Container
```bash
docker run -d -p 8000:8000 sudeeprd001/encryption_project-web
```

### 🔹 3. Stop and Remove the Container
```bash
docker ps  # Get the container ID
docker stop <container_id>
docker rm <container_id>
```
For Docker setup, visit:

```arduino
http://localhost:8000
```

## 🚀 **Installation & Setup**  
Follow these steps to set up and run the project locally:  

### 🔹 **1. Clone the Repository**  
```bash
git clone https://github.com/SudeepRD001/encryption_project.git
cd encryption_project
```

### 🔹 **2. Install Dependencies**
```bash
pip install -r requirements.txt  # For Python projects
npm install  # For JavaScript projects
```

### 🔹 **3. Configure Environment Variables**
Create a .env file in the project root and set up:
```bash
DJANGO_SECRET_KEY=Your_DJANGO_SECRET_KEY
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
GOOGLE_CLIENT_ID=Your_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET=Your_GOOGLE_CLIENT_SECRET
```

## 🔥 Run the Application
For local setup, use the following command:

```bash
python manage.py runserver  # For Django projects
python app.py  # For Python projects
npm start  # For React/Node.js projects
```


