# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, random, os

global driver


def login():
    #     driver=webdriver.Chrome()#打开火狐浏览器
    driver = webdriver.Firefox()  # 打开火狐浏览器
    driver.get('https://pf.winbons.com/login')
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.find_element_by_id('j_username').send_keys('131-4886-0728')
    driver.find_element_by_id('j_password').send_keys('888888')
    driver.find_element_by_class_name('bigFont').click()
    driver.implicitly_wait(20)
    time.sleep(2)
    return driver


def pulish_dynamic():
    driver = login()
    time.sleep(3)
    driver.implicitly_wait(20)
    st = str(time.time())
    driver.find_element_by_class_name('dynamic-inputarea-mess').clear()
    driver.find_element_by_class_name('dynamic-inputarea-mess').send_keys(st)
    driver.implicitly_wait(20)
    driver.find_element_by_class_name('dynamic-mess-out').click()
    time.sleep(5)
    return driver


def newBusinessOpportunity(driver):
    try:
        driver.find_element_by_class_name('icon-oppo').click()
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element_by_id('contacts_create').click()
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element_by_css_selector('input[type="text"][name="name"]').clear()
        businessName = u'BusinessOpportunity' + str(random.randint(0, 1000))
        driver.find_element_by_css_selector('input[type="text"][name="name"]').send_keys(businessName)
        btns = driver.find_elements_by_class_name('autocom-icon')
        for btn in btns:
            btn.click()
            driver.implicitly_wait(10)
            time.sleep(3)
            break
        chks = driver.find_elements_by_class_name('r0')
        for i in chks:
            try:
                i.click()
                break
            except:
                pass
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.find_element_by_id('search-confirm').click()
        driver.implicitly_wait(10)
        time.sleep(2)
        lists = driver.find_elements_by_class_name('pulldown-text')
        for i in lists:
            if i.text == u'销售阶段':
                i.click()
                driver.implicitly_wait(10)
                time.sleep(2)
                break
        lists = driver.find_elements_by_class_name('row-content')
        for i in lists:
            if i.text == u'初步接洽':
                i.click()
                driver.implicitly_wait(10)
                time.sleep(2)
                break
        # 执行js代码
        js = """$("input[name='finishDate']").val('2017-11-07')"""
        driver.execute_script(js)
        driver.implicitly_wait(10)
        time.sleep(2)
        btns = driver.find_elements_by_class_name('crm-button-yellow')
        for i in btns:
            if i.text == u'保存':
                i.click()
                driver.implicitly_wait(20)
                if driver.find_element_by_class_name('crm_prompt_text'):
                    return True
                time.sleep(3)
                break
        labs = driver.find_elements_by_class_name('opportunity-name')
        for i in labs:
            if i.text == businessName:
                return True
        return False
    except:
        return False


# 有新建客户功能的
def newBusinessOpportunity2(driver):
    try:
        # 点击商机
        driver.find_element_by_class_name('icon-oppo').click()
        driver.implicitly_wait(20)
        time.sleep(3)
        # 点击新建按钮
        driver.find_element_by_id('contacts_create').click()
        driver.implicitly_wait(20)
        time.sleep(3)
        driver.find_element_by_css_selector('input[type="text"][name="name"]').clear()
        businessName = u'BusinessOpportunity' + str(random.randint(0, 1000))
        driver.find_element_by_css_selector('input[type="text"][name="name"]').send_keys(businessName)
        btns = driver.find_elements_by_class_name('autocom-icon')
        for btn in btns:
            btn.click()
            driver.implicitly_wait(20)
            time.sleep(3)
            break
        # 新建客户
        driver.find_element_by_class_name('addNew').click()
        driver.implicitly_wait(20)
        time.sleep(2)
        driver.find_element_by_css_selector('[name="name"][placeholder="客户名称"]').send_keys(
            'test' + str(random.randint(1, 1000)))
        driver.implicitly_wait(20)
        time.sleep(2)
        driver.find_element_by_class_name('opera-search').click()
        driver.implicitly_wait(20)
        time.sleep(2)
        # 在搜索栏输入深圳
        driver.find_element_by_id('mapSearchInput').send_keys(u'深圳')
        driver.implicitly_wait(20)
        time.sleep(2)
        adds = driver.find_elements_by_class_name('auto-item')
        for i in adds:
            if u'深圳' in i.text:
                i.click()
                break
        driver.implicitly_wait(20)
        time.sleep(2)
        driver.find_element_by_class_name('opera-select').click()
        driver.implicitly_wait(20)
        time.sleep(2)
        driver.find_element_by_name('cust_pool').click()
        driver.implicitly_wait(20)
        time.sleep(2)
        driver.find_element_by_id('101793614151').click()
        driver.implicitly_wait(20)
        time.sleep(2)
        btns = driver.find_elements_by_class_name('newclient-button')
        for i in btns:
            if i.text == u'保存':
                i.click()
                break
        driver.implicitly_wait(20)
        time.sleep(2)

        #         driver.find_element_by_id('search-confirm').click()
        #         driver.implicitly_wait(10)
        #         time.sleep(2)
        lists = driver.find_elements_by_class_name('pulldown-text')
        for i in lists:
            if i.text == u'销售阶段':
                i.click()
                driver.implicitly_wait(20)
                time.sleep(2)
                break
        lists = driver.find_elements_by_class_name('row-content')
        for i in lists:
            if i.text == u'初步接洽':
                i.click()
                driver.implicitly_wait(20)
                time.sleep(2)
                break
        # 执行js代码
        js = """$("input[name='finishDate']").val('2017-7-30')"""
        driver.execute_script(js)
        driver.implicitly_wait(20)
        time.sleep(2)
        btns = driver.find_elements_by_class_name('crm-button-yellow')
        for i in btns:
            if i.text == u'保存':
                i.click()
                driver.implicitly_wait(20)
                if driver.find_element_by_class_name('crm_prompt_text'):
                    return True
                time.sleep(3)
                break
        labs = driver.find_elements_by_class_name('opportunity-name')
        for i in labs:
            if i.text == businessName:
                return True
        return False
    except:
        return False


driver = pulish_dynamic()
newBusinessOpportunity2(driver)
# newBusiness(driver)