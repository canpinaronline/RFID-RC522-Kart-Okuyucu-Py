#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
import Adafruit_CharLCD as LCD

db = mysql.connector.connect(
  host="localhost",
  user="yoklamaadmin",
  passwd="root1479",
  database="yoklamasistemi"
)

cursor = db.cursor()
reader = SimpleMFRC522()
lcd = LCD.Adafruit_CharLCD(4, 24, 23, 17, 18, 22, 16, 2, 4);

try:
  while True:
    lcd.clear()
    lcd.message('Place to\nregister')
    id, text = reader.read()
    cursor.execute("SELECT id FROM users WHERE rfid_uid="+str(id))
    cursor.fetchone()

    if cursor.rowcount >= 1:
      lcd.clear()
      lcd.message("Overwrite\nexisting user?")
      overwrite = input("Overwite (Y/N)? ")
      if overwrite[0] == 'Y' or overwrite[0] == 'y':
        lcd.clear()
        lcd.message("Overwriting user.")
        time.sleep(1)
        sql_insert = "UPDATE users SET name = %s, ogr_sin = %s, ogr_bol = %s  WHERE rfid_uid=%s"
      else:
        continue;
    else:
      sql_insert = "INSERT INTO users (name, rfid_uid, ogr_sin, ogr_bol) VALUES (%s, %s, %s, %s)" #Veritabanındaki kolon isimleri buraya yazılacak.
    lcd.clear()
    lcd.message('Isim giriniz: ')
    new_name = input("Isim: ")
    lcd.clear()
    lcd.message("Sinif giriniz: ")
    ogrenci_sin = input("Sınıf: ")
    lcd.clear()
    ogrenci_bol = input("Bolum giriniz: ")

    cursor.execute(sql_insert, (new_name, ogrenci_sin, ogrenci_bol, id))

    db.commit()

    lcd.clear()
    lcd.message("Ogrenci " + new_name + "\nkaydedildi.")
    time.sleep(2)
finally:
  GPIO.cleanup()

