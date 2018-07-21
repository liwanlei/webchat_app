// pages/order/order.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    orders:[],
    orders_yuan:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that=this
    wx.setNavigationBarTitle({
      title: '订单界面',
    })
    app.getUserInfo(function (userInfo) {
    })
    that.userorder('orders','orders_yuan')
  },
  userorder: function (orders, orders_yuan){
    var that=this
    wx.request({
      url: app.globalData.url+'/huoquding',
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
        var resdasy={}
        resdasy[orders]=res.data.data
        resdasy[orders_yuan] =res.data.data
        that.setData(resdasy)
      }
    })
  },
  switchCate:function(res){
   var that =this;
   var oeders = that.data.orders_yuan;
   
    if(res.currentTarget.dataset.name=='待付款'){
      var huoqu = [];
      for(var j=0;j<oeders.length;j++){
        if (oeders[j].shi_zhifu==false){
          huoqu.push(oeders[j])
        }; 
      }; 
      that.data.orders = [];
      that.setData({
        orders: huoqu
      })
   }else if(res.currentTarget.dataset.name == '待发货'){
      var huoqu = [];
      for (var j = 0; j < oeders.length; j++) {
        if (oeders[j].is_fa == false && oeders[j].shi_zhifu==true) {
          huoqu.push(oeders[j])
        };
     };
     that.data.orders = [];
     that.setData({
       orders: huoqu
     })
    }else if (res.currentTarget.dataset.name == '待收货') {
      var huoq = [];
      for (var j = 0; j < oeders.length; j++) {
       if (oeders[j].is_shou == false && oeders[j].shi_zhifu == true && oeders[j].is_fa==true) {
         huoq.push(oeders[j])
       };
      }; that.data.orders = []; 
      that.setData({
        orders: huoq
      })
   }else if (res.currentTarget.dataset.name == '待评价') {
      var huo = [];
     for (var j = 0; j < oeders.length; j++) {
       if (oeders[j].is_ping == false && oeders[j].shi_zhifu == true && oeders[j].is_fa == true && oeders[j].is_shou == true) {
         huo.push(oeders[j]);
       };
     } 
     that.data.orders = [];
     that.setData({
       orders:huo
     })
     }else{
      that.setData({
        orders: oeders
      })
     }
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
    app.getUserInfo(function (userInfo) {
    });
    this.userorder('orders', 'orders_yuan');
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