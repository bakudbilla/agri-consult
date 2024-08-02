# AgriConsult Flask Application
## Description
AgriConsult is a web application built with Flask that provides agricultural consulting services. It features a booking system for appointments, a discussion forum, and a blog section for sharing agricultural insights. This platform provides farmers with access to Agric Experts where they can book sessions to talk to farmers on ways of improving yield and learn about better ways of storing their produce and modern farming methods.
Individuals who are passionate about farming but not as a full-time job can also book sessions on how to start up farms in their homes. Mission Statement;

Link: 


![Screenshot 2024-07-31 180246](https://github.com/user-attachments/assets/2828540a-17ad-4e41-803a-c470f2a57312)



## Features
 <h1>User authentication (signup and login)</h1>
 
![Screenshot 2024-07-31 180514](https://github.com/user-attachments/assets/bf13b4c2-1a36-4cb3-8553-765131e4b374)
![Screenshot 2024-07-31 180535](https://github.com/user-attachments/assets/249ac999-34aa-43e4-8918-f525773e4e42)

  <h1>Appointment booking with agricultural experts</h1>
  
  ![Screenshot 2024-07-31 180310](https://github.com/user-attachments/assets/31528b0c-dae3-4eb9-9539-1c8829733393)
![Screenshot 2024-07-31 180331](https://github.com/user-attachments/assets/89e3fde1-030d-4141-9e19-192d143bfc51)


- Discussion forum for agricultural topics
  ![Screenshot 2024-07-31 180420](https://github.com/user-attachments/assets/6a003da3-ccd2-4616-bfc6-0ee9bbbf8d59)

<h1>Blog section with agricultural articles</h1>

![Screenshot 2024-07-31 185323](https://github.com/user-attachments/assets/778d6139-ec6d-45a6-a219-87b3f651292f)


  <h1>CONTACT US</h1>
  
![Screenshot 2024-07-31 180448](https://github.com/user-attachments/assets/2e7b6e97-a7d8-4bcd-90ab-6821afc7d23a)

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
 ```
git clone https://github.com/yourusername/agriconsult.git 
   cd agriconsult
 ```

2. Create a virtual environment: <br>
 ```
 python -m venv venv
 ```

3. Activate the virtual environment:
 On Windows:
  ```
  venv\Scripts\activate
  ```
 On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required packages:
   ``` 
   pip install -r requirements.txt
   ```

  
## Configuration

1. Create a `.env` file in the root directory and add the following:<br>
SECRET_KEY=your_secret_key<br>
MAIL_USERNAME=your_email@gmail.com<br>
MAIL_PASSWORD=your_app_password<br>
Replace `your_secret_key`, `your_email@gmail.com`, and `your_app_password` with your actual values.

2. Set up the database:
flask db upgrade

## Running the Application

1. Start the Flask development server:
   flask run
Copy
2. Open a web browser and navigate to `http://localhost:5000`

## Contributing
Contributions to AgriConsult are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
This README provides:






