CREATE DATABASE bar_crawl;

USE bar_crawl;

CREATE TABLE bars(id INT PRIMARY KEY AUTO_INCREMENT,
    bar VARCHAR(50),
    vibes INT,
    comments VARCHAR(255)
    );

CREATE TABLE drinks(id INT PRIMARY KEY AUTO_INCREMENT,
    drink VARCHAR(50),
    drink_type VARCHAR(50),
    price DECIMAL(4,2),
    ounces DECIMAL(4,1),
    apv DECIMAL(3,1),
    bar_id INT,
    FOREIGN KEY(bar_id) REFERENCES bars (id)
    );