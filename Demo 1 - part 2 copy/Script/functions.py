def ChromeStressTest():
            options2 = uc.ChromeOptions()
            prefs = {'credentials_enable_service': False,
                    'profile.password_manager_enabled': False}
            options2.add_experimental_option('prefs',prefs)
            driver = uc.Chrome(options=options2)
            driver.maximize_window()
            driver.execute_script("window.scrollTo(0,0)")
            driver.get('https://www.supremacy1914.com')
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'didomi-notice-agree-button'))
            )
            driver.find_element(By.ID, 'didomi-notice-agree-button').click()
            username = 'k4wn_'
            password = 'D@n1el092009'
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, 'loginbox_login_input'))
            )

            driver.find_element(By.ID, 'loginbox_login_input').send_keys(username)
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'loginbox_password_input'))
            )
            driver.find_element(By.ID, 'loginbox_password_input').send_keys(password)
            driver.find_element(By.ID, 'loginbutton_cont').click()
            wait(1)
            driver.close()
            wait(1)