#!/bin/bash

TOKEN=$1
BUILD_PATH="build"

if [ -z "${TOKEN}" ]; then
  echo 'please pass token as parameter'
  exit 1
fi

git fetch;git reset origin/master  --hard

# Input semantic version

# Activate virtual environment
#source venv/Scripts/activate

# Update version in galaxy.yml
bump2version patch --verbose

VERSION=$(cat marker)

# Build and publish Ansible Galaxy Collection
ansible-galaxy collection build . --force --output-path  ${BUILD_PATH} --timeout 0 --verbose
ansible-galaxy collection publish "${BUILD_PATH}/tocard-utils-${VERSION}.tar.gz" --token "${TOKEN}"

# Create tag and push to Git
git push origin master --tags

# Create a GitHub release and upload the artifact
gh release create "${VERSION}" -n "Release ${VERSION}" -t "${VERSION}" "${BUILD_PATH}/tocard-utils-${VERSION}.tar.gz"

rm *.gz -f
# Deactivate virtual environment (optional, depending on your needs)
#deactivate

