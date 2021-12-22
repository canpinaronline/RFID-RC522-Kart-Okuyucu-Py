# rfidpy

Lang:Py
rfid rc522 card register and attendance with SPI

**LCD Lib**
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
   ogr_sin VARCHAR(1) NOT NULL,
   ogr_bol VARCHAR(5) NOT NULL,
   PRIMARY KEY ( id )
);

create table tbl_admin(  
  id INT(11) NOT NULL,  
  username varchar(250) NOT NULL,  
  password varchar(250) NOT NULL,  
  PRIMARY KEY ( id )  
 ) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;
 
 INSERT INTO `users` (`id`, `username`, `password`) VALUES  
 (1, 'admin', 'admin');  
 
 
 **Veritabanına öğrenci kayıt et.**
 
 -Scriptte ihtiyacımız olan mysql connector pip aracılığıyla kuralım.
 sudo pip3 install mysql-connector-python
 
 -Boş bir klasör oluşturalım.
 
 mkdir ~/yoklamasistemi
 
 Script dosyalrını githubtan çekelim.
 
 git clone https://github.com/canpinaronline/rfidpy.git
 
 
 **Veritabanına örnek öğrencileri kayıt edelim.**
 python3 yoklamasistemi/rfidpy/kart_kayit.py
 
 RFID kartımızı okutalım.
 **Örnek yoklama alalım.**
  python3 yoklamasistemi/rfidpy/yoklama_kayit.py

 **Veritabanını kontrol edelim


 
