// pages/cang/cang.js
var app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    goods:{},
    hsgood:false
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.setNavigationBarTitle({
      title: '收藏',
    });
    this.getusercang();
  },
  getusercang:function(){
    var that=this;
    wx.request({
      url: app.globalData.url+'/getusercang',
      data:{
        userid: app.globalData.userid,
        usercode: app.globalData.usercode,
        usernickname: app.globalData.usernickname
      },
      method: 'POST',
      header: {
        'content-type': 'application/json'
      },
      success:function(res){
        if(res.data.code==200){
          that.setData({
            goods:res.data.data,
            hsgood:true
          })
          app.globalData.userid = res.data.userid
        }else{
          wx.showModal({
            title: '获取收藏',
            content: res.data.data,
          })
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

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function (res) {
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    wx.showModal({
      title: '收藏',
      content: '没有更多收藏',
    })
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})