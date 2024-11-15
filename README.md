

# E-commerce Backend Project with FastAPI and PostgreSQL

This is a **backend-only e-commerce project** built with Python and the **FastAPI framework**. It is connected to a **PostgreSQL database using Docker**. This project provides basic e-commerce functionalities, including user and product management, product purchasing, and updating product statuses. This was a practical test of our skills with FastAPI, database management, security, and Docker configuration.

## Features

- **User Management 📑**: Register, login, and manage users.
- **Product Management**: CRUD operations for products (*create, read, update, delete*).
- **Purchasing Products**: API to purchase products.
- **Product Status Tracking**: View and update product statuses.
- **Secure API Endpoints**: _Authentication and authorization for secure access._

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

Make sure you have the following installed:

- **Docker** and **Docker Compose**
- **Python 3.8+**

### Installation and Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Omarjabari007/E-commerce-BackEnd.git
   

2. **Set Up Environment Variables**

Create a .env file in the project root and add the necessary environment variables for PostgreSQL and the application settings.

**Example .env file:**

```
dotenv
DATABASE_URL=postgresql://user:password@db:5432/ecommerce_db
SECRET_KEY=your-secret-key
Start the Docker Containers
```
**Use Docker Compose to build and start the containers.**
```
docker-compose up --build
```
This will:

### Set up a PostgreSQL database container ###
Launch the FastAPI application container
The application will be accessible at  **http://localhost:8000.**

For any questions, please contact **Omar Mohammed Karam Abdelfattah Jabari** at **omarjabari009@gmail.com.**

**This project was completed by three students ( Omar , Yasser , Hattem) . We learned to use GitHub to divide tasks, manage branches, and work together in a real-world environment.
Enjoy exploring the e-commerce backend!**







