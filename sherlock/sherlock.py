# This file used to trigger updates on packages too out of date
# to use the new release tag format. Remove in next update.
__version__ = "0.15.0"
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
virtualenv .
source bin/activate
sherlock 42_vxw
