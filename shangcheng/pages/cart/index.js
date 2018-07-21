// pages/cart/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    hasgood:false,
    cartgood:[],
    num:1
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.setNavigationBarTitle({
      title: '购物车',
    });
    var datacart=[];
    datacart = wx.getStorageSync("cartInfo");
    this.setData({
      cartgood:datacart,
      hasgood:true
    });
  },
  checkboxChange:function(res){
    console.log(res)
  },
  addNumber:function(res){
    var num = res.currentTarget.dataset.id;
    var numb = this.data.cartgood[num][0].num;
    var kun = this.data.cartgood[num][0].kuncun;
    if (numb < kun) {
      numb +=1
    };
    this.data.cartgood[num][0].num = numb;
    this.setData({
      cartgood: this.data.cartgood
    })
  },
  cutNumber:function(res){
    var num = res.currentTarget.dataset.id;
    var numb=this.data.cartgood[num][0].num;
    if (numb>1){
      numb-=1
    };
    this.data.cartgood[num][0].num=numb;
    this.setData({
      cartgood:this.data.cartgood
    })
  },
  wodesgoucang:function(){
    wx.navigateTo({
      url: '../../pages/cang/cang',
    })
  },
  usergou:function(){
    wx.navigateTo({
      url: '../../pages/order/order',
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