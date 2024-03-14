import mysql.connector

# Establish a connection to your MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9009-Ocean!",
    auth_plugin='mysql_native_password'
)

# Establish a connection to MySQL
cursor = conn.cursor()

# Create the database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS Skillmate")
cursor.execute(f"USE Skillmate")

# Create User Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS User (
        UserID INT AUTO_INCREMENT PRIMARY KEY,
        FirstName VARCHAR(255),
        LastName VARCHAR(255),
        Email VARCHAR(255),
        PasswordHash VARCHAR(255),
        ProfilePicture VARCHAR(255),
        Bio TEXT,
        DateOfBirth DATE,
        Gender VARCHAR(10),
        PhoneNumber VARCHAR(15),
        IsActive BOOLEAN DEFAULT 0,
        IsEmployee BOOLEAN DEFAULT 0,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
""")

# Create Job Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Job (
        JobID INT AUTO_INCREMENT PRIMARY KEY,
        EmployerID INT,
        JobTitle VARCHAR(255),
        JobDescription TEXT,
        RequiredExperience INT,
        PreferredLocation VARCHAR(255),
        OtherQualifications TEXT,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (EmployerID) REFERENCES User(UserID)
    )
""")

# Create Application Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Application (
        ApplicationID INT AUTO_INCREMENT PRIMARY KEY,
        ApplicantID INT,
        JobID INT,
        Status VARCHAR(255),
        CoverLetter TEXT,
        Resume VARCHAR(255),
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (ApplicantID) REFERENCES User(UserID),
        FOREIGN KEY (JobID) REFERENCES Job(JobID)
    )
""")

# Create Like Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS `Like` (
        LikeID INT AUTO_INCREMENT PRIMARY KEY,
        SenderID INT,
        ReceiverID INT,
        IsMatch BOOLEAN DEFAULT FALSE,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (SenderID) REFERENCES User(UserID),
        FOREIGN KEY (ReceiverID) REFERENCES User(UserID)
    )
""")

# Create Match Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS `Match` (
        MatchID INT AUTO_INCREMENT PRIMARY KEY,
        JobID INT,
        ApplicantID INT,
        MatchStrength INT,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (JobID) REFERENCES Job(JobID),
        FOREIGN KEY (ApplicantID) REFERENCES User(UserID)
    )
""")

# Create Message Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Message (
        MessageID INT AUTO_INCREMENT PRIMARY KEY,
        SenderID INT,
        ReceiverID INT,
        Content TEXT,
        IsRead BOOLEAN,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (SenderID) REFERENCES User(UserID),
        FOREIGN KEY (ReceiverID) REFERENCES User(UserID)
    )
""")

# Create UserLink Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS UserLink (
        UserLinkID INT AUTO_INCREMENT PRIMARY KEY,
        UserID INT,
        LinkType VARCHAR(255),
        LinkURL VARCHAR(255),
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES User(UserID)
    )
""")

# Create Skill Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Skill (
        SkillID INT AUTO_INCREMENT PRIMARY KEY,
        UserID INT,
        SkillName VARCHAR(255),
        SkillLevel VARCHAR(20),
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES User(UserID)
    )
""")

# Create Education Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Education (
        EducationID INT AUTO_INCREMENT PRIMARY KEY,
        UserID INT,
        Institution VARCHAR(255),
        Degree VARCHAR(255),
        FieldOfStudy VARCHAR(255),
        GraduationDate DATE,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES User(UserID)
    )
""")

# Create Work Experience Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS WorkExperience (
        ExperienceID INT AUTO_INCREMENT PRIMARY KEY,
        UserID INT,
        JobTitle VARCHAR(255),
        Company VARCHAR(255),
        StartDate DATE,
        EndDate DATE,
        Description TEXT,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES User(UserID)
    )
""")

# Create Location Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Location (
        LocationID INT AUTO_INCREMENT PRIMARY KEY,
        UserID INT,
        City VARCHAR(255),
        State VARCHAR(255),
        ZipCode VARCHAR(20),
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (UserID) REFERENCES User(UserID)
    )
""")

# Sample Users
users_data = [
    ('John', 'Doe', 'john.doe@email.com', 'hashed_password_1', 'profile_pic_1.jpg', 'I am a software engineer.', '1990-01-15', 'Male', '123-456-7890', 1, 0),
    ('Jane', 'Smith', 'jane.smith@email.com', 'hashed_password_2', 'profile_pic_2.jpg', 'Experienced marketing professional.', '1985-05-20', 'Female', '987-654-3210', 1, 0),
    ('Chris', 'Johnson', 'chris.johnson@email.com', 'hashed_password_3', 'profile_pic_3.jpg', 'Passionate graphic designer.', '1992-08-10', 'Male', '456-789-0123', 1, 0),
    ('Alice', 'Johnson', 'alice.johnson@email.com', 'hashed_password_4', 'profile_pic_4.jpg', 'Experienced software developer.', '1988-07-22', 'Female', '111-222-3333', 1, 0),
    ('Bob', 'Miller', 'bob.miller@email.com', 'hashed_password_5', 'profile_pic_5.jpg', 'Digital marketing enthusiast.', '1995-03-10', 'Male', '444-555-6666', 1, 0),
    ('Eva', 'Brown', 'eva.brown@email.com', 'hashed_password_6', 'profile_pic_6.jpg', 'Creative graphic designer.', '1990-12-05', 'Female', '777-888-9999', 1, 0),
    ('Grace', 'Williams', 'grace.w@email.com', 'hashed_password_7', 'profile_pic_7.jpg', 'Full-stack developer with a focus on front-end technologies.', '1987-04-12', 'Female', '111-222-3334', 1, 0),
    ('Michael', 'Brown', 'michael.b@email.com', 'hashed_password_8', 'profile_pic_8.jpg', 'Experienced project manager with a background in IT.', '1980-11-25', 'Male', '444-555-6667', 1, 0),
    ('Sophie', 'Smith', 'sophie.s@email.com', 'hashed_password_9', 'profile_pic_9.jpg', 'Creative content creator with a passion for storytelling.', '1991-09-08', 'Female', '777-888-1000', 1, 0)
    
]

# Insert Sample Users
user_insert_query = """
    INSERT INTO User (FirstName, LastName, Email, PasswordHash, ProfilePicture, Bio, DateOfBirth, Gender, PhoneNumber, IsActive, IsEmployee)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

cursor.executemany(user_insert_query, users_data)

# Sample Jobs
jobs_data = [
    (1, 'Software Engineer', 'Develop and maintain software applications.', 3, 'Any', 'Experience with Python and Django is a plus.'),
    (2, 'Marketing Specialist', 'Create and execute marketing strategies.', 5, 'New York', 'Knowledge of social media advertising platforms.'),
    (3, 'Graphic Designer', 'Design visually appealing graphics for marketing materials.', 2, 'Los Angeles', 'Proficient in Adobe Creative Suite'),
    (4, 'Data Scientist', 'Analyze and interpret complex data sets.', 4, 'Remote', 'Strong background in machine learning.'),
    (5, 'Content Writer', 'Create engaging and informative content.', 2, 'Any', 'Excellent writing and editing skills.'),
    (6, 'UI/UX Designer', 'Design user interfaces for web and mobile applications.', 3, 'San Francisco', 'Proficiency in design tools like Sketch or Figma.'),
    (7, 'Front-end Developer', 'Create responsive and visually appealing user interfaces.', 3, 'Remote', 'Proficient in HTML, CSS, and JavaScript frameworks.'),
    (8, 'IT Project Manager', 'Lead and coordinate IT projects for optimal efficiency.', 6, 'New York', 'PMP certification is a plus.'),
    (9, 'Content Strategist', 'Develop and implement content strategies for online platforms.', 4, 'San Francisco', 'Experience in SEO and content marketing.')
    
]

# Insert Sample Jobs
job_insert_query = """
    INSERT INTO Job (EmployerID, JobTitle, JobDescription, RequiredExperience, PreferredLocation, OtherQualifications)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor.executemany(job_insert_query, jobs_data)

# Sample Applications
applications_data = [
    (1, 1, 'Pending', 'I have a strong background in software development.', 'resume_4.pdf'),
    (2, 2, 'Rejected', 'I have extensive experience in marketing.', 'resume_5.pdf'),
    (3, 3, 'Approved', 'I am a skilled graphic designer with a creative mindset.', 'resume_6.pdf'),
    (4, 4, 'Approved', 'I specialize in data analysis and machine learning.', 'resume_7.pdf'),
    (5, 5, 'Pending', 'I have a passion for creating compelling content.', 'resume_8.pdf'),
    (6, 6, 'Rejected', 'I am an experienced UI/UX designer with a focus on user-centered design.', 'resume_9.pdf'),
    (7, 7, 'Approved', 'I specialize in front-end development with a focus on user experience.', 'resume_10.pdf'),
    (8, 8, 'Pending', 'I have successfully managed complex IT projects in the past.', 'resume_11.pdf'),
    (9, 9, 'Rejected', 'My content creation skills align with your organization\'s goals.', 'resume_12.pdf'),
]

# Insert Sample Applications
application_insert_query = """
    INSERT INTO Application (ApplicantID, JobID, Status, CoverLetter, Resume)
    VALUES (%s, %s, %s, %s, %s)
"""

cursor.executemany(application_insert_query, applications_data)

# Sample Likes
likes_data = [
    (1, 2, 0),
    (2, 1, 1),
    (3, 4, 0),
    (4, 5, 0),
    (5, 4, 1),
    (6, 7, 0),
    (7, 8, 0),
    (8, 7, 1),
    (9, 5, 0)
]

# Insert Sample Likes
like_insert_query = """
    INSERT INTO `Like` (SenderID, ReceiverID, IsMatch)
    VALUES (%s, %s, %s)
"""

cursor.executemany(like_insert_query, likes_data)

# Sample Matches
matches_data = [
    (1, 2, 90),
    (4, 5, 80),
    (8, 7, 70)
]

# Insert Sample Matches
match_insert_query = """
    INSERT INTO `Match` (JobID, ApplicantID, MatchStrength)
    VALUES (%s, %s, %s)
"""

cursor.executemany(match_insert_query, matches_data)

# Sample Messages
messages_data = [
    (1, 2, 'Hello, I\'m interested in the software engineer position.', 0),
    (2, 1, 'Hi John, nice to meet you! We can discuss more about the position.', 0),
    (3, 4, 'Your graphic design skills caught my attention.', 1),
    (4, 5, 'Hello, I\'m interested in the data scientist position.', 0),
    (5, 4, 'Hi Alice, nice to meet you! We can discuss more about the content writer position.', 0),
    (6, 7, 'Your UI/UX design skills are impressive.', 1),
    (7, 8, 'Hello, I\'m interested in the front-end developer position.', 0),
    (8, 7, 'Hi Grace, nice to meet you! We can discuss more about the IT project manager position.', 0),
    (9, 5, 'Your content creation skills are impressive.', 1)
]

# Insert Sample Messages
message_insert_query = """
    INSERT INTO Message (SenderID, ReceiverID, Content, IsRead)
    VALUES (%s, %s, %s, %s)
"""

cursor.executemany(message_insert_query, messages_data)

# Sample User Links
user_links_data = [
    (1, 'LinkedIn', 'https://www.linkedin.com/in/johndoe'),
    (2, 'Twitter', 'https://twitter.com/janesmith'),
    (3, 'Portfolio', 'https://www.chrisjohnsondesigns.com'),
    (4, 'GitHub', 'https://github.com/alicejohnson'),
    (5, 'Blog', 'https://www.bobmillerwrites.com'),
    (6, 'Dribbble', 'https://dribbble.com/evabrown'),
    (7, 'GitHub', 'https://github.com/gracewilliams'),
    (8, 'LinkedIn', 'https://www.linkedin.com/in/michaelbrown'),
    (9, 'Blog', 'https://www.sophiesmithwrites.com')
]

# Insert Sample User Links
user_link_insert_query = """
    INSERT INTO UserLink (UserID, LinkType, LinkURL)
    VALUES (%s, %s, %s)
"""

cursor.executemany(user_link_insert_query, user_links_data)

# Sample Skills
skills_data = [
    (1, 'Python', 'Advanced'),
    (1, 'Django', 'Intermediate'),
    (2, 'Digital Marketing', 'Expert'),
    (3, 'Graphic Design', 'Advanced'),
    (4, 'Machine Learning', 'Advanced'),
    (4, 'Python', 'Intermediate'),
    (5, 'Content Marketing', 'Expert'),
    (6, 'UI Design', 'Advanced'),
    (7, 'React', 'Intermediate'),
    (7, 'Angular', 'Intermediate'),
    (8, 'Project Management', 'Expert'),
    (9, 'Content Creation', 'Advanced')
]

# Insert Sample Skills
skill_insert_query = """
    INSERT INTO Skill (UserID, SkillName, SkillLevel)
    VALUES (%s, %s, %s)
"""

cursor.executemany(skill_insert_query, skills_data)
# Sample Education
education_data = [
    (1, 'University of Computer Science', 'Bachelor of Science', 'Computer Science', '2012-05-15'),
    (2, 'Marketing Academy', 'Master of Business Administration', 'Marketing', '2010-12-20'),
    (3, 'Art and Design Institute', 'Bachelor of Fine Arts', 'Graphic Design', '2015-06-30'),
    (4, 'Data Science Institute', 'Master of Science', 'Data Science', '2014-08-18'),
    (5, 'Journalism School', 'Bachelor of Arts', 'Journalism', '2018-05-12'),
    (6, 'Design Academy', 'Master of Fine Arts', 'UI/UX Design', '2016-11-30'),
    (7, 'Computer Science University', 'Bachelor of Science', 'Computer Science', '2009-05-20'),
    (8, 'Business School', 'Master of Business Administration', 'Project Management', '2013-08-15'),
    (9, 'Journalism Institute', 'Bachelor of Arts', 'Journalism', '2015-06-30')
    
]

# Insert Sample Education
education_insert_query = """
    INSERT INTO Education (UserID, Institution, Degree, FieldOfStudy, GraduationDate)
    VALUES (%s, %s, %s, %s, %s)
"""

cursor.executemany(education_insert_query, education_data)

# Sample Work Experience
work_experience_data = [
    (1, 'Software Engineer', 'Tech Solutions Inc.', '2012-06-01', '2020-12-31', 'Developed and maintained web applications.'),
    (2, 'Marketing Specialist', 'Global Marketing Agency', '2011-01-15', '2019-09-30', 'Led successful marketing campaigns.'),
    (3, 'Graphic Designer', 'Creative Design Studio', '2015-07-01', '2021-03-15', 'Designed graphics for various clients.'),
    (4, 'Data Scientist', 'Tech Innovations', '2014-09-01', '2021-06-30', 'Led data science projects and implemented machine learning models.'),
    (5, 'Content Writer', 'Digital Media Agency', '2018-06-01', '2020-12-15', 'Created content for various clients, including articles and blog posts.'),
    (6, 'UI/UX Designer', 'Creative Agency', '2017-01-01', '2023-02-28', 'Designed user interfaces for web and mobile applications.'),
    (7, 'Full-stack Developer', 'Tech Innovations', '2009-06-01', '2018-12-31', 'Developed and maintained various web applications.'),
    (8, 'Project Manager', 'Global IT Solutions', '2013-01-15', '2021-09-30', 'Successfully managed and delivered IT projects on time.'),
    (9, 'Content Creator', 'Online Media Agency', '2015-07-01', '2021-03-15', 'Created engaging content for diverse online platforms.')
    
]

# Insert Sample Work Experience
work_experience_insert_query = """
    INSERT INTO WorkExperience (UserID, JobTitle, Company, StartDate, EndDate, Description)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor.executemany(work_experience_insert_query, work_experience_data)

# Sample Locations
locations_data = [
    (1, 'San Francisco', 'CA', '94105'),
    (2, 'New York', 'NY', '10001'),
    (3, 'Los Angeles', 'CA', '90001'),
    (4, 'Seattle', 'WA', '98101'),
    (5, 'Austin', 'TX', '78701'),
    (6, 'Portland', 'OR', '97201'),
    (7, 'Seattle', 'WA', '98105'),
    (8, 'Boston', 'MA', '02101'),
    (9, 'Chicago', 'IL', '60601')
]

# Insert Sample Locations
location_insert_query = """
    INSERT INTO Location (UserID, City, State, ZipCode)
    VALUES (%s, %s, %s, %s)
"""

cursor.executemany(location_insert_query, locations_data)

# Commit changes and close connection
conn.commit()
conn.close()