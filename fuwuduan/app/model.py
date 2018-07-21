""" 
@author: lileilei
@file: model.py 
@time: 2018/5/26 20:36 
"""
from app import  db
from datetime import datetime
rely_case=db.Table('cartgood',
                   db.Column('goods_id',db.Integer(),db.ForeignKey('goods.id')),
                    db.Column('carts_id', db.Integer(), db.ForeignKey('carts.id')),
                   db.Column('num',db.Integer()),
                   db.Column('guige',db.String())
                   )
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username=db.Column(db.String(252),unique=False)
    status=db.Column(db.Boolean(),default=False)
    level=db.Column(db.Integer(),default=0)
    iphone=db.Column(db.Integer(),default=0)
    yue=db.Column(db.Integer(),default=0)
    weixinid=db.Column(db.String())
    last_login_ip=db.Column(db.String())
    last_login_time=db.Column(db.DateTime(),default=datetime.now())
    register_time=db.Column(db.DateTime())
    def __repr__(self):
        return self.username
class Baner(db.Model):
    __tablename__ = 'baners'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name=db.Column(db.String())
    img=db.Column(db.String())
    is_fa=db.Column(db.Boolean(),default=False)
    status=db.Column(db.Boolean(),default=False)
    make=db.Column(db.Integer(),db.ForeignKey('users.id'))
    def __repr__(self):
        return  self.name
class classtag(db.Model):
    __tablename__ = 'classtags'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name=db.Column(db.String(),unique=False)
    status=db.Column(db.Boolean(),default=False)
    leve=db.Column(db.String(),default='L1')
    desc=db.Column(db.String())
    pid=db.Column(db.Integer(),db.ForeignKey('classtags.id'),nullable=True)
    icon=db.Column(db.String())
    def __repr__(self):
        return  self.name
class good(db.Model):
    __tablename__='goods'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    goodname=db.Column(db.String())
    gooddesc=db.Column(db.String())
    desc=db.Column(db.String())
    pic_url=db.Column(db.String())
    cellnum=db.Column(db.Integer())
    classtag=db.Column(db.Integer(),db.ForeignKey('classtags.id'))
   # is_you=db.Column(db.Boolean(),default=False)
    kucun=db.Column(db.Integer())
    is_cell=db.Column(db.Boolean(),default=False)
    addtime=db.Column(db.DateTime())
    xiutime=db.Column(db.DateTime(),default=datetime.now())
    yuanjia=db.Column(db.Integer())
    xianjian=db.Column(db.String())
    is_huo=db.Column(db.Boolean(),default=False)
    is_re=db.Column(db.Boolean(),default=False)
    is_tuijian=db.Column(db.Boolean(),default=False)
    is_fenx=db.Column(db.Boolean(),default=False)
    status=db.Column(db.Boolean(),default=False)
    def __repr__(self):
        return  self.goodname
class goodimg(db.Model):
    __tablename_='goodimgs'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    url=db.Column(db.String())
    desc=db.Column(db.String(64))
    types=db.Column(db.String(8))
    good=db.Column(db.Integer(),db.ForeignKey('goods.id'))
    def __repr__(self):
        return  str(self.id)
class goodguige(db.Model):
    __tablename__='goodguiges'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    good = db.Column(db.Integer(), db.ForeignKey('goods.id'))
    guige=db.Column(db.String(32))
    value=db.Column(db.String(32))
    pic_url=db.Column(db.String(32))
    atter=db.Column(db.Integer(),db.ForeignKey('goodatters.id'))
    def __repr__(self):
        return str(self.id)
class goodatter(db.Model):
    __tablename__ = 'goodatters'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    good = db.Column(db.Integer(), db.ForeignKey('goods.id'))
    attersid=db.Column(db.Integer(),db.ForeignKey('attres.id'))
    value=db.Column(db.String())
    def __repr__(self):
        return str(self.id)
class  attres(db.Model):
    __tablename__ = 'attres'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name=db.Column(db.String())
    tag=db.Column(db.Integer(),db.ForeignKey('atterstags.id'))
    def __repr__(self):
        return str(self.id)
class atterstag(db.Model):
    __tablename__ = 'atterstags'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    def __repr__(self):
        return str(self.id)
class cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user=db.Column(db.Integer(),db.ForeignKey('users.id'))
    jiatime=db.Column(db.DateTime())
    rely = db.relationship('good', secondary=rely_case,
                           backref=db.backref('carts', lazy='dynamic'),
                           lazy='dynamic')
    def __repr__(self):
        return  str(self.id)
class youhui(db.Model):
    __tablename__ = 'youhuis'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name=db.Column(db.String())
    man_num=db.Column(db.Integer())
    jian_num=db.Column(db.Integer())
    dazhe=db.Column(db.String())
    good=db.Column(db.Integer(),db.ForeignKey('goods.id'))
    classtags=db.Column(db.Integer(),db.ForeignKey('classtags.id'))
    lingqu=db.Column(db.Integer())
    endtime=db.Column(db.DateTime(),default=datetime.now())
    status=db.Column(db.Boolean(),default=False)
    is_die=db.Column(db.Boolean(),default=False)
    type=db.Column(db.Integer(),default=1)
    def __repr__(self):
        return  self.name
class adderss(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    address=db.Column(db.String())
    user=db.Column(db.String())
    userphone=db.Column(db.Integer())
    jiehuo=db.Column(db.String())
    jointime=db.Column(db.DateTime(),default=datetime.now())
    xiugaitime=db.Column(db.DateTime())
    is_moren=db.Column(db.Boolean(),default=False)
    status=db.Column(db.Boolean(),default=False)
    relation=db.Column(db.Integer(),db.ForeignKey('users.id'))
    def __repr__(self):
        return  str(self.id)
class order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    ordenum=db.Column(db.String())
    orderdesc=db.Column(db.String())
    address=db.Column(db.Integer(),db.ForeignKey('address.id'))
    kuaidi=db.Column(db.Integer(),db.ForeignKey('kuaidis.id'))
    xiadan=db.Column(db.DateTime(),default=datetime.now())
    zhifutype=db.Column(db.Integer())
    shi_zhifu=db.Column(db.Boolean(),default=False)
    zhifushijian=db.Column(db.DateTime(),default=datetime.now())
    zhifujine=db.Column(db.String())
    oreder_user=db.Column(db.Integer(),db.ForeignKey('users.id'))
    zhangtai=db.Column(db.String(64),default='未支付')
    is_fa=db.Column(db.Boolean(),default=False)
    is_shou=db.Column(db.Boolean(),default=False)
    is_tui=db.Column(db.Boolean(),default=False)
    is_ping=db.Column(db.Boolean(),default=False)
    yundamhao=db.Column(db.String())
    def __repr__(self):
        return  self.ordenum
class ordergood(db.Model):
    __tablename__ = 'ordergoods'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    good=db.Column(db.Integer(),db.ForeignKey('goods.id'))
    order=db.Column(db.Integer(),db.ForeignKey('orders.id'))
    num=db.Column(db.Integer())
    guige=db.Column(db.String(32))
    value=db.Column(db.String(32))
    def __repr__(self):
        return str(self.id)
class shoucang(db.Model):
    __tablename__ = 'shoucangs'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user=db.Column(db.Integer(),db.ForeignKey('users.id'))
    shoucangtime=db.Column(db.DateTime(),default=datetime.now())
    good=db.Column(db.Integer(),db.ForeignKey('goods.id'))
    cellnum=db.Column(db.Integer())
    def __repr__(self):
        return str(self.id)
class comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    good=db.Column(db.Integer(),db.ForeignKey('goods.id'))
    user=db.Column(db.Integer(),db.ForeignKey('users.id'))
    time=db.Column(db.DateTime(),default=datetime.now())
    ping=db.Column(db.String())
    pid=db.Column(db.Integer(),db.ForeignKey('comments.id'),nullable=True)
    def __repr__(self):
        return str(self.id)
class prover(db.Model):
    __tablename__ = 'provers'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name=db.Column(db.String())
    type=db.Column(db.String())
    pid=db.Column(db.Integer(),db.ForeignKey('provers.id'),nullable=True)
    def __repr__(self):
        return  self.name
class kuaidi(db.Model):
    __tablename__ = 'kuaidis'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name=db.Column(db.String())
    code=db.Column(db.String(32))
    def __repr__(self):
        return  self.name
class useryou(db.Model):
    __tablename__='useryous'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user=db.Column(db.Integer(),db.ForeignKey('users.id'))
    youh=db.Column(db.Integer(),db.ForeignKey('youhuis.id'))
    lingqu=db.Column(db.DateTime(),default=datetime.now())
    num=db.Column(db.Integer())
    is_use=db.Column(db.Boolean(),default=False)
    user_time=db.Column(db.DateTime())
    def __repr__(self):
        return  str(self.id)