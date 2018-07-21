// pages/add/add.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    hasadd:false,
    add:[],
    openAttr:false,
    priver: ['北京','天津','河北省','山西省','内蒙古自治区','辽宁省','吉林省','黑龙江省','上海','江苏省','浙江省','安徽省','福建省','江西省','山东省','河南省','湖北省','湖南省','广东省','广西壮族自治区','海南省','重庆','四川省','贵州省','云南省','西藏自治区','陕西省','甘肃省','青海省','宁夏回族自治区','新疆维吾尔自治区','台湾','香港特别行政区','澳门特别行政区'],
    shi:{},
    userid:''
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.setNavigationBarTitle({
      title: '收货地址',
    }),
    app.getUserInfo(function (userInfo) {
    }),
      that.useradd('add','hasadd')
  },
  tianjia:function(){
    this.setData({
      openAttr:true
    })
  },
  closeAttr:function(){
    this.setData({
      openAttr: false
    })
  },
  bindChange:function(res){
    var proes = this.data.priver[res.detail.value[0]]
  },
  formSubmit: function (e) {
    var that = this;
    var name=e.detail.value.name
    var phone = e.detail.value.phone
    var dizhi = e.detail.value.dizhi
    wx.request({
      url: app.globalData.url+'/add_address',
      method:"POST",
      data:{
        name:name,
        phone: phone,
        dizhi:dizhi,
        id: app.globalData.userid,
        usernickname: app.globalData.usernickname,
        usercode: app.globalData.usercode
      },
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
      if (res.data.code==200){
        that.setData({
          openAttr: false
        })
        wx.startPullDownRefresh()
      }
      else{
        wx.showToast({
          title: res.data.data,
          icon: 'none',
          duration: 2000
        })
      }
      }
    })
  },
  useradd: function (add, hasadd){
    var that = this
    wx.request({
      url: app.globalData.url+'/getaddress',
      method: 'POST',
      data: {
        id: app.globalData.userid,
        usercode: app.globalData.usercode,
        usernickname: app.globalData.usernickname
      },
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        if (res.data.dcode=!200){
          that.hasadd=false
          app.globalData.userid =res.data.id
        }
        else {
          var readyData = {};
          readyData[add] = res.data,
          readyData[hasadd]=true,
          that.setData(readyData);
          app.globalData.userid = res.data.id
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
  edit:function(res){
    var that = this
    var id = res.currentTarget.dataset.id
    var userid=res.currentTarget.dataset.userid
  },
  shezhi: function (res) {
    var that = this
    var id = res.currentTarget.dataset.id
    var userid = res.currentTarget.dataset.userid
    wx.request({
      url: app.globalData.url+'/shzm',
      method: 'POST',
      data: {
        id: id,
        userid: userid
      },
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        if (res.data.dcode =!200) {
          wx.showToast({
            title: res.data.data,
            icon: 'none',
            duration: 3000
          })
          that.userid=userid
        }
        else {
          if (res.data.you==true){
            wx.showToast({
              title: '重新设置默认成功',
              icon: 'none',
              duration: 3000
            }),
              that.userid = userid
          }
          else{
            wx.showToast({
              title: '设置默认成功',
              icon: 'none',
              duration:3000
            }),
              that.userid = userid
              wx.startPullDownRefresh({
              })
          }
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
  dele:function(res){
    var that = this
    var id = res.currentTarget.dataset.id
    var userid = res.currentTarget.dataset.userid
    var id = res.currentTarget.dataset.id
    var userid = res.currentTarget.dataset.userid
    wx.request({
      url: app.globalData.url+'/deleadd',
      method: 'POST',
      data: {
        id: id,
        userid: userid
      },
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        if (res.data.dcode = !200) {
          wx.showToast({
            title: res.data.data,
            icon: 'none',
            duration: 3000
          })
          that.userid = userid
        }
        else {
          
            wx.showToast({
              title: '删除地址成功',
              icon: 'none',
              duration: 3000
            }),
              that.userid = userid
            wx.startPullDownRefresh({
            })
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
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },
  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    app.getUserInfo(function (userInfo) {
    })
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    app.getUserInfo(function (userInfo) {
    })
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
    app.getUserInfo(function (userInfo) {
    });
    var readyData = {};
    readyData['add'] = [];
      this.setData(readyData);
      this.useradd('add', 'hasadd')
      wx.stopPullDownRefresh();
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