echo "setup.sh is called..."
apt-get update

echo "remove mmxlib"
pip uninstall mmxlib -y

echo "install mmxlib for logger test"
pip install git+http://mod.lge.com/hub/mmx/mmx.libs.git@logger