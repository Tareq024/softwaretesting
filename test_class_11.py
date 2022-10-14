from selenium import webdriver
class Firefox():
    def firefox(self):
        driver=webdriver.Firefox(executable_path="D:\\softwarem testing class\\Class 10\\tools\\geckodriver.exe")
        driver.get("https://www.iiuc.ac.bd")

test_object=Firefox()
test_object.firefox()