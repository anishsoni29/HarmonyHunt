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
parser.add_argument('-vb', '--verbose', action='store_true', help='switch between log levels')

#subcommands
subparser = parser.add_subparsers(dest='subcommands')
#add
parser_add = subparser.add_parser('add', help='add a song to the database')
parser_add.add_argument('--pathfile', type = str, help='pathfile to the song')

#update (modify song info)
parser_update = subparser.add_parser('update', help='update metadata of a song')
parser_update.add_argument('title',type=str, help='song title') 
parser_update.add_argument('--artist', type=str, help='song artist')
parser_update.add_argument('--album', type=str, help='album of the song')

#remove
parser_remove = subparser.add_parser('remove', help='remove a song from the database')
parser_remove.add_argument('title', type=str, help='song title')

#construct (insert an entire directory for database construction)
parser_fun = subparser.add_parser('construct', help='construct the database at 1-click')

#identity
parser_identity = subparser.add_parser('identity', help='identify a snippet ')
parser_identity.add_argument('--pathfile', type = str, help='pathfile to the snippet')
parser_identity.add_argument('--type', type = int, help='1 or 2, fingerprint method for identification of a song')

#admin
parser_admin = subparser.add_parser('admin', help = 'administrator mode, cleanup database etc.')
parser_admin.add_argument('--action', type=str, help='rm_dup - remove duplicates from the database')

#list
parser_list = subparser.add_parser('list', help = 'list of all songs in database')

args = parser.parse_args()


#LOG SETUP

#set up logging to file
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='shazam.log',
                    filemode='w')

#define a Handler which writes WARNING messages or higher to the sys
console = logging.StreamHandler(sys.stdout)

#set log level by verbose
if args.verbose:
    console.setLevel(logging.DEBUG)
else:
    console.setLevel(logging.WARNING)
    
formatter = logging.Formatter('%(levelname)-8s %(message)s')
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger().addHandler(console)

log = logging.getLogger(__name__)
