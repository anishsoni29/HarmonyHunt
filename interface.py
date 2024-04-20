import sys
import logging
import argparse
import fun as f
import convert as c
import database as d
from database import conn


# Interface design

#parser breaks a program into a set of tokens
parser = argparse.ArgumentParser(description='HarmonyHunt : An alternative to Shazam!')
parser.add_argument('-v', '--version', action='version', version='HarmonyHunt 0.5 beta')