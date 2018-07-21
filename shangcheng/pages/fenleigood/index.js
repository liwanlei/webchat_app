// pages/fenleigood/index.js
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    navList:{},
    good:{}
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
     var id=options.id
     this.getidgood(id)
     this.setData({
       id:id
     })
  },
  getidgood:function(id){
    var that=this
    wx.request({
      url: app.globalData.url+'/getfengood',
      data:{
        id:id
      },
      method: 'POST',
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        var getgood=res.data.good
        var getnav=res.data.data
        that.setData(
          {
            navList:getnav,
            good:getgood
          }
        )
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
  
  },
  switchCate: function (event) {
    if (this.data.id == event.currentTarget.dataset.id) {
      return false;
    } 
    this.getidgood( event.currentTarget.dataset.id)
    }
})