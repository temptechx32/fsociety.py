echo "Please Wait while Its Installing techx-shell"
git clone https://github.com/temptechx32/fsociety.py.git ~/txshell

mkdir ~/txshell

cd ~/txshell
sudo mv src/TXSH/txsh /usr/local/bin/

cd /usr/local/bin/
chmod +x txsh

sudo rm -rf ~/txshell

echo "Install Done"
txsh
