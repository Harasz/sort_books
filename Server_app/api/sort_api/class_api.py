from sort_api import api, parser
from sort_api.view import appLogin
from sort_api.view import addRe
from sort_api.view import addBook
from sort_api.view import getReaders
from sort_api.view import getBooks
from sort_api.view import addBorrow
from sort_api.view import getBorrows
from sort_api.view import retBook
from sort_api.view import publicKey
from sort_api.view import showComm
from sort_api.view import acceptCom
from sort_api.view import readerInfo
from sort_api.view import readerEdit



class Sort_Books_API(object):


	def __init__(self):

		api.add_resource(appLogin.API_appLogin, '/logaction')
		api.add_resource(addRe.API_addRe, '/addre')
		api.add_resource(addBook.API_addBook, '/addbook')
		api.add_resource(getReaders.API_getReaders, '/getreader')
		api.add_resource(getBooks.API_getBooks, '/getbook')
		api.add_resource(addBorrow.API_addBorrow, '/borrow')
		api.add_resource(getBorrows.API_getBorrows, '/getborrow')
		api.add_resource(retBook.API_retBook, '/retbook')
		api.add_resource(publicKey.API_publicKey, '/key')
		api.add_resource(showComm.API_showComm, '/getcomm')
		api.add_resource(acceptCom.API_acceptCom, '/acceptcom')
		api.add_resource(readerInfo.API_readerInfo, '/userinfo')
		api.add_resource(readerEdit.API_readerEdit, '/useredit')

		parser.add_argument('login', type=str)
		parser.add_argument('pass_', type=str)
		parser.add_argument('key', type=str)
		parser.add_argument('arg1', type=str)
		parser.add_argument('arg2', type=str)
		parser.add_argument('book_id', type=str)
		parser.add_argument('name_id', type=str)
		parser.add_argument('publicKey', type=str)
