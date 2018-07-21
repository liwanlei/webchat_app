//index.js
//获取应用实例
const app = getApp()
Page({
  data: {
    motto: '',
    userInfo: {},
    banner:{},
    rexiao:{},
    tuijian:{},
    youhui:{},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onShareAppMessage: function (res) {
    if (res.from === 'button') {
      // 来自页面内转发按钮
     
    }
    return {
      title: '大型购物中心小程序',
      path: ''
    }
  },
  onLoad: function () {
    this.getbanner('banner');
    this.getrexiao('rexiao');
    this.gettuijian('tuijian');
    this.getyouhui('youhui');
    app.getUserInfo(function (userInfo) {
    });
  }
  ,
  lingqu:function(res){
    var id=res.target.dataset.id
    wx.request({
      url: app.globalData.url+'/linquyouhui',
      data: {
        id: id,
        username: app.globalData.usernickname,
        usercode: app.globalData.usercode,
      },
      method: 'POST',
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
      // console.log(res)
        app.globalData.userid=res.data.id
       if (res.data.code==200){
         wx.showToast({
           title: '优惠券领取成功',
           icon: 'success',
           duration: 3000
         })
       }
       else{
         wx.showToast({
           title: '你已经有了这个优惠券，请使用',
           icon: 'none',
           duration: 3000
         })
       }
      }
    })
  },
  getyouhui: function (youhui) {
    var that = this
    wx.request({
      url: app.globalData.url+'/getyouhui',
      success: function (res) {
        var data = res.data;
        var readyData = {};
        readyData[youhui] = data,
          that.setData(readyData);
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
  gettuijian: function (tuijian) {
    var that = this
    wx.request({
      url: app.globalData.url +'/gettuijiangood',
      success: function (res) {
        var data = res.data;
        var readyData = {};
        readyData[tuijian] = data,
          that.setData(readyData);
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
  getbanner: function (banner) {
    var that=this
    wx.request({
      url: app.globalData.url +'/getbanner',
      success: function (res) {
        var data = res.data;
        var readyData = {};
        readyData[banner] = data,
          that.setData(readyData);
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
  getrexiao: function (rexiao) {
    var that = this
    wx.request({
      url: app.globalData.url +'/getregood',
      success: function (res) {
        var data = res.data;
        var readyData = {};
        readyData[rexiao] = data,
          that.setData(readyData);
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
})
