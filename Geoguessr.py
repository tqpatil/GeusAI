import numpy as np
import cv2
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from matplotlib import pyplot as plt
import pygetwindow
import time
import mss
from PIL import Image
counter = 0
image_count = 0
def play_one(driver):
    global counter
    global image_count
    x=WebDriverWait(driver,60)
    try:
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-qa='pano-zoom-in']"))).click()
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-qa='pano-zoom-out']"))).click()
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-qa='pano-zoom-in']"))).click()
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-qa='pano-zoom-out']"))).click()
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-qa='pano-zoom-in']"))).click()
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-qa='pano-zoom-out']"))).click()
    except Exception:
        print("mal")
    time.sleep(1.5)
    pic1=take_screenshot()
    path1 = "Model_Data"
    path1 = path1 + "\\" + "serbia_" + str(image_count) + ".jpg"
    cv2.imwrite(path1, cv2.cvtColor(pic1, cv2.COLOR_BGR2RGB))
    image_count += 1
    main = driver.find_element(By.TAG_NAME,'main')
    for _ in range(0, 4):
        action = ActionChains(driver)
        action.move_to_element(main) \
            .click_and_hold(main) \
            .move_by_offset(350, 0) \
            .release(main) \
            .perform()
    pic2=take_screenshot()
    path2 = "Model_Data"
    path2 = path2 + "\\" + "serbia_" + str(image_count) + ".jpg"
    cv2.imwrite(path2, cv2.cvtColor(pic2, cv2.COLOR_BGR2RGB))
    image_count += 1
    # plt.imshow(pic2)
    # plt.show()
    x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='button_button__CnARx button_variantPrimary__xc8Hp button_sizeLargeWide__r3OFc']"))).click()
    counter += 1
    if(counter % 5 == 0):
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='button_button__CnARx button_variantPrimary__xc8Hp button_sizeLargeWide__r3OFc']"))).click()
        counter = 0
        time.sleep(1)
    time.sleep(1)

    
def cropImage(Image, XY: tuple, WH: tuple, returnGrayscale=False):
    # Extract the x,y and w,h values
    (x, y) = XY
    (w, h) = WH
    # Crop Image with numpy splitting
    crop = Image[y:y + h, x:x + w]
    # Check if returnGrayscale Var is true if is then convert image to grayscale
    if returnGrayscale:
        crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    # Return cropped image
    return crop
    
def take_screenshot():
    cap=mss.mss()
    # x= np.array(cap.grab(pygetwindow.getActiveWindow().box))
    monitor_1 = cap.monitors[1]
    x= np.array(cap.grab(monitor_1))
    x2=cv2.cvtColor(x,cv2.COLOR_BGR2RGB)[:,:,:3]
    x2=cv2.resize(x2,(224,224))
    arr_image = np.array(x2)
    final_image = cropImage(arr_image, (25,36), (174,174))
    return final_image
def guess(driver):
    x=WebDriverWait(driver,60)

    try:
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[style='position: absolute; left: 0px; top: 256px; width: 256px; height: 256px; transition: opacity 200ms linear 0s;']"))).click()
    except Exception:
        print("mal")
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[style='position: absolute; left: 0px; top: 256px; width: 256px; height: 256px; transition: opacity 200ms linear 0s;']"))).click()

if __name__=="__main__":
    chrome_options=Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.geoguessr.com/signin")
    try:
        email=driver.find_element(By.NAME,"email")
        email.send_keys("geusdeus007@gmail.com")
    except Exception:
        driver.refresh()
        WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.NAME,"email"))).send_keys("geusdeus007@gmail.com")
    try:
        pw = driver.find_element(By.NAME,"password")
        pw.send_keys("PASSWORD GOES HERE")
    except Exception:
        driver.refresh()
        WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.NAME,"password"))).send_keys("deusetpatria")
    try:
        submit_button = driver.find_element(By.CSS_SELECTOR,"button[data-qa='login-cta-button']")
        submit_button.click()
    except Exception:
        WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-qa='login-cta-button']"))).click()
    x=WebDriverWait(driver,60)
    try:
        x.until(EC.element_to_be_clickable((By.CLASS_NAME,"game-menu-button_button__WPwVi"))).click()
    except:
        x.until(EC.element_to_be_clickable((By.CLASS_NAME,"game-menu-button_button__WPwVi"))).click()
    x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='nav-card_tag__jrwi0 screens_buttonHollow__6jfJJ']"))).click()
    try:
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[class='button_link__xHa3x button_variantSecondary__lSxsR button_sizeSmall__POheY']"))).click()
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='button_button__CnARx button_variantPrimary__xc8Hp button_sizeSmall__POheY']"))).click()
    except Exception:
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[class='button_link__xHa3x button_variantSecondary__lSxsR button_sizeSmall__POheY']"))).click()
        x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='button_button__CnARx button_variantPrimary__xc8Hp button_sizeSmall__POheY']"))).click()
    x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[data-qa='play-map-serbia']"))).click()
    x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[type='checkbox']"))).click()
    slider_handle = driver.find_element(By.CSS_SELECTOR,"div[class='styles_handle__zYRZ7']")
# Create an ActionChains object
    actions = ActionChains(driver)
    actions.move_to_element(slider_handle).click_and_hold().move_by_offset(-18,0).release().perform()
    x.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-qa='start-game-button']"))).click()
    for i in range(10):
        play_one(driver)

    # x=int(input("Done"))


    
    # WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,'a'))).click()

    #nav-card_tag__jrwi0 screens_buttonHollow__6jfJJ
    #button_button__CnARx button_variantPrimary__xc8Hp button_sizeSmall__POheY