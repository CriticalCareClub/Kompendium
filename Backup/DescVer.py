#!/bin/python3
# (c) Sebastian GABRIEL

"""
DescVer handles Descriptive Versioning information and can derive versioning information in git repositories automatically using git-describe.

Version 0.0.2
"""
import sys
import os
import re
from git import Repo
from git.cmd import Git


def convertGitDescribe(
	git_repo:Repo,
	flag_development:str = "DEVELOPMENT",
	flag_git:str = "git",
	flag_branch:str = "branch",
	flag_dirty:str = "DIRTY" ):
	'''
	Takes git repo and converts git-describe from HEAD, returns formated string (<major>.<minor>.<patch>.<misc>-<prerelease>+<upcount>#branch=<branch>.git=<hash>).

	Beware: Pre-existing <upcount> is resetted and <metadata> is stripped!
	'''

	formatted_version_string = None
	git                      = git_repo.git
	regexp                   = re.compile('v(\d+).(\d+).(\d+)(.(\d+))?(-([\w\d]+(([\w\d\.]))*[\w\d])*)?((\!([\w\d]+(([\w\d\.]))*[\w\d]))*)?(\#([\w\d]+(([\w\d\=\.])*[\w\d]))*)?(-(\d+))(-g([0-9a-fA-F]+))')


	try:
		git_description = str(git.execute(["git", "describe" , "--dirty"]))
	except:
		print ("Can not get git description!")
		raise

	print("Git description: " + git_description)

	version_regexped = re.search(regexp, git_description)

	# Do we have pre-existing Caveats?

	if version_regexped.group(12): # caveat
		caveat = str(version_regexped.group(12))
	else:
		caveat = None

	if version_regexped.group(20): # if upcount, add caveat "DEVELEOPMENT"
		if caveat:   # if we have pre-existings caveats ...
			caveat += "." + flag_development # ... append to caveats ...
		else:
			caveat = flag_development # ... otherwise set
	# Is workind dir dirty?

	if git_repo.is_dirty:
		if caveat:   # if we have pre-existings caveats ...
			caveat += "." + flag_dirty # ... append dirty to caveats ...
		else:
			caveat = flag_dirty # ... otherwise set do DIRTY

	formatted_version_string = (
		str(version_regexped.group(1)) +  # "major"
		"." +
		str(version_regexped.group(2)) +  # "minor"
		"." +
		str(version_regexped.group(3))   # "patch"
	)
	if version_regexped.group(5): # "misc"
		formatted_version_string += "." + str(version_regexped.group(5))
	if version_regexped.group(7): # "prerelease"
		formatted_version_string += "-" + str(version_regexped.group(7))
	if version_regexped.group(20): # "upcount"
		formatted_version_string += "+" + str(version_regexped.group(20))
	if caveat: # "caveat"
		formatted_version_string += "!" + caveat
	try:
		active_branch = str(git_repo.active_branch)
	except:
		active_branch = "NOBRANCH"

	if version_regexped.group(22): # "hash"
		formatted_version_string += (
			"#" +
			flag_branch +
			"=" +
			active_branch +
			"." +
			flag_git +
			"=" +
			str(version_regexped.group(22))
		)

	assert formatted_version_string, "formatted string is still empty!"

	return(formatted_version_string)

def parseVersionString(string:str):
	"""
	Takes a string and returns a list with version segment values:

	major, minor, patch, prerelease, upcount, caveat, metadata

	"""

	version_re = re.compile('(\d+)\.(\d+)\.(\d+)(\.(\d+))?(-([\w\d]([\w\d\.][\w\d])*))?(\!([\w\d](([\w\d\.])+[\w\d])*))?(\+(\d+)?(\!([\w\d]([\w\d\.])*[\w\d]))*)?(\#([\w\d](([\w\d\=\.])*[\w\d]))*)?')

	assert version_re.search(string), "Version string validation failed!"

	version_regexped = re.search(version_re, string)

	my_version = [
		version_regexped.group(1),  # "major" :
		version_regexped.group(2),  # "minor" :
		version_regexped.group(3),  # "patch" :
		version_regexped.group(5),  # "misc" :
		version_regexped.group(7),  # "prerelease" :
		version_regexped.group(14),  # "upcount" :
		version_regexped.group(16), # "caveat" :
		version_regexped.group(19) # "metadata" :
	]
	return(my_version)