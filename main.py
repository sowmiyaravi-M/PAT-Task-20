from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DragAndDrop:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://jqueryui.com/droppable/"
        self.droppable_frame_locator = (By.CLASS_NAME, "demo-frame")
        self.draggable_locator = (By.ID, "draggable")
        self.droppable_locator = (By.ID, "droppable")

    def open_page(self):
        self.driver.get(self.base_url)

    def switch_to_droppable_frame(self):
        frame = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.droppable_frame_locator))
        self.driver.switch_to.frame(frame)

    def find_draggable_and_droppable(self):
        self.draggable_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.draggable_locator))
        self.droppable_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.droppable_locator))

    def perform_drag_and_drop(self):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(self.draggable_element, self.droppable_element).perform()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def close_browser(self):
        self.driver.quit()


draganddrop = DragAndDrop()
draganddrop.open_page()
draganddrop.switch_to_droppable_frame()
draganddrop.find_draggable_and_droppable()
draganddrop.perform_drag_and_drop()
draganddrop.switch_to_default_content()
draganddrop.close_browser()

