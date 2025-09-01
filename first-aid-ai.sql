CREATE DATABASE first_aid_ai;

USE first_aid_ai;

CREATE TABLE symptoms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symptom_text TEXT NOT NULL,
    ai_advice TEXT NOT NULL,
    severity VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
