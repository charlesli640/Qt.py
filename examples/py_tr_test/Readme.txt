Use pyqt5's lupdate to update *.ts
pylupdate5 i18n/tr.pro

Use standard Qt's lrelease to generate *.qm
lrelease i18n/tr.pro


Choose language and install tranlation in python code at run time
Make sure i18n folder contains *.qm and locates in the same folder with test.py

python test.py
