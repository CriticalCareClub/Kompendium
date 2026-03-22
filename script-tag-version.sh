#!/bin/bash

prefix="v"
echo ""
echo "Tagging last commit ..."
echo "======================="
echo ""

echo "Last version: " && git describe

echo -n "Enter you desired new version string (w/o prefix): $prefix" && read version_value


version_string="$prefix$version_value"

echo "creating version tag $version_string ...."

git tag -a "$version_string" -m "$version_string"

echo ""