""" 
@author: lileilei
@file: url.py 
@time: 2018/5/26 20:36 
"""
from app.views import *
from app import  app
app.add_url_rule('/getbanner',view_func=getbannerView.as_view('getbanner'))
app.add_url_rule('/getyouhui',view_func=getyouhui.as_view('getyouhui'))
app.add_url_rule('/getregood',view_func=getregood.as_view('getregood'))
app.add_url_rule('/getftag',view_func=getfenleif.as_view('getftag'))
app.add_url_rule('/getfengood',view_func=getfengood.as_view('getfengood'))
app.add_url_rule('/getgooddetai',view_func=getgooddetai.as_view('getgooddetai'))
app.add_url_rule('/getguige',view_func=getguige.as_view('getguige'))
app.add_url_rule('/gettuijiangood',view_func=gettuijian.as_view('gettuijiangood'))
app.add_url_rule('/linquyouhui',view_func=linquyouhui.as_view('linquyouhui'))
app.add_url_rule('/huoquding',view_func=huoquding.as_view('huoquding'))
app.add_url_rule('/getaddress',view_func=getaddress.as_view('getaddress'))
app.add_url_rule('/add_address',view_func=Addaddress.as_view('add_address'))
app.add_url_rule('/deleadd',view_func=deleadd.as_view('deleadd'))
app.add_url_rule('/shzm',view_func=shzm.as_view('shzm'))
app.add_url_rule('/addcang',view_func=addcang.as_view('addcang'))
app.add_url_rule('/createorder',view_func=createorder.as_view('createorder'))
app.add_url_rule('/one_add_user',view_func=getdefult.as_view('one_add_user'))
app.add_url_rule('/getgoodyouhui',view_func=getgoodyouhui.as_view('getgoodyouhui'))
app.add_url_rule('/getusercang',view_func=getusercang.as_view('getusercang'))
app.add_url_rule('/getalluserhui',view_func=getalluserhui.as_view('getalluserhui'))