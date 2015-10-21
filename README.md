# ipa-deploy #

Deploy .ipa package to iOS device

# Dependency

* Mac OS
* ios-deploy, use it to install .app to iOS device, install it: ```[sudo] npm install -g ios-deploy```
* unzip, use it to unzip .ipa file.

# Install

```bash
[sudo] npm install -g ipa-deploy
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
cd ./tmp
unzip <path_to_ipa_file>

# run ios-deploy to install the app into iOS device
ios-deploy -b ./Payload/*.app

# clean up the tmp folder
cd ..
rm -r ./tmp
```

# Credits #

A simple tool created by Raymond Xie, to install IPA package with command line.

Any comments are welcome.
