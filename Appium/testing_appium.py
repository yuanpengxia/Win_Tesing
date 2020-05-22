
from appium import webdriver

desire_cap = {
  "platformName": "Android",
  "deviceName": "7XBNW19910007839",
  "appPackage": "com.bkt.exchange",
  "appActivity": ".activity.StartPageActivity",
  #绕过弹窗
  "noReset":True,
  #不需要重启，直接按照上次停留的页面继续操作（提升运行速度）
  "dontStopAppOnReset":True,
  #跳过安装，权限等设置等操作（提升运行速度）
  "skipDeviceInitialization":True
}
driver = webdriver.Remote("http://192.168.0.130:4723/wd/hub",desire_cap)
driver.implicitly_wait(2)
#本地的地址，/wd/hub为固定写法
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[2]/android.widget.TextView").click()
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.ImageView").click()
driver.find_element_by_id("com.bkt.exchange:id/coin_edit").send_keys("BKK")
# driver.find_element_by_xpath("//*[@]").click()
#返回到上一页面
driver.back()
driver.back()
# driver.quit()
