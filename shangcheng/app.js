//app.js
App({
  onLaunch: function () {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

  },
  getUserInfo: function (cb) {
    var that = this
    if (this.globalData.userInfo) {
      typeof cb == "function" && cb(this.globalData.userInfo)
    } else {
      //调用登录接口
      wx.login({
        success: function (res) {
          that.globalData.usercode=res.code
          wx.getUserInfo({
            success: function (res) {
              that.globalData.userInfo = res.userInfo
              that.globalData.usernickname = res.userInfo.nickName
              that.globalData.useravat = res.userInfo.nickName
              typeof cb == "function" && cb(that.globalData.userInfo)
            }
          })
        }
      })
    }
  },
  globalData: {
    userInfo: null,
    usercode:null,
    usernickname:null,
    useravat:null,
    userid:null,
    url:'http://127.0.0.1:5000'
  }
})