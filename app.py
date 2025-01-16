
import os
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session, flash
from random import randint
from werkzeug.utils import secure_filename
import tempfile


db = SQLAlchemy()

def create_app():

    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///rj.db"
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    UPLOAD_FOLDER = '/Users/mr.sairajnanda/Documents/House-website-main/House-website-main/house-website-master'
    ALLOWED_EXTENSIONS = {'xlsx'}

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)
   



    otp_store = {}


    class Student(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(100), nullable=False, unique=True)
        exam_city = db.Column(db.String(100), nullable=False)
        exam_state = db.Column(db.String(100), nullable=False, default="Unknown")  
        group_id = db.Column(db.Integer, nullable=False)
        house = db.Column(db.String(100), nullable=False)
        region = db.Column(db.String(100), nullable=False)


        def __repr__(self):
            return f'<Student {self.email}>'

    class FormSubmission(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name=db.Column(db.String(100),nullable=False)
        email = db.Column(db.String(100), nullable=False)
        house = db.Column(db.String(100), nullable=False)
        region = db.Column(db.String(100), nullable=False)
        gender = db.Column(db.String(20), nullable=False)
        phone = db.Column(db.String(10), nullable=False)

        def __repr__(self):
            return f'<FormSubmission {self.email}>'



    @app.route('/view_data')
    def view_data():

        students = Student.query.all()  
        form_submissions = FormSubmission.query.all()  

        return render_template('view_data.html', students=students)
    @app.route('/view_data/students')
    def view_students_data():
        students = Student.query.all()  
        return render_template('students_table.html', students=students, form_submissions=[])

    @app.route('/view_data/form_submissions')
    def view_form_submissions_data():
        form_submissions = FormSubmission.query.all()  
        return render_template('form_submission_table.html',  form_submissions=form_submissions)


    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    def populate_db_from_excel(excel_file):
        
        df = pd.read_excel(excel_file)
        df.fillna("", inplace=True) 
        
        for _, row in df.iterrows():
            
            existing_student = Student.query.filter_by(email=row['Student_Email']).first()
            
            if existing_student:
                
                existing_student.exam_city = row['ExamCity']
                existing_student.exam_state = row['ExamState']
                existing_student.group_id = row['GroupId']
                existing_student.house = row['House']
                existing_student.region = row['Region']
            else:
                
                new_student = Student(
                    email=row['Student_Email'],
                    exam_city=row['ExamCity'],
                    exam_state=row['ExamState'],
                    group_id=row['GroupId'],
                    house=row['House'],
                    region=row['Region']
                )
                db.session.add(new_student) 

        db.session.commit()

    @app.route('/upload', methods=['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part', 'danger')
                return redirect(request.url)

            file = request.files['file']

            if file.filename == '':
                flash('No selected file', 'danger')
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                # Ensure upload folder exists
                if not os.path.exists(app.config['UPLOAD_FOLDER']):
                    os.makedirs(app.config['UPLOAD_FOLDER'])

                # Save the uploaded file
                file.save(file_path)

                # Process the file (for example, populate DB)
                populate_db_from_excel(file_path)

                flash('Database updated successfully!', 'success')
                return redirect(url_for('upload_file'))

        return render_template('upload.html')


    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/Rc')
    def RC():
        return render_template("Regional-Coordinators.html")

    @app.route('/HC')
    def HC():
        return render_template("house-council.html")

    @app.route('/pr')
    def pr():
        return render_template("Pr-team.html")

    @app.route('/Club')
    def Club():
        return render_template("clubs.html")

    @app.route('/Resource')
    def resource():
        return render_template("resources.html")

    @app.route('/announcement')
    def announcement():
        return render_template("announcement.html")
    @app.route('/shivam')
    def shivam():
        return render_template("shivam.html")
    @app.route('/monika')
    def monika():
        return render_template("monika.html")
    @app.route('/navi')
    def navi():
        return render_template("navi.html")
    @app.route('/sadhana')
    def sadhana():
        return render_template("sadhana.html")
    @app.route('/sravya')
    def sravya():
        return render_template("sravya.html")
    @app.route('/vasundhara')
    def vasundhara():
        return render_template("vasundhara.html")
    @app.route('/saumya')
    def saumya():
        return render_template("saumya.html")
    @app.route('/hari')
    def hari():
        return render_template("hari.html")

    @app.route('/pastevent')
    def pastevent():
        return render_template("pastevent.html")



    @app.route('/joinus', methods=['GET', 'POST'])
    def joinus():
        # Dictionary for region-specific WhatsApp links
        region_links = {
            "Mumbai": "https://chat.whatsapp.com/mumbai_group_link",
            "Kolkata": "https://chat.whatsapp.com/kolkata_group_link",
            "Chennai": "https://chat.whatsapp.com/chennai_group_link",
            "Delhi-NCR": "https://chat.whatsapp.com/delhi_ncr_group_link",
            "Chandigarh": "https://chat.whatsapp.com/chandigarh_group_link",
            "Lucknow": "https://chat.whatsapp.com/lucknow_group_link",
            "Patna": "https://chat.whatsapp.com/patna_group_link",
            "Bangalore": "https://chat.whatsapp.com/bangalore_group_link",
            "Hyderabad": "https://chat.whatsapp.com/hyderabad_group_link"
        }

        # Link for female-specific WhatsApp group
        female_group_link = "https://chat.whatsapp.com/female_group_link"

        if request.method == 'POST':
            email = request.form.get('email')
            name = request.form.get('name')
            house = request.form.get('house')
            region = request.form.get('region')  # Get region from form
            gender = request.form.get('gender')  # Get gender from form
            phone = request.form.get('phone')

            # Check if the email exists in the Student table
            student = Student.query.filter_by(email=email).first()

            if student:
                # Store the form submission in the FormSubmission table
                new_submission = FormSubmission(
                    email=email,
                    name=name,
                    house=house,
                    region=region,
                    gender=gender,
                    phone=phone
                )
                db.session.add(new_submission)
                db.session.commit()

                # Fetch the region-specific WhatsApp link
                region_link = region_links.get(region)

                if region_link:
                    # If the user is female, provide both region and female-specific group links
                    if gender.lower() == 'female':
                        flash(f'Details submitted successfully! Here is your {region} WhatsApp group link: {region_link}', 'success')
                        flash(f'Additionally, join the female WhatsApp group link: {female_group_link}', 'success')
                    else:
                        flash(f'Details submitted successfully! Here is your {region} WhatsApp group link: {region_link}', 'success')
                else:
                    flash('Selected region is invalid.', 'danger')

                return redirect("/joinus")  # Redirect back or to some other page
            else:
                flash('Email not found. Please check your email or contact admin.', 'danger')

        return render_template('Joinus.html')




    @app.route('/populate')
    def populate():
        excel_file = '/Users/mr.sairajnanda/Documents/house_website/namdapha_house_for_web.xlsx'  
        if os.path.exists(excel_file):
            populate_db_from_excel(excel_file)
            return "Database populated successfully!"
        else:
            return "Excel file not found!"


    return app
    #postgresql://namdapha_database_user:kMf47MQ0YmvcyXR8JYRaTLzmdQxmLiiC@dpg-cu0uelt2ng1s73e3eei0-a.oregon-postgres.render.com/namdapha_database

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)