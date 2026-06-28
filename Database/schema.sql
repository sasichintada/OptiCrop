-- ============================================
-- OPTICROP DATABASE SCHEMA
-- ============================================

-- Create User Table
CREATE TABLE User (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('Farmer', 'Researcher', 'Policymaker') DEFAULT 'Farmer',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create SoilData Table
CREATE TABLE SoilData (
    soil_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    nitrogen FLOAT NOT NULL,
    phosphorus FLOAT NOT NULL,
    potassium FLOAT NOT NULL,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    ph FLOAT NOT NULL,
    rainfall FLOAT NOT NULL,
    recorded_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Create Crop Table
CREATE TABLE Crop (
    crop_id INT PRIMARY KEY AUTO_INCREMENT,
    crop_name VARCHAR(50) UNIQUE NOT NULL,
    crop_type VARCHAR(50),
    season VARCHAR(20),
    optimal_ph FLOAT
);

-- Create Prediction Table
CREATE TABLE Prediction (
    prediction_id INT PRIMARY KEY AUTO_INCREMENT,
    soil_id INT,
    crop_id INT,
    confidence FLOAT,
    prediction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (soil_id) REFERENCES SoilData(soil_id),
    FOREIGN KEY (crop_id) REFERENCES Crop(crop_id)
);