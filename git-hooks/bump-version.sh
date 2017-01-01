#!/bin/sh

# Bumps the version number to relevant files at the end of any release and hotfix start
#
# Positional arguments:
# $1 The version (including the version prefix)
# $2 The origin remote
# $3 The full branch name (including the release prefix)
# $4 The base from which this release is started
#
# The following variables are available as they are exported by git-flow:
#
# MASTER_BRANCH - The branch defined as Master
# DEVELOP_BRANCH - The branch defined as Develop

VERSION=$1

# Remove v prefix (if present)
VERSION=${VERSION#"v"}

ROOTDIR=$(git rev-parse --show-toplevel)

# Bump package.version
sed -i.bak 's/^\( *\)"version": .*/\1"version": "'$VERSION'",/' $ROOTDIR/package.json
rm $ROOTDIR/package.json.bak

# Rebuild datasets
python scripts/generate.py

# Commit changes
git commit -a -m "Version bump $VERSION"


exit 0
