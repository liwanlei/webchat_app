// pages/payorder/index.js
const app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    curAddressData:'',
    address:false,
    goodslist: [],
    orderType:'',
    openAttr:false,
    hasNoCoupons:false,
    youhui:[],
    allGoodsAndYunPrice:0,
    yunfei:0,
    allGoodsPrice:0
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.setNavigationBarTitle({
      title: '订单支付',
    })
    app.getUserInfo(function (userInfo) {
    });
    this.setData({
      orderType: options.orderType
    });
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  },
  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    var that=this;
    var sholist=[];
    if (that.data.orderType =='buyNow'){
      sholist = wx.getStorageSync('buyNowInfo')
      }else{
        sholist=[];
      }
    that.setData({
      goodslist:sholist,
    });
    that.getaddress();
    that.jisuan();
  },
  jisuan:function(){
    var good = this.data.goodslist.shopList;
    var sum=0;
    var yunprice=0;
    var shopnprice=0;
    var that=this;
    wx.request({
      url: app.globalData.url+'/getgoodyouhui',
      method: 'POST',
      data: {
        id: app.globalData.userid,
        usercode: app.globalData.usercode,
        usernickname: app.globalData.usernickname,
        goods:good
      }, header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        if (res.data.code==200){
          that.setData({
            hasNoCoupons:true,
            youhui:res.data.data
          })
        }else{
          that.setData({
            hasNoCoupons: false,
            youhui:[]
          })
        }
      }
    })
    if (that.data.hasNoCoupons==false){
      for (var i = 0; i < good.length; i++) {
        sum += good[i].price * good[i].num
      };
      shopnprice = sum;
      if (sum > 88) {
        yunprice = 0
      } else {
        yunprice = 10
        sum += 10
      }
      that.setData({
        allGoodsAndYunPrice: sum,
        yunfei: yunprice,
        allGoodsPrice: shopnprice
      })
    }else{

    }
  },
  selectAddress:function(){
    this.setData({
      openAttr:true
    })
  },
  getaddress:function(){
    var that = this;
    wx.request({
      url: app.globalData.url+'/one_add_user',
      data: {
        id: app.globalData.userid,
        usercode: app.globalData.usercode,
        usernickname:app.globalData.usernickname
      },
      method: 'POST',
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        if (res.data.code==200){
          that.setData({
            curAddressData: res.data.data,
            address: true
          })
        }else{
          that.setData({
            address: false})
        }
      }
    })
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
  addAddress:function(){
    wx.navigateTo({
      url: '../../pages/add/add',
    })
  },
  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  },
  createOrder:function(e){
    var that=this;
    var desc=e.detail.value.remark;
    wx.request({
      url: app.globalData.url+'/createorder',
      method: "POST",
      data: {
        id: app.globalData.userid,
        usercode: app.globalData.usercode,
        usernickname: app.globalData.usernickname,
        des:desc,
        goods: that.data.goodslist,
        youhui: that.data.youhui,
        allPrice: that.data.allGoodsAndYunPrice,
        curAddressData: that.data.curAddressData
      }, header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        if(res.data.code==200){
          wx.requestPayment({
            timeStamp: '',
            nonceStr: '',
            package: '',
            signType: '',
            paySign: '',
            success:function(res){
              wx.navigateTo({
                url: '../order/order',
              })
            },
            fail:function(res){
                wx.navigateTo({
                  url: '../order/order',
                })
            }
          })
        }else{
          wx.showModal({
            title:'订单创建失败',
            content: res.data.data,
          })
        }
      }
    })
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