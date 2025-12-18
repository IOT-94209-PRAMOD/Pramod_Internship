
*iot_sen
    *id
    *temperature
    *humidity
    *timestamp

* create table iot_sen(id INT, temperature DECIMAL,humidity DECIMAL, timesamp DATETIME);

* insert into iot_sen values(1, 30.35, 76.25, 2025-01-10 08:00:00);

* insert into sen_iot(id, temperature, humidity, timesamp) values(1, 30.35, 76.25, 2025-01-10 08:00:00);

* select * from sen_iot;

* update sen_iot SET id = "12" where temperature = "36.56";

* delete from sen_iot where id = 12;

* To install mysql connector for python
    * pip install mysql-connector-python

* To install flask
    * pip install flask