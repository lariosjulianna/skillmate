import mysql.connector

# Establish a connection to your MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="CPSC408!",
    auth_plugin='mysql_native_password'
)

# Establish a connection to MySQL
cursor = conn.cursor()

# Create the database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS YourDatabaseName")
cursor.execute(f"USE YourDatabaseName")

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
    CREATE TABLE IF NOT EXISTS Like (
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
    CREATE TABLE IF NOT EXISTS Match (
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

# Commit changes and close connection
conn.commit()
conn.close()
