-- Creation of audiences table
CREATE TABLE audiences (
    id        INT,
    date      DATE             NOT NULL,
    respondent INT             NOT NULL,
    sex        INT             NOT NULL,
    age        INT             NOT NULL,
    weight     NUMERIC         NOT NULL,
    PRIMARY KEY (sex, respondent, date)
);

COPY audiences (id, date, respondent, sex, age, weight)
FROM '/var/lib/postgresql/csvs/OKKAM_Middle Python Developer_data.csv' DELIMITER ';' CSV HEADER;

ALTER TABLE audiences DROP COLUMN id;
