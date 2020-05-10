1.Install fixfox
sudo apt update
sudo apt install firefox
---------------------------------------------------------
2.Install python, pip
... ... ... ... ... ...
--------------------------------------------------------
3.install tesseract-ocr-osd

sudo apt update
sudo apt install tesseract-ocr-osd

--------------------------------------------
4.install geckodriver

wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/

----------------------------------------
5.install python package

pip install -r requirements.txt