DROP DATABASE IF EXISTS daytripper;

CREATE DATABASE daytripper;

USE daytripper;

CREATE TABLE city
(
	city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(50) NOT NULL
);

INSERT INTO city VALUES (1, 'Boston');

CREATE TABLE feature
(
	feature_id INT PRIMARY KEY AUTO_INCREMENT,
    feature_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(250)
);

CREATE TABLE place
(
	place_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(120) NOT NULL,
    category ENUM('dining','museum','park','landmark','entertainment') NOT NULL,
    type VARCHAR(120) DEFAULT NULL,
    budget ENUM('$', '$$', '$$$','$$$$', '') DEFAULT '',
    rating DOUBLE NOT NULL DEFAULT 3,
    num_reviews INT DEFAULT 0,
    description VARCHAR(250) DEFAULT NULL,
    address VARCHAR(150) DEFAULT NULL,
    latitude DOUBLE NOT NULL,
    longitude DOUBLE NOT NULL,
    city_id INT NOT NULL DEFAULT 1,
    CONSTRAINT place_fk_city
		FOREIGN KEY (city_id)
        REFERENCES city (city_id)
);

CREATE TABLE tag
(
	place_id INT NOT NULL,
    feature_id INT NOT NULL,
    CONSTRAINT tag_fk_place
		FOREIGN KEY (place_id)
        REFERENCES place (place_id),
	CONSTRAINT tag_fk_feature
		FOREIGN KEY (feature_id)
        REFERENCES feature (feature_id)
);


CREATE TABLE user
(
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE itinerary
(
	itinerary_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    description VARCHAR(250),
    CONSTRAINT itinerary_fk_user
		FOREIGN KEY (user_id)
        REFERENCES user (user_id)
);

CREATE TABLE activity
(
	itinerary_id INT NOT NULL,
    place_id INT NOT NULL,
    ordering INT NOT NULL,
    CONSTRAINT activity_fk_itinerary
		FOREIGN KEY (itinerary_id)
        REFERENCES itinerary (itinerary_id),
	CONSTRAINT activity_fk_place
		FOREIGN KEY (place_id)
        REFERENCES place (place_id)
);