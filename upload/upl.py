import os
import time

# m = sys.argv[1]
# d = sys.argv[2]
# ef = sys.argv[3]
from sele_util import init_driver, judge_id, judge_class_name, judge_class_name_human_valid, \
    judge_xpath_span

_media = "D:\centralization\\temp\img"
_description = "description"
_eth_flag = 1

driver = init_driver()
curl = driver.current_url


def read_nft():
    path = str(_media)
    int_ef = int(_eth_flag)

    filelist = os.listdir(path)
    x = 0
    for i in filelist:
        name = filelist[x]
        full_name = path + os.sep + name
        x += 1
        nl = len(name) - 4
        name = name[0:int(nl)]
        opensea_create_item(full_name, name, _description, int_ef)


def opensea_create_item(p_media, p_name, p_description, p_ethflg):
    # add the media url
    add_media(p_media)

    # add the name
    add_name(p_name)

    # add the description
    add_description(p_description)

    # select the chain
    # '1':default(ETH)
    # '0': Polygon
    if str(p_ethflg) == '1':
        judge_id(driver, "chain").click()
    else:
        judge_id(driver, "chain").click()
        judge_xpath_span(driver, "Polygon").click()
    time.sleep(3)

    judge_class_name(driver, "fzwDgL").click()
    time.sleep(5)

    print(p_name + " create success")

    # goto create item url
    driver.get(curl)


def add_media(p_media):
    judge_id(driver, "media").send_keys(p_media)


def add_name(p_name):
    judge_id(driver, "name").send_keys(p_name)


def add_description(p_description):
    judge_id(driver, "description").send_keys(p_description)

read_nft()
