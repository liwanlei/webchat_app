// pages/fenlei/index.js
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    fenlei:[],
    lei:{},
    bann:{}
  },
  
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getftag('fenlei')
  },
  getftag: function (fenlei) {
    var that = this
    wx.showLoading({
      title: '加载中...',
    });
    wx.request({
      url: app.globalData.url+'/getftag',
      success: function (res) {
        var data = res.data.data;
        var readyData = {};
        readyData[fenlei] = data,
          that.setData(readyData);
        wx.hideLoading();
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
  fenleis:function(res){
    var that=this;
    var fenlei = res.target.dataset.name
    wx.request({
      url: app.globalData.url+'/getftag',
      method:'POST',
      data:{fenlei:fenlei},
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        var banner =res.data
        var data=(res.data.data)
          that.setData({
            lei:data,
            bann:banner
          });
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