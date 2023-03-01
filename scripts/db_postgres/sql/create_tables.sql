-- Creation of audiences table

CREATE TABLE audiences (
    date      DATE             NOT NULL,
    respondent INT             NOT NULL,
    sex        INT             NOT NULL,
    age        INT             NOT NULL,
    weight     NUMERIC         NOT NULL,
    PRIMARY KEY (sex, respondent, date)
);