
driver = webdriver.Chrome(options=chrome_options)
curl = driver.current_url

ef = 1


def judge_class_name(name):
    try:
        target = driver.find_element(By.CLASS_NAME, name)
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+name)
        sys.exit()

def judge_class_names(name):
    try:
        target = driver.find_elements(By.CLASS_NAME, name)
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+name)
        sys.exit()


def judge_class_name_num(name, num):
    try:
        target = driver.find_elements(By.CLASS_NAME, name)[num]
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+name)
        sys.exit()

def judge_link_text(name):
    try:
        target = driver.find_element(By.LINK_TEXT, name)
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+name)
        sys.exit()

def judge_id(name):
    try:
        target = driver.find_element(By.ID, name)
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+name)
        sys.exit()


def judge_name(name):
    try:
        target = driver.find_element(By.NAME, name)
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+name)
        sys.exit()


def judge_xpath_btn(text):
    try:
        target = driver.find_element(By.XPATH, "//button[text()='"+ text + "']")
        return target
    except NoSuchElementException as ex:
        print("页面没有加载成功，请刷新后重试！"+text)
        sys.exit()


def auto_sell(eth):
    title = judge_class_name("item--title")
    title_text = title.text
    print(title_text + " Sell开始。。。")
    sell_btn = judge_link_text("Sell")
    sell_btn.click()
    time.sleep(6)

    duration_btn = judge_id("duration")
    duration_btn.click()
    time.sleep(1)

    # 1month
    iaeyiq_btn = judge_class_name("iAeYiQ")
    iaeyiq_btn.click()
    time.sleep(1)

    glym_pt = judge_class_name_num("glymPt", 2)
    glym_pt.click()
    time.sleep(1)

    price_btn = judge_name("price")
    price_btn.click()

    price = judge_name("price")
    price.send_keys(eth)
    time.sleep(1)

    fzw_dgL_btn = judge_xpath_btn("Complete listing")
    fzw_dgL_btn.click()
    time.sleep(6)

    if ef == 1:
        sign_btn = judge_xpath_btn("Sign")
        sign_btn.click()
    time.sleep(4)
    handles = driver.window_handles
    curhandle = driver.current_window_handle
    for h in handles:
        if h != curhandle:
            driver.switch_to.window(h)
            break

    time.sleep(4)

    if ef == 1:
        sign = judge_class_name("request-signature__footer__sign-button")
        sign.click()
    else:
        primary_btn = judge_class_name("btn-primary")
        primary_btn.click()

    driver.switch_to.window(curhandle)
    time.sleep(6)
    print(title_text + " sell 成功~~~")

    driver.get(curl)
    time.sleep(6)


itemlist = judge_class_names("dNtdmG")
if any(itemlist):
    idx = 0
    for item in itemlist:
        ele = judge_class_name_num("dNtdmG", idx)
        ele.click()

        time.sleep(6)
        auto_sell("0.08")
        idx = idx + 1
    print("全部已成功Sell")
else:
    print("没有找到需要sell的商品")
    sys.exit()


