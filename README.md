
Command line tool to deploy IPA package to iOS device.

It was written with nodejs before, now it's re-written with python3.

# Installation #

Please make sure your Python is v3.7 or above.

```bash
python3 --version
python3 -m pip install ipa-deploy
```

Or, clone from GitHub:
```bash
git clone https://github.com/floatinghotpot/ipa-deploy.git
cd ipa-deploy
python3 -m pip install -e .
```

# How To Use #

```bash
ipa-deploy <path_to_ipa_file>
```

Example:
```bash
ipa-deploy myapp.ipa
```

# How It Works #

Here are the steps that the tool actualy runs:

```bash
# unzip the IPA file to tmp folder
mkdir ./tmp
unzip <path_to_ipa_file> -d ./tmp

# run ios-deploy to install the app into iOS device
ios-deploy -b ./tmp/Payload/*.app

# clean up the tmp folder
rm -r ./tmp
```

# Dependency #

It will call [ios-deploy](https://github.com/ios-control/ios-deploy), so make sure it's installed first.

If not installed, install  it with Homebrew:
```bash
brew install ios-deploy
```

# Credits #

A simple tool created by Raymond Xie, to install IPA package with command line.

Any comments are welcome.
