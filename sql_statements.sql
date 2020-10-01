create table raw_features 
(
  id integer NOT NULL AUTO_INCREMENT, 
  created_at timestamp default current_timestamp, 
  raw_features JSON,
  PRIMARY KEY (id)
);

INSERT INTO raw_features (raw_features) VALUES ('{"median_age": 101}');

drop table raw_features;

--docker run --name=root --env="MYSQL_ROOT_PASSWORD=my-secret-pw" -p 3306:3306 -d mysql:8.0.21

create table house_information 
(
  id integer NOT NULL AUTO_INCREMENT, 
  uuid varchar(100) NOT NULL,
  created_at timestamp default current_timestamp, 
  house_description JSON,
  PRIMARY KEY (id)
);

DELIMITER ;;
CREATE TRIGGER before_insert_house_information
BEFORE INSERT ON house_information
FOR EACH ROW
BEGIN
  IF new.uuid IS NULL THEN
    SET new.uuid = uuid();
  END IF;
END
;;
