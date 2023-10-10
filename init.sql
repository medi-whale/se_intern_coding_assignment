CREATE TABLE images (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    patient_id VARCHAR(255) NOT NULL,
    exam_date DATE,
    laterality VARCHAR(1)
);
