* smart_agri_iot
    *sensor_id
    *moisture_level
    *date_and_time


* create table smart_agri_iot(sensor_id INT, moisture_level DECIMAL, date_and_time DATETIME);

* insert into smart_agri_iot values(101, 70.30, dt.now());

* insert into smart_agri_iot(sensor_id, moisture_level, date_and_time) values(106, 70.30, dt.now());

* select * from smart_agri_iot;

* update smart_agri_iot SET email = 100, 70.30, dt.now();

* delete from smart_agri_iot where sensor_id = 108;

* To install mysql connector for python
    * pip install mysql-connector-python

* To install flask
    * pip install flask