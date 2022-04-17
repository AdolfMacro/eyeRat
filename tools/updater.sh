crd=pwd
cd /tmp/
git clone https://github.com/adolfmacro/eyeRat.git
sudo -u root cp -R eyeRat/* /usr/src/eyerat/
sudo -u root rm -rf eyeRat
cd $prc