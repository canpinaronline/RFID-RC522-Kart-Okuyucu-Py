# rfidpy

Lang:Py


**Raspbbery Pi GPIO kurulmunu yapalım**
-sudo pip3 install RPi.GPIO

**SPI Aktif et.**

sudo raspi-config
Interfacing options -> SPI -> Enable (Yes)

**Restart**

sudo reboot

**SPI Aktiflik Kontrol**

lsmod | grep spi

**RFID lib**

sudo pip3 install mfrc522

**Database settings**

1)**Install mariadb server**
sudo apt install mariadb-server
sudo mysql_secure_installation
Y > Y > Y > Y

2)Root olma
sudo mysql -u root -p
! 1. adımda girilen şifreyi isteyecektir. Şifreyi girelim.

3) Database oluşturalım.
CREATE DATABASE yoklamasistemi;

4) Database yoneticisi oluşturalım.
CREATE USER 'yoklamaadmin'@'localhost' IDENTIFIED BY 'root1479';

5) Oluşturduğuumz kullanıcının veritabanına erişmesine izin verelim.
GRANT ALL PRIVILEGES ON yoklamasistemi.* TO 'yoklamaadmin'@'localhost';

6) Veritabanına geçiş yapalım.
use yoklamasistemi;

create table attendance(
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
   user_id INT UNSIGNED NOT NULL,
   clock_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( id )
);

create table users(
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
   rfid_uid VARCHAR(255) NOT NULL,
   name VARCHAR(255) NOT NULL,
   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   ogr_sin VARCHAR(255) NOT NULL,
   ogr_bol VARCHAR(255) NOT NULL,
   PRIMARY KEY ( id )
);

create table tbl_admin(  
  id INT(11) NOT NULL,  
  username varchar(250) NOT NULL,  
  password varchar(250) NOT NULL,  
  PRIMARY KEY ( id )  
 ) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;
 
 INSERT INTO tbl_admin (`id`, `username`, `password`) VALUES  
 (1, 'admin', 'admin');  
 
 
 **Veritabanına öğrenci kayıt et.**
 
 -Scriptte ihtiyacımız olan mysql connector pip aracılığıyla kuralım.
 sudo pip3 install mysql-connector-python
 
 -Boş bir klasör oluşturalım.
 
 mkdir ~/yoklamasistemi
 
 Script dosyalrını githubtan çekelim.
 
 sudo git clone https://github.com/canpinaronline/rfidpy.git
 
 
 **Veritabanına örnek öğrencileri kayıt edelim.**
 python3 yoklamasistemi/rfidpy/kart_kayit.py
 RFID kartımızı okutalım.
 
**Örnek yoklama alalım.**
  python3 yoklamasistemi/rfidpy/yoklama_kayit.py

**Veritabanını kontrol edelim**
Root olarak giriş yapalım.

sudo mysql -u root -p
use yoklamasistemi;

**Sisteme kayıtlı kullanıcıları görüntüleyelim.**
SELECT * FROM USERS;
+--+------------------+---------+------------------------+
| id | rfid_uid       | name    | created                |
+--+------------------+---------+------------------------+
|  1 | 496840744001   | Testing User   | 2021-12-22 22:34:06    |
+--+------------------+---------+------------------------+

**Yoklama listesini görelim.**
 SELECT * FROM attendance;
 
 
 Raspbbery Pi üzerine apache sunucusunu ve php7'yi kuralım.
 
 **Local web sunucu dosyalarının bulunduğu dizine yeni klasör oluşturalım.**
 
 sudo  mkdir /var/www/html/yoklamasistemi
 
**Daha önce hazırladığım ayarlamaları yaptığım dosyaları github üzerinden çekiyorum.**

sudo git clone https://github.com/canpinaronline/rfidfe.git /var/www/html/yoklamasistemi

**Web sunucumuza giriş yapalım.**
Cihazın ip adresini öğrenmek için ip -4 addr komutunu terminale yazıyorum. Terminaldeki ipv4 adresi ile yerel sunucuma giriş yapıyorum.
**Localde çalıştığı için Raspbbery PI cihazımın IP adresiyle giriş yapıyorum.**

