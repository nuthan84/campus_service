###### **Project Title : Smart Campus Complaint \& Service Management System**



**Tech Stack or Technologies used:** 

Frontend: HTML, CSS, Bootstrap, JavaScript

Backend: Python – Django

Database: MySQL

Auth: Django Authentication

Deployment: PythonAnywhere / Render

Version Control: Git + GitHub



###### **Problem Statement**



In colleges and campuses, complaints related to hostel, electricity, water, labs, internet are handled manually, causing delays and lack of transparency.



This system allows students to raise complaints online, track status, and enables admin/maintenance staff to resolve them efficiently.



###### **Modules \& Features**



1. **User (Student)**

* Register / Login
* Raise a complaint (category + description)
* Upload image (optional)
* Track complaint status
* View complaint history



**2. Admin**

* Login dashboard
* View all complaints
* Assign complaint to staff
* Update status (Pending / In-Progress / Resolved)
* Generate reports



**3. Staff**

* Login
* View assigned complaints
* Update resolution status
* Add remarks



###### **Database Tables**

1. users
2. complaints
3. categories
4. staff
5. status\_logs



###### **Real-World Live Flow**



Student → Raises Complaint → Admin Reviews → Assigns Staff →Staff Resolves → Status Updated → Student Notified



###### **Optional Advanced Features (Add Later)**



1. Email notification
2. Admin analytics dashboard
3. Complaint priority
4. Role-based access
5. REST API (Django REST Framework)



