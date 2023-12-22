import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://intranet-test.roslesinforg.ru/")
driver.find_element(By.NAME, "USER_LOGIN").send_keys("OK_RLI")
driver.find_element(By.NAME, "USER_PASSWORD").send_keys("OK_RLIOK_RLI")
wait = WebDriverWait(driver, 10)
driver.find_element(By.NAME, "USER_SUBMIT").click()
wait.until(EC.title_contains("Доска объявлений"))

driver.find_element(By.LINK_TEXT, "Живая лента").click()
wait.until(EC.title_contains("Рослесинфорг"))

driver.find_element(By.ID, "feed-add-post-form-tab-message").click()

iframe_element: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
driver.switch_to.frame(iframe_element)
driver.find_element(By.TAG_NAME, "body").send_keys("Дорогие друзья, постоянное информационно-техническое \
обеспечение нашей деятельности способствует повышению актуальности дальнейших направлений развитая системы массового \
участия. Равным образом повышение уровня гражданского сознания играет важную роль в формировании всесторонне \
сбалансированных нововведений. Разнообразный и богатый опыт выбранный нами инновационный путь обеспечивает \
актуальность ключевых компонентов планируемого обновления.\
Разнообразный и богатый опыт постоянный количественный рост и сфера нашей активности напрямую зависит от \
соответствующих условий активизации? Повседневная практика показывает, что реализация намеченного \
плана развития играет важную роль в формировании новых предложений. Значимость этих проблем настолько \
очевидна, что новая модель организационной деятельности позволяет выполнить важнейшие задания по разработке \
всесторонне сбалансированных нововведений? Практический опыт показывает, что социально-экономическое развитие \
требует от нас системного анализа модели развития? \
Соображения высшего порядка, а также повышение уровня гражданского сознания \
обеспечивает широкому кругу специалистов участие в формировании направлений прогрессивного развития. \
Равным образом постоянное информационно-техническое обеспечение нашей деятельности напрямую зависит от системы \
обучения кадров, соответствующей насущным потребностям. Задача организации, в особенности же выбранный нами \
инновационный путь играет важную роль в формировании существующих финансовых и административных условий. \
Соображения высшего порядка, а также сложившаяся структура организации влечет за собой процесс внедрения и \
модернизации направлений прогрессивного развития.")

driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption").click()

element_input = wait.until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box")))
element_input.send_keys("Тарасевич Любовь" + Keys.ENTER)

element_profile: WebElement = driver.find_element(By.CSS_SELECTOR,".ui-tag-selector-item.ui-tag-selector-tag.ui-tag-selector-tag--has-avatar")
wait.until(EC.element_to_be_clickable(element_profile))
driver.find_element(By.ID, "blog-submit-button-save").click()

driver.find_element(By.ID, "feed-add-post-form-link-text").click()
element_more:  WebElement = driver.find_element(By.ID, "menu-popup-feed-add-post-form-popup")
wait.until(EC.element_to_be_clickable(element_more))
driver.find_element(By.CSS_SELECTOR, ".menu-popup-item.menu-popup-no-icon.feed-add-post-form-important.feed-add-post-form-important-more").click()

iframe_imp_element: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
driver.switch_to.frame(iframe_imp_element)
driver.find_element(By.TAG_NAME, "body").send_keys("Мир информационных технологий, сокращенно «IT», \
является неизбежной реальностью современной эпохи. Неоспоримо, что с каждым годом IT-отрасль становится все \
более значимой, проникая во все сферы нашей жизни и оказывая огромное влияние на социальный, экономический и \
технологический прогресс.\
IT охватывает широкий спектр деятельности, связанный с разработкой, использованием и управлением информационными \
системами и технологиями. Это включает в себя программирование, сетевые технологии, базы данных, облачные вычисления, \
искусственный интеллект, интернет вещей и множество других областей, каждая из которых вносит свой вклад в развитие \
IT-мира. IT-специалисты играют ключевую роль в создании и сопровождении современных информационных систем. Их задача \
включает разработку и интеграцию программного обеспечения, анализ и оптимизацию данных, обеспечение безопасности \
информации, поддержку пользователей и многое другое. Благодаря их труду мы имеем возможность пользоваться \
многочисленными удобствами и сервисами, которые сделали нашу жизнь проще и комфортнее.")

driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption").click()

element_input = wait.until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box")))
element_input.send_keys("Тарасевич Любовь" + Keys.ENTER)

element_profile: WebElement = driver.find_element(By.CSS_SELECTOR,".ui-tag-selector-item.ui-tag-selector-tag.ui-tag-selector-tag--has-avatar")
wait.until(EC.element_to_be_clickable(element_profile))
driver.find_element(By.ID, "blog-submit-button-save").click()

driver.find_element(By.ID, "feed-add-post-form-link-text").click()
element_more:  WebElement = driver.find_element(By.ID, "menu-popup-feed-add-post-form-popup")
wait.until(EC.element_to_be_clickable(element_more))
driver.find_element(By.CSS_SELECTOR, "menu-popup-feed-add-post-form-popup").click()

iframe_imp_element: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
driver.switch_to.frame(iframe_imp_element)
driver.find_element(By.TAG_NAME, "body").send_keys("Мир информационных технологий, сокращенно «IT», \
является неизбежной реальностью современной эпохи. Неоспоримо, что с каждым годом IT-отрасль становится все \
более значимой, проникая во все сферы нашей жизни и оказывая огромное влияние на социальный, экономический и \
технологический прогресс.\
IT охватывает широкий спектр деятельности, связанный с разработкой, использованием и управлением информационными \
системами и технологиями. Это включает в себя программирование, сетевые технологии, базы данных, облачные вычисления, \
искусственный интеллект, интернет вещей и множество других областей, каждая из которых вносит свой вклад в развитие \
IT-мира. IT-специалисты играют ключевую роль в создании и сопровождении современных информационных систем. Их задача \
включает разработку и интеграцию программного обеспечения, анализ и оптимизацию данных, обеспечение безопасности \
информации, поддержку пользователей и многое другое. Благодаря их труду мы имеем возможность пользоваться \
многочисленными удобствами и сервисами, которые сделали нашу жизнь проще и комфортнее.")

driver.switch_to.default_content()
# Кому сообщение
driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption").click()
element_input = wait.until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box")))
element_input.send_keys("Тарасевич Любовь" + Keys.ENTER)
element_profile: WebElement = driver.find_element(By.CSS_SELECTOR,".ui-tag-selector-item.ui-tag-selector-tag.ui-tag-selector-tag--has-avatar")
wait.until(EC.element_to_be_clickable(element_profile))

driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption").click()

driver.find_element(By.ID, "blog-submit-button-save").click()

# driver.find_element(By.CSS_SELECTOR, ".menu-popup-item.menu-popup-no-icon.feed-add-post-form-file.feed-add-post-form-file-more").click()
# driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption").click()
# element_input = wait.until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box")))
# element_input.send_keys("Тарасевич Любовь" + Keys.ENTER)
#
# driver.find_element(By.CSS_SELECTOR, ".ui-tile-uploader-drop-label").send_keys("D:/test_file/test.jpg")
