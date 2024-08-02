# AgriConsult Flask Application

## Description
AgriConsult is a web application built with Flask that provides agricultural consulting services. It features a booking system for appointments, a discussion forum, and a blog section for sharing agricultural insights. This platform provides farmers with access to Agric Experts where they can book sessions to talk to farmers on ways of improving yield and learn about better ways of storing their produce and modern farming methods.
Individuals who are passionate about farming but not as a full-time job can also book sessions on how to start up farms in their homes. Mission Statement;

Link: 


![home](https://github.com/user-attachments/assets/a5a49f7d-0e0f-43d3-9bdd-31fbbab02f69)



## Features
 <h1>User authentication (signup and login)</h1>
 
![login](https://github.com/user-attachments/assets/ac72bb94-1561-4c99-94cf-ecb200047f84)
![signup](https://github.com/user-attachments/assets/f7b9028b-411a-429c-8b8e-18d51b7ad3e6)

  <h1>Appointment booking with agricultural experts</h1>
  
![book](https://github.com/user-attachments/assets/95688be5-1578-4091-a0c0-d20c9b23a28c)
![book1](https://github.com/user-attachments/assets/76d740a7-e7c9-4fff-87b6-c3e0d362a1da)


- Discussion forum for agricultural topics
![connect](https://github.com/user-attachments/assets/ae8508e5-d0ed-4002-a33a-613303c3ad03)

<h1>Blog section with agricultural articles</h1>

![blog](https://github.com/user-attachments/assets/aa4a7e95-187b-4335-83cc-18ea94c6c2fe)


  <h1>CONTACT US</h1>
  
![contact](https://github.com/user-attachments/assets/338bd5be-3548-414a-9a38-178327e519cf)

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






