# Physical AI & Humanoid Robotics Living Textbook

Welcome to the Physical AI & Humanoid Robotics Living Textbook - an interactive learning platform with AI-powered teaching assistant functionality.

## 📋 Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Local Development](#local-development)
- [Deployment](#deployment)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)

## Overview

This is a comprehensive educational platform featuring:
- Interactive textbook content on Physical AI and Humanoid Robotics
- AI-powered teaching assistant with RAG (Retrieval-Augmented Generation)
- Modern Docusaurus-based frontend
- FastAPI backend with Qdrant vector database integration
- Responsive design with dark mode support

## Architecture

The application consists of:
- **Frontend**: Docusaurus-based documentation site (in `frontend/`)
- **Backend**: FastAPI application with RAG functionality (in `backend/`)
- **Database**: Qdrant vector database for document embeddings
- **AI Service**: OpenAI API for natural language processing

## Prerequisites

Before running the application, you'll need:

### For Backend:
- Python 3.9+
- OpenAI API Key
- Qdrant Cloud account or self-hosted instance

### For Frontend:
- Node.js 16+ (or 18+ recommended)
- npm or yarn

## Local Development

### 1. Clone the Repository
```bash
git clone https://github.com/SaboorTunio/Physical-AI---Humanoid-Robotics-Book.git
cd Physical-AI---Humanoid-Robotics-Book
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run the backend server
python -m uvicorn src.main:app --reload
```

### 3. Frontend Setup
```bash
# Open a new terminal and navigate to frontend
cd frontend

# Install dependencies
npm install

# Set up environment variables if needed
cp .env.example .env

# Run the development server
npm start
```

The application will be available at:
- Frontend: http://localhost:4000
- Backend API: http://localhost:8000
- Backend API docs: http://localhost:8000/docs

## Deployment

### Frontend Deployment (to Vercel)

1. **Prepare your frontend directory**:
   ```bash
   cd frontend
   ```

2. **Set environment variables in Vercel dashboard**:
   - `BACKEND_API_URL`: Your backend API URL (e.g., `https://your-backend-app.onrender.com`)

3. **Deploy using Vercel CLI**:
   ```bash
   npm install -g vercel
   vercel --prod
   ```

### Backend Deployment (to Render)

1. **Create a Render account** at https://render.com

2. **Create a new Web Service**:
   - Connect to your GitHub repository
   - Choose the `backend` directory
   - Set runtime to Python
   - Add build command: `pip install -r requirements.txt`
   - Add start command: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`

3. **Set environment variables in Render dashboard**:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `QDRANT_URL`: Your Qdrant cluster URL
   - `QDRANT_API_KEY`: Your Qdrant API key
   - `PORT`: 8000 (or leave empty to use Render's default)

### Alternative: Deploy Both to Railway

1. **Create accounts** at https://railway.app

2. **Deploy backend**:
   - New project → GitHub → Select your repo
   - Choose `backend` directory
   - Set environment variables as above

3. **Deploy frontend**:
   - New project → GitHub → Select your repo
   - Choose `frontend` directory
   - Set `BACKEND_API_URL` environment variable

## Environment Variables

### Backend (.env in backend/ directory)
```env
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4-turbo
OPENAI_EMBEDDING_MODEL=text-embedding-3-small

# Qdrant Configuration
QDRANT_URL=https://your-cluster-url.qdrant.tech
QDRANT_API_KEY=your_qdrant_api_key_here
QDRANT_COLLECTION_NAME=textbook_chunks

# Application Configuration
PORT=8000
ENVIRONMENT=production

# CORS Configuration
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.vercel.app,http://localhost:4000
```

### Frontend (.env in frontend/ directory)
```env
# Backend API URL
BACKEND_API_URL=https://your-backend-url.onrender.com
```

## Project Structure

```
Physical-AI---Humanoid-Robotics-Book/
├── backend/                 # FastAPI backend
│   ├── src/
│   │   ├── main.py         # Main application entry point
│   │   ├── config.py       # Configuration settings
│   │   └── services/       # AI and database services
│   ├── requirements.txt    # Python dependencies
│   └── ingest_book.py      # Script to ingest textbook content
├── frontend/               # Docusaurus frontend
│   ├── src/
│   ├── docs/              # Textbook content
│   ├── package.json       # Node.js dependencies
│   └── docusaurus.config.ts # Docusaurus configuration
├── .env.example           # Environment variable examples
└── README.md             # This file
```

## Data Ingestion

To populate your Qdrant database with textbook content:

1. Ensure your backend is running with proper API keys configured
2. Run the ingestion script:
   ```bash
   cd backend
   python ingest_book.py
   ```

This will process the textbook content and store embeddings in Qdrant for the AI assistant.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support

For issues and questions:
- Check the documentation files in the root directory
- Open an issue in the GitHub repository
- Review the implementation guides:
  - `IMPLEMENTATION_COMPLETE.md`
  - `QUICK_START.md`
  - `LIVING_TEXTBOOK_IMPLEMENTATION.md`

## License

This project is open source and available under the [MIT License](LICENSE).