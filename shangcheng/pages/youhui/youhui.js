// pages/youhui/youhui.js
var app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    youhui:{},
    hsyouhui:false
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.setNavigationBarTitle({
      title: '我的优惠券',
    });
    this.getyouhui();
  },
getyouhui:function(){
  var that=this;
  wx.request({
    url: app.globalData.url + '/getalluserhui',
    data: {
      userid: app.globalData.userid,
      usercode: app.globalData.usercode,
      usernickname: app.globalData.usernickname
    },
    method: 'POST',
    header: {
      'content-type': 'application/json'
    },
    success:function(res){
      if (res.data.code==200){
        that.setData({
          youhui:res.data.data,
          hsyouhui:true
        });
        app.globalData.userid = res.data.userid
      }else{
        that.setData({
          hsyouhui:flase
        });
        wx.showModal({
          title: '获取优惠券失败',
          content: res.data.data,
        });
      }
    }
  })
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
  quwang:function(res){
    if (res.currentTarget.dataset.lei==true){
      wx.switchTab({
        url: '../../pages/fenlei/index',
      })
    }else{
      wx.switchTab({
        url: '../../pages/fenlei/index',
        fail:function(res){
          console.log(res)
        }
      })
    }
  },
  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    this.setData({
      youhui: {}
    })
    wx.setNavigationBarTitle({
      title: '我的优惠券',
    });
    this.getyouhui();
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
   wx.showModal({
     title: '优惠券',
     content: '没有更多优惠券',
   })
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})