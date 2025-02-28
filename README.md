# Vehicle-mangement-system
# Vehicle Service Management System

## 📌 Project Overview
The **Vehicle Service Management System** allows users to register vehicles, report issues, track repairs, and visualize revenue trends. The system supports component registration, service pricing, and payment simulation.

## 🚀 Features
- **Component Registration & Pricing Management**
- **Vehicle Repair Tracking**
- **Issue Reporting & Component Selection**
- **Final Price Calculation & Payment Simulation**
- **Revenue Graphs**

## 🖼️ Screenshots
*(Add actual screenshots here)*

![Dashboard Screenshot](screenshots/dashboard.png)
![Repair Form Screenshot](screenshots/repair_form.png)

---

## ⚙️ Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/vehicle-service-management.git
cd vehicle-service-management
```

### **2️⃣ Backend Setup (Django & SQLite)**
```sh
cd backend
python -m venv venv
source venv/bin/activate  # (On Windows: venv\Scripts\activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### **3️⃣ Frontend Setup (React.js)**
```sh
cd frontend
npm install
npm start
```

---

## 📡 API Documentation
### 🔹 **Component APIs**
#### **1️⃣ Get All Components**
```http
GET /service/components/
```
#### **2️⃣ Register a New Component**
```http
POST /service/components/
Content-Type: application/json
{
  "name": "Brake Pad",
  "price": 50.00
}
```

### 🔹 **Vehicle APIs**
#### **3️⃣ Get All Vehicles**
```http
GET /service/vehicles/
```
#### **4️⃣ Register a Vehicle**
```http
POST /service/vehicles/
Content-Type: application/json
{
  "vin": "ABC12345XYZ",
  "make": "Toyota",
  "model": "Corolla",
  "year": 2020
}
```

### 🔹 **Repair & Issue Reporting APIs**
#### **5️⃣ Record a Repair**
```http
POST /service/repairs/
Content-Type: application/json
{
  "vehicle": 1,
  "issue_description": "Engine overheating",
  "service_type": "new",
  "labor_cost": 250.00,
  "components": [1, 2]
}
```
#### **6️⃣ Fetch All Repairs**
```http
GET /service/repairs/
```

### 🔹 **Revenue API**
#### **7️⃣ Fetch Revenue Data**
```http
GET /service/revenue/
```

---

## 🛠️ Technologies Used
- **Backend**: Python, Django, SQLite
- **Frontend**: React.js, Recharts
- **API**: Django REST Framework (DRF)

---



