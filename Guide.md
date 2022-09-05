# Selenium-Python-Hybrid-Framework-Design

###  ⚫ The things this guide contains
            ---> Pytest unit testing framework
            ---> Logging and HTML report
            ---> Page Object Design Pattern
            ---> Data driven framework with excel
            ---> Git
            ---> Integration of framework to Jenkins
            
###  ⚫ Theory

#### ⚫ What is PIP installer Tool?
pip is a package management system used to install and manage software packages written in Python
pip is a recursive acronym that can stand for either "Pip Installs Packages" or "Pip Installs Python.


#### ⚫ Types of Wait in Selenium?
            --- Explicit Waits
                        --- An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code.  
                        
                        --- The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait.
                        
                        --- Example:
                                    from selenium import webdriver
                                    from selenium.webdriver.common.by import By
                                    from selenium.webdriver.support.ui import WebDriverWait
                                    from selenium.webdriver.support import expected_conditions as EC

                                    driver = webdriver.Firefox()
                                    driver.get("http://somedomain/url_that_delays_loading")
                                    try:
                                                element = WebDriverWait(driver, 10).until(
                                                EC.presence_of_element_located((By.ID, "myDynamicElement")))
                                    finally:
                                                driver.quit()
                                                
                        --- Expected Conditions:
                                    --- title_is
                                    --- title_contains
                                    --- presence_of_element_located
                                    --- visibility_of_element_located
                                    --- visibility_of
                                    --- presence_of_all_elements_located
                                    --- text_to_be_present_in_element
                                    --- text_to_be_present_in_element_value
                                    --- frame_to_be_available_and_switch_to_it
                                    --- invisibility_of_element_located
                                    --- element_to_be_clickable
                                    --- staleness_of
                                    --- element_to_be_selected
                                    --- element_located_to_be_selected
                                    --- element_selection_state_to_be
                                    --- element_located_selection_state_to_be
                                    --- alert_is_present
                                    
                        --- Custom Wait Command: You can also create custom wait conditions when none of the previous convenience methods fit your requirements.
                        
                        --- Example:
                                    # Wait until an element with id='myNewInput' has class 'myCSSClass'
                                    wait = WebDriverWait(driver, 10)
                                    element = wait.until(element_has_css_class((By.ID, 'myNewInput'), "myCSSClass"))
                                    
            --- Implicit Waits
                        --- It tells WebDriver to poll the DOM for a certain amount of time when trying to find any element not immediately available.
                        
                        --- The default setting is 0 (zero). 
                        
                        --- Once set, the implicit wait is set for the life of the WebDriver object.
                        
                        --- Example:
                                    from selenium import webdriver

                                    driver = webdriver.Firefox()
                                    driver.implicitly_wait(10) # seconds
                                    driver.get("http://somedomain/url_that_delays_loading")
                                    myDynamicElement = driver.find_element_by_id("myDynamicElement")


###  ⚫ Framework Design Step by Step


#### ⚫ What is XPath?
            --- XPath stands for XML Path Language	
            --- XPath uses "path like" syntax to identify and navigate nodes in an XML document


#### ⚫ Types of XPath?
            --- Absolute XPath:
                        --- It is the direct way to find the element, but the disadvantage of the absolute XPath is that if there are any changes made in the path of the element then that XPath gets failed.
                        
                        --- The key characteristic of XPath is that it begins with the single forward slash(/) ,which means you can select the element from the root node.
                        
                        --- Example: /html/body/div[2]/div[1]/div/h4[1]/b/html[1]/body[1]/div[2]/div[1]/div[1]/h4[1]/b[1]
                        
            --- Relative XPath: 
                        --- Relative Xpath starts from the middle of HTML DOM structure.
                        
                        --- It starts with double forward slash (//). 
                        
                        --- It can search elements anywhere on the webpage, means no need to write a long xpath and you can start from the middle of HTML DOM structure.    
                        
                        --- Relative Xpath is always preferred as it is not a complete path from the root element.
                        
                        --- Example: //div[@class='featured-box cloumnsize1']//h4[1]//b[1]
                        
                        
#### ⚫ How to locate elements?
            --- driver.find_element(By.ID, "id")
            
            --- driver.find_element(By.NAME, "name")
            
            --- driver.find_element(By.XPATH, "xpath")
            
            --- driver.find_element(By.LINK_TEXT, "link text")
            
            --- driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
            
            --- driver.find_element(By.TAG_NAME, "tag name")
            
            --- driver.find_element(By.CLASS_NAME, "class name")
            
            --- driver.find_element(By.CSS_SELECTOR, "css selector")
            
            
#### ⚫ What is page object model in Selenium?
            --- A design pattern in Selenium that creates an object repository for storing all web elements.
            --- Benefits: 
                        --- Easy to read test cases
                        --- Creating reusable code that can share across multiple test cases
                        --- Reducing the amount of duplicated code
                        --- If the user interface changes, the fix needs changes in only one place


#### ⚫ What is page factory model in Selenium?
            --- An inbuilt Page Object Model framework concept for Selenium WebDriver
            --- Benefits: 
                        --- It is very optimized.
                        --- It is used for initialization of Page objects or to instantiate the Page object itself.
                        --- Also used to initialize Page class elements without using “FindElement/s.”
                        --- @FindBy can accept tagName, partialLinkText, name, linkText, id, css, className, xpath as attributes.


#### ⚫ What is PyTest?
            --- PyTest is a testing framework that allows users to write test codes using Python programming language. 
            --- It helps you to write simple and scalable test cases for databases, APIs, or UI. 
            --- PyTest is mainly used for writing tests for APIs. It helps to write tests from simple unit tests to complex functional tests.


#### ⚫ What is PyTest?
            --- Very easy to start with because of its simple and easy syntax.
            --- Can run tests in parallel.
            --- Can run a specific test or a subset of tests
            --- Automatically detect tests
            --- Skip tests
            --- Open source
            
            
### Step 1: Install Python

            --- Windows : http://python.org/download/.

            --- Note : IF you are using Linux, MacOS X, Unix operating Systems then python will be installed by default with OS


### Step 2: Install Selenium
            Use Below command on PIP to install Selenium Package
                --- pip install selenium

// This command will set up the Selenium WebDriver client library on your machine with all modules and classes that we will need to create automated scripts using Python


### Step 3: Upgrade Selenum (If you need)
            The optional –U flag will upgrade the existing version of the installed package
                --- pip install -U selenium


### Step 4: How to know whether selenium was installed?
                --- pip show selenium


### Step 5: Install Pycharm IDE
                --- https://www.jetbrains.com/pycharm/download
                
                
### Step 7: Create a new project in PyCharm 
                --- Keep to deafault folder to avoid issues             


### Step 8: Interpreter Settings -> Select Below path instead of project path  //It will install required package generally
                --- C:\Users\ialmu\AppData\Local\Programs\Python\Python39\python.exe


### Step 9: Install pytest using below commad
                --- pip install pytest          //install
                --- pytest --version            // to check version
                
                
### Step 10: Create a new package under existing project
                --- Project -> New -> Python Package -> Name it pytests (Recommended)
                
                
### Step 11: Create test classes under Pytests Package
                --- Conventions you need to follow
                        --- Test class names have to start with "test_" or end with "_test" if you want to treat them as pytests because pytest look for them and run them automatically using this.
                        --- Example: 
                                    test_login


### Step 12: Create test methods inside test classes
                --- Conventions you need to follow
                        --- Test method names have to start with "test_" 
                        --- Example: 
                                   def test_login():
                                   
### Step 13: How to configure and run pytests?
                --- Click on "Edit Configurations" from right -> '+' -> Python test -> pytest and then select script from directy -> apply -> click on Run 
                      

### Step 14: How to run the tests from terminal?
                --- Open terminal, copy the path of the test package, paste it to the terminal, go to that directory, use command "py.test" //it will run all test
                --- Example: 
                        cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests             // go to directory by using cd
                        C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test        // use command py.test
                        C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -v     // To get more information avout test result
                        C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -v -s  // To print all the console logs in terminal
                        
### Step 15: How to run selected Pytests in Terminal from set of Tests?
               --- cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests                                // go to directory by using cd
               --- C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test test_testname.py -v -s      // will run specific test


### Step 16: How to run specific method in Terminal from the set of Test methods?
               --- cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests                                // go to directory by using cd
               --- C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -k methodname -v -s       // will run specific method
               
### Step 17: Grouping tests with pytest marks to run selected group?
               --- Import pytest, write @pytest.mark.smoke/ or anything
                        --- Example: 
                                    import pytest
                                    @pytest.mark.smoke
                                    def first_test():
                                      print('hello')
                           Here the test will be marked as smoke test which can be run in the terminal
               --- cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests                           // go to directory by using cd
               --- C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -m smoke -v -s       // m stands for mark
               
### Step 18: Skip particular test in termnial using mark?
               --- Import pytest, add @pytest.mark.skip
                        --- Example: 
                                    import pytest
                                    @pytest.mark.skip
                                    def first_test():
                                      print('hello')
                           Here the test will be marked as smoke test which can be run in the terminal
               --- cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests                  // go to directory by using cd
               --- C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -v -s       // marked test will be skipped  
               
### Step 19: How to make any specific failed test case to run but not to be added to the report?
               --- Import pytest, add @pytest.mark.xfail
                        --- Example: 
                                    import pytest
                                    @pytest.mark.xfail
                                    def first_test():
                                      print('hello')
                           Here the test will be marked as smoke test which can be run in the terminal
               --- cd C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests                  // go to directory by using cd
               --- C:\Users\ialmu\PycharmProjects\Selenium-Python-Hybrid-Framework-Design\pytests>py.test -v -s       // marked test will be skipped from reporting                    
