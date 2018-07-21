var app = getApp()
var WxParse = require('../../lib/wxParse/wxParse.js');
Page({
  /**
   * 页面的初始数据
   */
  data: {
    userInfo: {},
    gallery:{},
    goods:{},
    comment:{},
    goodid:{},
    specificationList:[],
    propeyanse: "",
    propeguige: "",
    yanse:{},
    yansepic:{},
    guige:{},
    number1:1,
    minnumber:1,
    openAttr:'',
    attribute:{},
    cartGoodsCount:0
  },
  closeAttr: function () {
    this.setData({
      openAttr: false,
    });
  },
  seleceyanse:function(event){
    var yans=event.currentTarget.dataset.yanse;
    console.log()
    this.setData({
      propeyanse: yans,
      yansepic: this.data.yanse[event.currentTarget.dataset.index].icon,
    }) 
  },
  guigese:function(event){
    var yanse = event.currentTarget.dataset.guige;
    this.setData({
      propeguige:yanse
    }) 
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var id=options.id
    this.getgood(id, 'goods', 'comment', 'gallery','attribute')
    this.setData({
      goodid:id
    });
  },
  getgood: function (id, goods, comment, gallery, attribute){
    var that=this
    wx.request({
      url: app.globalData.url +'/getgooddetai',
      data:{
        id:id
      },
      method: 'POST',
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        var dat=res.data
        var readyData = {}
        readyData[goods] = dat.good,
          readyData[comment] = dat.comment,
          readyData[gallery] = dat.img,
          readyData[attribute] = dat.atterdss
          that.setData(readyData);
      },
    });
  },
  openCartPage:function(){
    wx.switchTab({
      url: '../../pages/cart/index',
    })
  },
  addToCart:function(){
    if (this.data.propeyanse == '' && this.data.propeguige == '') {
      wx.showModal({
        title: '提示',
        content: '请选择商品规格！',
        showCancel: false
      })
      return;
    };
    var buginfo = this.buynowinfo();
    var cartGoodsCountnew=0;
    var buinfos=[];
    var dar=[];
    dar = wx.getStorageSync('cartInfo');
    if (dar==''){
      buinfos.push(buginfo.shopList);
    }else{
      buinfos.push(dar[0]);
      buinfos.push(buginfo.shopList);
    } 
    wx.setStorage({
      key: 'cartInfo',
      data: buinfos,
    });
    cartGoodsCountnew += this.data.number1 +this.data.cartGoodsCount
    this.setData({
      cartGoodsCount:cartGoodsCountnew
    })
  },
  switchAttrPop:function(evnt){
    if (this.data.openAttr == false) {
      this.setData({
        openAttr: !this.data.openAttr
      });
    }
    var that = this
    var id = evnt.currentTarget.dataset.red
    wx.request({
      url: app.globalData.url +'/getguige',
      data: {
        id: id
      },
      method: 'POST',
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        var dat = res.data
          that.setData({
            yanse:dat.yanse,
            guige:dat.guige
          });
        },
    })
  },
  addCannelCollect:function(event){
    var that = this
    var goodeid = event.currentTarget.dataset.id;
    app.getUserInfo(function (userInfo) {
    });
    wx.request({
      url: app.globalData.url +'/addcang',
      method: 'POST',
      data: {
        id: app.globalData.userid,
        usercode: app.globalData.usercode,
        usernickname: app.globalData.usernickname,
        goodid:goodeid
      },
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        if(res.data.code==200){
          wx.showModal({
            title: '成功',
            content: res.data.data,
            showCancel: false
          });
        }
        else{
          wx.showModal({
            title: '提示',
            content: res.data.data,
            showCancel: false
          });
        }
      },
      fail: function () {
        // fail
      },
      complete: function () {
        // complete
        wx.hideToast();
      }
    })
  },
  addNumber:function(){
    if (this.data.number1 < this.data.goods.kucun){
      var currentNum = this.data.number1;
      currentNum++;
      this.setData({
        number1: currentNum
      }) 
    }
  },
  cutNumber:function(){
    if (this.data.number1 > this.data.minnumber){
      var currentNum = this.data.number1;
      currentNum--;
      this.setData({
        number1: currentNum
      }) 
    }
  },
  lijigoumai:function(){
    if (this.data.propeyanse == '' && this.data.propeguige==''){
      wx.showModal({
        title: '提示',
        content: '请选择商品规格！',
        showCancel: false
      })
      return;
    };
    var buginfo = this.buynowinfo();
    wx.setStorage({
      key: 'buyNowInfo',
      data: buginfo,
    })
    wx.navigateTo({
      url: "/pages/payorder/index?orderType=buyNow"
    }) 
  },
  buynowinfo:function(){
    var buyNowInfo = {};
    var buyinfo={};
    buyNowInfo.shopList=[];
    buyinfo['gooid']=this.data.goods.id;
    buyinfo['guige'] = this.data.propeguige;
    buyinfo['yanse'] = this.data.propeyanse;
      buyinfo['num'] = this.data.number1;
      buyinfo['name'] = this.data.goods.name;
      buyinfo['kuncun'] = this.data.goods.kucun;
      buyinfo['price'] = this.data.goods.xianjian;
      buyinfo['pic'] = this.data.goods.pic_url;
      buyNowInfo.shopList.push(buyinfo);
      return buyNowInfo;
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    WxParse.wxParse('goodsDetail', 'html', this.data.goods.desc, this);
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})