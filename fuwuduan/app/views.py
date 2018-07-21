""" 
@author: lileilei
@file: views.py 
@time: 2018/5/26 20:36 
"""
from app.model import  *
from config import appid,selseid
import  requests,json,time,random
from flask import  jsonify,request
from flask.views import  MethodView
from datetime import datetime
class getbannerView(MethodView):
    def get(self):
        banner=Baner.query.filter_by(status=False).all()
        list_banner=[]
        for item in banner:
            list_banner.append({'img':item.img})
        return  jsonify({'code':200,'data':list_banner})
class getregood(MethodView):
    def get(self):
        goos=good.query.filter_by(status=False,is_re=True).all()
        back=[]
        for item in goos:
            img=goodimg.query.filter_by(good=item.id).first()
            back.append({'xianjian':item.xianjian,'name':item.goodname,'img':img.url,'id':item.id})
        return  jsonify({'code':200,'good':back})
class gettuijian(MethodView):
    def get(self):
        goos = good.query.filter_by(status=False, is_tuijian=True).all()
        back = []
        for item in goos:
            img = goodimg.query.filter_by(good=item.id).first()
            if img is None:
                back.append({'gooddesc': item.gooddesc, 'name': item.goodname, 'img': '', 'id': item.id})
            else:
                back.append({'gooddesc': item.gooddesc, 'name': item.goodname, 'img': img.url, 'id': item.id})
        return jsonify({'code': 200, 'good': back})
class getyouhui(MethodView):
    def get(self):
        youhuis=youhui.query.filter_by(status=False).all()
        bask=[]
        for item in youhuis:
            if item.type==3:
                pass
            elif item.type==2:
                tas=classtag.query.filter_by(id=item.classtags).first()
                bask.append({'man_num':item.man_num,'lingqu':item.lingqu,'endtime':item.endtime.strftime('%Y-%m-%d'),'id':item.id,'cate':tas.name,'jian_num':item.jian_num})
            else:
                bask.append({'man_num': item.man_num, 'lingqu': item.lingqu, 'endtime': item.endtime.strftime('%Y-%m-%d'), 'id': item.id,
                             'cate': True,'jian_num':item.jian_num})
        return  jsonify({'code':200,'data':bask})
class getfenleif(MethodView):
    def get(self):
        tasg=classtag.query.filter_by(id=1).first()
        tag=classtag.query.filter_by(pid=tasg.id).all()
        data=[]
        for item in tag:
            data.append({'id':item.id,'name':item.name})
        return  jsonify({'code':200,'data':data})
    def post(self):
        f=request.get_json('fenlei')['fenlei']
        tag=classtag.query.filter_by(name=f,status=False).first()
        tags=classtag.query.filter_by(pid=tag.id,status=False).all()
        data=[]
        for item in tags:
            data.append({'id':item.id,'name':item.name,'icon':item.icon})
        data={'data':data,'banner':tag.icon}
        return  jsonify({'code':200,'data':data})
class getfengood(MethodView):
    def post(self):
        f=request.get_json('id')['id']
        tag=classtag.query.filter_by(id=f,status=False).first()
        navlist=classtag.query.filter_by(pid=tag.pid,status=False).all()
        data_nav=[]
        for i in navlist:
            data_nav.append({'id':i.id,'name':i.name})
        goods=good.query.filter_by(classtag=tag.id,status=False).all()
        goodlist=[]
        for item in goods:
            img=goodimg.query.filter_by(good=item.id).first()
            if img is None:
                goodlist.append({'name': item.goodname, 'xianjian': item.xianjian, 'id': item.id, 'icon':''})
            else:
                goodlist.append({'name':item.goodname,'xianjian':item.xianjian,'id':item.id,'icon':img.url})
        return  jsonify({'code':200,'data':data_nav,'good':goodlist})
class getgooddetai(MethodView):
    def post(self):
        try:
            goodid=request.get_json('id')['id']
        except:
            return jsonify({'code':197,'data':'获取信息失败'})
        goods=good.query.filter_by(id=goodid,status=False,is_cell=True).first()
        goodimgs=goodimg.query.filter_by(good=goods.id).all()
        comments=comment.query.filter_by(good=goods.id).all()
        gooda_ttres = goodatter.query.filter_by(good=goods.id).all()
        atter_dss = []
        for att in gooda_ttres:
            attr_is = attres.query.filter_by(id=att.attersid).first()
            atter_dss.append({'name': attr_is.name, 'vlaue': att.value})
        goode={}
        goode['id']=goods.id
        goode['name']=goods.goodname
        goode['gooddesc']=goods.gooddesc
        goode['desc']=goods.desc
        goode['kucun']=goods.kucun
        goode['xiaoliang']=goods.cellnum
        goode['xianjian']=goods.xianjian
        goode['pic_url']=goods.pic_url
        youhuilist = []
        if goods.is_huo is True:
            youhuis = youhui.query.filter_by(good=goods.id).all()
            for item in youhuis:
                youhuilist.append({'name':item.name,'id':item.id})
        imglist=[]
        for img in goodimgs:
            if int(img.types)==1:
                imglist.append({"url":img.url})
            else:
                goode['jianjie']=img.url
        commnetslist=[]
        for commen in comments:
            commnetslist.append({"user":commen.user.username,'neirong':commen.ping,'time':commen.time.strftime('%Y-%m-%d')})
        return jsonify({'code':200,'good':goode,'img':imglist,'comment':commnetslist,"youhui":youhuilist,'atterdss':atter_dss})
class getguige(MethodView):
    def post(self):
        try:
            goodid = request.json['id']
        except Exception as e:
            jsonify({'code':198,'data':'获取信息失败'})
        goods = good.query.filter_by(id=goodid, status=False, is_cell=True).first()
        guige=goodguige.query.filter_by(good=goods.id).all()
        yanselist=[]
        guigelist=[]
        for item in guige:
            if item.guige=="颜色":
                yanselist.append({'guige':item.value,'icon':item.pic_url})
            else:
                guigelist.append({'guige':item.value})
        return jsonify({'code':200,'guige':guigelist,'yanse':yanselist})
def jianuser(userin,usercode):
    url='https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code'%(appid,selseid,usercode)
    f=requests.get(url=url)
    if userin == None  or usercode is None:
        return False
    else:
        try:
            openid=f.json()['openid']
            user_is = User.query.filter_by(weixinid=openid, username=userin, status=False).first()
            if not user_is:
                user_is = User(username=userin, weixinid=openid,register_time=datetime.now())
                db.session.add(user_is)
                db.session.commit()
            userid=user_is.id
            return {'userid':userid}
        except Exception as e:
            return False
class linquyouhui(MethodView):
    def post(self):
        userin = request.json['username']
        usercode = request.json['usercode']
        id_youhui=request.json['id']
        f=jianuser(userin,usercode)
        if f is False:
            return jsonify({'code': 202, 'data': '领取失败'})
        else:
            user=User.query.filter_by(id=f['userid'],status=False,username=userin).first()
            youhui_is=youhui.query.filter_by(id=id_youhui).first()
            user_you=useryou.query.filter_by(user=user.id,youh=youhui_is.id,is_use=False).all()
            if len(user_you)<=0:
                new=useryou(user=user.id,youh=youhui_is.id,num=1)
                db.session.add(new)
                db.session.commit()
                return jsonify({'code': 200,'data':'领取成功','id':user.id})
            else:
                if youhui_is.is_die==False:
                    return jsonify({'code':201,'data':'你用这种优惠券还没有使用','id':user.id})
                else:
                    new = useryou(user=user.id, youh=youhui_is.id, num=1)
                    db.session.add(new)
                    db.session.commit()
                    return jsonify({'code': 200, 'data': '领取成功','id':user.id})
class huoquding(MethodView):
    def post(self):
        try:
            id=request.json['id']
        except Exception as e:
            return jsonify({'code': 210,'data':'获取用户信息'})
        usercode=request.json['usercode']
        usernickname=request.json['usernickname']
        if id is None:
            f=jianuser(usernickname,usercode)
            if f is False:
                return jsonify({'code': 211,'data':'用户查询失败'})
            else:
                id=f['userid']
        user=User.query.filter_by(id=id,status=False).first()
        ding=order.query.filter_by(oreder_user=user.id).all()
        if len(ding)<1:
            return jsonify({'code':212,'data':'用户没有订单'})
        else:
            data_ding=[]
            for item in ding:
                add=adderss.query.filter_by(id=item.address,status=False).first()
                kuadi=kuaidi.query.filter_by(id=item.kuaidi).first()
                if kuadi is None:
                    kadiname=''
                else:
                    kadiname=kuaidi.name
                goods=ordergood.query.filter_by(order=item.id).all()
                good_ordesr=[]
                num=0
                for gooditem in goods:
                    good_one=good.query.filter_by(id=gooditem.good).first()
                    num+=gooditem.num
                    img=goodimg.query.filter_by(good=good_one.id).first()
                    good_ordesr.append({'good_id':good_one.id,'goodname':good_one.goodname,'good_img':img.url,
                                        'num':gooditem.num,'guige':gooditem.guige,'value':gooditem.value,'id':good_one.id,
                                        'yuanjia':good_one.yuanjia})
                data_ding.append({'ordenum':item.ordenum,'address':add.id,
                                  'kuaidi':kadiname,'xiadan':item.xiadan,'zhangtai':item.zhangtai,
                                  'yundamhao':item.yundamhao,'is_fa':item.is_fa,'is_shou':item.is_shou,
                                  'is_ping':item.is_ping,'zhifushijian':item.zhifushijian,
                                  'zhifujine':item.zhifujine,'shi_zhifu':item.shi_zhifu,
                                  'shouuser':add.user,'shouiphone':add.userphone,
                                  'id':item.id,'good_ordesr':good_ordesr,'total':num})
            return  jsonify({'code':200,'data':data_ding})
class getaddress(MethodView):
    def post(self):
        try:
            id = request.json['id']
        except:
            id=None
        usercode = request.json['usercode']
        usernickname = request.json['usernickname']
        if id is None:
            f = jianuser(usernickname, usercode)
            if f is False:
                return jsonify({'dcode':'211', 'data': '用户查询失败'})
            else:
                id = f['userid']
        user = User.query.filter_by(id=id, status=False).first()
        adderss_list=adderss.query.filter_by(relation=user.id,status=False).all()
        if len(adderss_list)<=0:
            return jsonify({'dcode':'213', 'data': '没有获取到收获地址，请添加','id':user.id})
        else:
            add_list=[]
            for item in adderss_list:
                add_list.append({'address':item.address,'user':item.user,'userphone':item.userphone,
                                 'jiehuo':item.jiehuo,'is_moren':item.is_moren,'id':item.id,'userid':item.relation})
            return jsonify({'dcode':'200', 'data':add_list,'id':user.id})
class Addaddress(MethodView):
    def post(self):
        data=json.loads(request.data.decode('utf-8'))
        try:
            id=data['id']
        except Exception as e:
            return jsonify({'code': 212,'data':'获取信息失败'})
        username=data['usernickname']
        usercode=data['usercode']
        shouname=data['name']
        shouphone=data['phone']
        shoudizhi=data['dizhi']
        if id==None or id =='':
            return_jian=jianuser(userin=username,usercode=usercode)
            if return_jian==False:
                return jsonify({'code': 213,'data':'检验用户失败，无法添加'})
            else:
                userid=return_jian['userid']
        else:
            userid=id
        user_add=User.query.filter_by(id=userid,status=False).first()
        if not  user_add:
            return jsonify({'code': 217, 'data': '检验用户失败，无法添加'})
        try:
            shouphone=int(shouphone)
        except:
            return jsonify({'code': 218, 'data': '收获号码必须是数字'})
        if shouname=='':
            return jsonify({'code': 219, 'data': '收货名字不能为空'})
        if shoudizhi=='':
            return jsonify({'code': 220, 'data': '收货地址不能为空'})
        new_add=adderss(relation=user_add.id,userphone=shouphone,user=shouname,address=shoudizhi)
        db.session.add(new_add)
        db.session.commit()
        return jsonify({'code':200,'data':'添加成功'})
class deleadd(MethodView):
    def post(self):
        data = json.loads(request.data.decode('utf-8'))
        try:
            id = data['id']
            userid = data['userid']
        except Exception as e:
            return jsonify({'code': 231, 'data': '删除失败，获取信息失败'})        
        user=User.query.filter_by(id=userid,status=False).first()
        if not user:
            return jsonify({'code': 231, 'data': '删除失败，用户不存在'})
        id_add=adderss.query.filter_by(id=id,status=False).first()
        if not id_add:
            return jsonify({'code': 232, 'data': '删除失败，找不到你编辑的地址'})
        if id_add.relation!=user.id:
            return jsonify({'code': 233, 'data': '删除失败，用户信息不匹配'})
        id_add.status=True
        db.session.commit()
        return jsonify({'code': 200, 'data': '删除成功'})
class shzm(MethodView):
    def post(self):
        data = json.loads(request.data.decode('utf-8'))
        try:
            id = data['id']
            userid = data['userid']
        except Exception as e:
            return jsonify({'code': 231, 'data': '设置失败，获取信息失败'})  
        user = User.query.filter_by(id=userid, status=False).first()
        if not user:
            return jsonify({'code': 233, 'data': '设置失败，用户不存在'})
        id_add = adderss.query.filter_by(id=id, status=False).first()
        if not id_add:
            return jsonify({'code': 234, 'data': '设置失败，找不到你编辑的地址','id':user.id})
        id_mo_add=adderss.query.filter_by(status=False,is_moren=True).first()
        if not  id_mo_add:
            id_add.is_moren=True
            db.session.commit()
            return jsonify({'code': 200, 'data': '设置默认成功','you':True,'id':user.id})
        else:
            id_mo_add.is_moren=False
            id_add.is_moren=True
            db.session.commit()
            return jsonify({'dcode': 200, 'data': '设置默认成功', 'you': False,'id':user.id})
class addcang(MethodView):
    def post(self):
        data = json.loads(request.data.decode('utf-8'))
        try:
            userid=data['id']
        except Exception as e:
            return jsonify({'code': 245, 'data': '收藏失败,获取信息失败'})
        usercode=data['usercode']
        username=data['usernickname']
        goodis=data['goodid']
        if userid is None or userid=='None':
            return_user=jianuser(usercode=usercode,userin=username)
            if return_user is False:
                return jsonify({'code': 240, 'data': '收藏失败，校验失败'})
            else:
                userid=return_user['userid']
        user=User.query.filter_by(id=userid,status=False).first()
        if not user:
            return jsonify({'code': 241, 'data': '收藏失败，用户不存在'})
        goodis=good.query.filter_by(id=goodis,status=False).first()
        if not  goodis:
            return jsonify({'code': 242, 'data': '请确认收藏商品是否已经删除'})
        good_user=shoucang.query.filter_by(user=user.id,good=goodis.id).first()
        if good_user:
            return jsonify({'code': 243, 'data': '已经收藏'})
        new_shoucang=shoucang(user=user.id,good=goodis.id,cellnum=goodis.xianjian)
        db.session.add(new_shoucang)
        db.session.commit()
        return jsonify({'code': 200, 'data': '收藏成功'})
class getdefult(MethodView):
    def post(self):
        data = json.loads(request.data.decode('utf-8'))
        try:
            userid = data['id']
        except Exception as e:
            return jsonify({'code': 250, 'data': '获取地址失败,获取信失败'})
        usercode = data['usercode']
        username = data['usernickname']
        if userid is None:
            checkuser=jianuser(userin=username,usercode=usercode)
            if checkuser is False:
                return jsonify({'code': 251, 'data': '获取地址失败，校验失败'})
            else:
                userid=checkuser['userid']
        user_add=User.query.filter_by(id=userid,status=False).first()
        if user_add is None:
            return jsonify({'code': 252, 'data': '获取地址失败，用户不存在或者被删除'})
        user_add_is=adderss.query.filter_by(relation=user_add.id,status=False,is_moren=False).first()
        if not  user_add_is:
            return jsonify({'code': 253, 'data': '获取地址失败，默认地址不存在'})
        add={'address':user_add_is.address,'user':user_add_is.user,'phone':user_add_is.userphone}
        return jsonify({'code': 200, 'data':add})
class getgoodyouhui(MethodView):
    def post(self):
        data = json.loads(request.data.decode('utf-8'))
        try:
            userid = data['id']
        except Exception as e:
            return jsonify({'code': 264, 'data': '获取优惠券，获取信息失败'})
        usercode = data['usercode']
        username = data['usernickname']
        good_list=data['goods']
        goods=[]
        for goo in good_list:
            goods.append(goo['gooid'])
        if userid is None:
            checkuser = jianuser(userin=username, usercode=usercode)
            if checkuser is False:
                return jsonify({'code': 260, 'data': '获取优惠券，校验失败'})
            else:
                userid = checkuser['userid']
        user_add = User.query.filter_by(id=userid, status=False).first()
        if user_add is None:
            return jsonify({'code': 261, 'data': '获取优惠券，用户不存在或者被删除'})
        youhui_user=useryou.query.filter_by(user=user_add.id,is_use=False).all()
        if len(youhui_user)<1:
            return jsonify({'code': 262, 'data': '用户没有可以使用的优惠券'})
        good_tag=[]
        for goos in goods:
            goodone=good.query.filter_by(id=goos,status=False).first()
            if goodone is None:
                pass
            else:
                good_tag.append({'tagid':goodone.classtag,'goodid':goodone.id})
        youhuiquan=[]
        for item in youhui_user:
            item_youhui=youhui.query.filter_by(id=item.youh,status=False).first()
            if  (item.lingqu-item_youhui.endtime).days>item_youhui.lingqu:
                pass
            else:
                youhuiquan.append({'youhui':item_youhui,'good':item_youhui.good,'classtags':item_youhui.classtags,'num':item.num})
        ke_user_you=[]
        for it in good_tag:
            for j in youhuiquan:
                if good_tag[it]['tagid']==youhuiquan[j]['classtags'] or  good_tag[it]['goodid']==youhuiquan[j]['good']:
                    ke_user_you.append({'youhu':youhuiquan[j]['youhui'],'num':youhuiquan[j]['num'],'goodid':good_tag[i]['goodid']})
        if len(ke_user_you)<1:
            return jsonify({'code': 263, 'data': '本次的商品没有可以使用优惠券的'})
        can_user_youhui=[]
        for item in ke_user_you:
            can_user_youhui.append({'name':item['youhu'].name,'man_num':item['youhu'].man_num,'jian_num':item['youhu'].jian_num,'is_die':item['youhu'].is_die,'num':item['num'],'goodid':item['goodid']})
        return jsonify({'code': 200, 'data':can_user_youhui})
class createorder(MethodView):
    def post(self):
        data=json.loads(request.data.decode('utf-8'))
        try:
            userid=data['id']
        except:
            return  jsonify({'code':260,'data':'获取用户信息失败'})
        usercode=data['usercode']
        username=data['usernickname']
        desc=data['des']
        goods=data['goods']
        youhuilist=data['youhui']
        allprice=data['allPrice']
        curAddressData=data['curAddressData']
        if userid is None:
            checkoutuser=jianuser(userin=username,usercode=usercode)
            if checkoutuser is False:
                return  jsonify({'code':261,'data':'检查用户失败'})
            userid=checkoutuser['userid']
        user_is=User.query.filter_by(id=userid,status=False).first()
        if not  user_is:
            return jsonify({'code': 262, 'data': '找不到用户'})
        goodlist=[]
        for goo in goods['shopList']:
            goodone=good.query.filter_by(id=goo['gooid'],status=False).first()
            goodlist.append({'goodid':goodone.id,'tagid':goodone.classtag,
                             'xianjian':goodone.xianjian,
                             'num':goo['num'],'yanse':goo['yanse'],'guige':goo['guige']})
        youhuiuser=[]
        for you in youhuilist:
            name=you['name']
            num=you['num']
            youone=youhui.query.filter_by(name=name,status=False).first()
            youhuiuser.append({'tag':youone.classtags,'goodid':youone.good,
                               'man_num':youone.man_num,
                               'jian_num':youone.jian_num})
        for item in youhuiuser:
            for good_one in goodlist:
                if item['tag']==good_one['tagid'] or item['goodid']==good_one['goodid']:
                    sum=good_one['xianjian']*good_one['num']
                    if sum>=item['man_num']:
                        pric=sum-item['jian_num']
                    else:
                        pric==sum
                else:
                    pric=good_one['xianjian'] * good_one['num']
            allprice += pric
        local_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))[2:]
        ordenum_make=str(user_is.id)+local_time+str(random.randint(100000,9999999))
        addre=adderss.query.filter_by(address=curAddressData['address'],relation=user_is.id,
                                        status=False,
                                        user=curAddressData['user']).first()
        new_order=order(ordenum=ordenum_make,oreder_user=user_is.id,address=addre.id,
                        zhifujine=allprice,orderdesc=desc)
        db.session.add(new_order)
        db.session.commit()
        for goos_or in goodlist:
            crea=ordergood(order=new_order.id,good=goos_or['goodid'],num=goos_or['num'],
                           guige=goos_or['guige'],value=goos_or['yanse'])
            db.session.add(crea)
        db.session.commit()
        order_deatil={'id':new_order.id,'price':allprice}
        return  jsonify({'code':200,'data':order_deatil})
class getusercang(MethodView):
    """错误的返回code从270开始,获取用户收藏的商品"""
    def post(self):
        data=json.loads(request.data.decode('utf-8'))
        userid=data['userid']
        usercode=data['usercode']
        username=data['usernickname']
        if userid is None:
            checkoutuser=jianuser(userin=username,usercode=usercode)
            if checkoutuser is False:
              return jsonify({'code':270,'data':'校验用户失败'})
            else:
                userid=checkoutuser['userid']
        useris=User.query.filter_by(id=userid,status=False).first()
        if not useris:
            return jsonify({'code':271,'data':'系统没有找到你的用户'})
        shoucang_user=shoucang.query.filter_by(user=useris.id).all()
        goodscang=[]
        for item in shoucang_user:
            goodone=good.query.filter_by(id=item.good).first()
            chajian=int(item.cellnum)-int(goodone.xianjian)
            if chajian>0:
                chajia='+%s'%chajian
            elif chajian<0:
                chajia=chajian
            else:
                chajia=0
            goodscang.append({'goodid':goodone.id,'goodstatus':goodone.status,
                'name':goodone.goodname,'pic':goodone.pic_url,'goodjiage':goodone.xianjian,'shoucangjia':item.cellnum,'chajia':chajia})
        return jsonify({'code':200,'data':goodscang,'userid':useris.id})
class getalluserhui(MethodView):
    """返回code从280开始"""
    def post(self):
        data=json.loads(request.data.decode('utf-8'))
        userid=data['userid']
        usercode=data['usercode']
        username=data['usernickname']
        if userid is None:
            checkoutuser=jianuser(userin=username,usercode=usercode)
            if checkoutuser is False:
              return jsonify({'code':280,'data':'校验用户失败'})
            else:
                userid=checkoutuser['userid']
        useris=User.query.filter_by(id=userid,status=False).first()
        if not useris:
            return jsonify({'code':281,'data':'用户不存在或者已经被删除'})
        youhuiall=useryou.query.filter_by(user=useris.id).order_by('is_use').all()
        data_you=[]
        for item in youhuiall:
            youhuione=youhui.query.filter_by(id=item.youh).first()
            if ((item.lingqu-datetime.now()).days)<=youhuione.lingqu and (youhuione.endtime-datetime.now()).days>0:
                usercan=True
            else:
                usercan=False
            if youhuione.type==1:
                cate=True
            else:
                tas=classtag.query.filter_by(id=youhuione.classtags).first()
                cate=tas.name
            data_you.append({'man_num':youhuione.man_num,'jian_num':youhuione.jian_num,'id':item.id,
                'linqushijian':item.lingqu,'use':item.is_use,'zhuantai':youhuione.status,'canuse':usercan,
                'linqu':youhuione.lingqu,'cate':cate,'endtime':youhuione.endtime.strftime('%Y-%m-%d')})
        return jsonify({'code':200,'data':data_you,'userid':userid})